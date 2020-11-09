# To import temploapiclient first pip install tempo-api-python-client
from tempoapiclient import client
import datetime

def execute(request):

    # Get todays date
    today = datetime.date.today() #+ datetime.timedelta(days=2)

    # Get friday when current day is mondey or weekend, else get today -1
    if today.isoweekday() == 1: 
        yesterday = today - datetime.timedelta(days=3)
    elif today.isoweekday() == 7:
        yesterday = today - datetime.timedelta(days=2) 
    else:
        yesterday = today - datetime.timedelta(days=1)

    # Tempo API Auth
    tempo = client.Tempo(
        auth_token="<your_atlassian_api_key>",
        base_url="https://api.tempo.io/core/3")

    # Get tempo worksheets from yesterday
    worklogs = tempo.get_worklogs(
        dateFrom= yesterday,
        dateTo= yesterday
        )

    # Get all tempo users in Service Delivey team, id=6
    users_info = tempo.get_team_members(6)

    # Append users into users list variable
    users = []
    for user in users_info:
        users.append(user['member']['displayName']) 

    tempo_sheet = {}
    date = str(yesterday)
    acc_time = 0

    # Add all users from Service Delivery Team to tempo_sheet dictionary and set accumulated time to cero
    # tempo_sheet format --> {NameLastname: {employee: 'Name LastName', accum_time: 0}, ...}
    for user in users:
        user_dict = {}
        user_dict["employee"] = user
        user_dict["accum_time"] = 0
        tempo_sheet[user.replace(' ', '')] = user_dict

    # Walk through employees worklogs and add their registered hours to tempo_sheet
    for i in worklogs:
        employee = i['author']['displayName']
        empl_key = employee.replace(' ', '')

        # Only for employees in Service Delivery Team add time from worklog into accum_time
        if employee in users:
            time = i['timeSpentSeconds'] / (60*60)
            tempo_sheet[empl_key]["accum_time"] += time
    
    return {'employee': tempo_sheet['MarianoVictory']['employee'], 'date': date, 'acc_time': tempo_sheet['MarianoVictory']['accum_time']}
    