# API-tempo

This repo shows a useage example of tempo-api-python-client library by [stanislavulrych](https://github.com/stanislavulrych).

The library is intended to simplify the usage and interactions with Tempo timeshits. 
To access the library documentation click [here](https://github.com/stanislavulrych/tempo-api-python-client).


The current example uses the get_worklogs method to get tempo timesheets and then uses the method get_team_members to get the employees from a team.

Finally it filters the timesheets belonging to the team members and iterates over the worklogs to get an accumulated registerd time for each employee.   

# Instalation
Use the package manager pip to install tempo-api-python-client.
```bash
pip install tempo-api-python-client
```
Then download this repo to try out the example.

# Usage 

In order to use the tempo api you'll need your Atlassian api key. 
```bash
from tempoapiclient import client

tempo = client.Tempo(
        auth_token="<your_atlassian_api_key>",
        base_url="https://api.tempo.io/core/3")
        
worklogs = tempo.get_worklogs(
        dateFrom= '2020-10-10',
        dateTo= '2020-10-15'
        )
for i in worklogs:
  print(i)
```
