import requests
... 
... CLIENT_ID = "178940"
... CLIENT_SECRET = "518a6caf89b06b1ce0a8b8ce47a9b367d66a5d5b"
... AUTHORIZATION_CODE = "5b60176c6377840d74658ff4e835dd553530fc6e"
... 
... response = requests.post(
...     "https://www.strava.com/oauth/token",
...     data={
...         'client_id': CLIENT_ID,
...         'client_secret': CLIENT_SECRET,
...         'code': AUTHORIZATION_CODE,
...         'grant_type': 'authorization_code'
...     }
... )
... 
... tokens = response.json()
... print("Status code:", response.status_code)
... print("Response:", tokens)
... 
Status code: 400
Response: {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
>>> import requests
... 
... CLIENT_ID = "178940"
... CLIENT_SECRET = "518a6caf89b06b1ce0a8b8ce47a9b367d66a5d5b"
... AUTHORIZATION_CODE = "5b60176c6377840d74658ff4e835dd553530fc6e"
... 
... response = requests.post(
...     "https://www.strava.com/oauth/token",
...     data={
...         'client_id': CLIENT_ID,
...         'client_secret': CLIENT_SECRET,
...         'code': AUTHORIZATION_CODE,
...         'grant_type': 'authorization_code'
...     }
... )
... 
... tokens = response.json()
... print("Status code:", response.status_code)
... print("Response:", tokens)
... 
Status code: 400
Response: {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
>>> import requests
... 
... CLIENT_ID = "178940"
... CLIENT_SECRET = "518a6caf89b06b1ce0a8b8ce47a9b367d66a5d5b"
... AUTHORIZATION_CODE = "961a6b1eed915593a704cb7a307b1256804eac1c"
... 
... response = requests.post(
...     "https://www.strava.com/oauth/token",
...     data={
...         'client_id': CLIENT_ID,
...         'client_secret': CLIENT_SECRET,
...         'code': AUTHORIZATION_CODE,
...         'grant_type': 'authorization_code'
...     }
... )
... 
... tokens = response.json()
... print("Status code:", response.status_code)
... print("Response:", tokens)
... 
Status code: 200
Response: {'token_type': 'Bearer', 'expires_at': 1759190354, 'expires_in': 20603, 'refresh_token': '771000efe9f551aba8a5a499801ae88059a3d7c5', 'access_token': '5e78364611787dfafc9e51e3feb2c34c026c4e54', 'athlete': {'id': 91488890, 'username': None, 'resource_state': 2, 'firstname': 'Billy', 'lastname': 'Hill', 'bio': None, 'city': 'Somerset ', 'state': 'New Jersey', 'country': None, 'sex': 'M', 'premium': False, 'summit': False, 'created_at': '2021-08-30T16:07:53Z', 'updated_at': '2025-09-29T17:07:47Z', 'badge_type_id': 0, 'weight': 63.5029, 'profile_medium': 'https://dgalywyr863hv.cloudfront.net/pictures/athletes/91488890/21797419/2/medium.jpg', 'profile': 'https://dgalywyr863hv.cloudfront.net/pictures/athletes/91488890/21797419/2/large.jpg', 'friend': None, 'follower': None}}
>>> 
>>> import requests
... import pandas as pd
... 
... ACCESS_TOKEN = "5e78364611787dfafc9e51e3feb2c34c026c4e54"
... 
... activities_url = "https://www.strava.com/api/v3/athlete/activities"
... all_activities = []
... page = 1
... per_page = 200  # max per page
... 
... while True:
...     response = requests.get(
...         activities_url,
...         headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
...         params={"page": page, "per_page": per_page}
...     )
...     
...     if response.status_code != 200:
...         print("Error:", response.status_code, response.text)
...         break
...     
...     data = response.json()
...     if not data:
...         break
...     
...     all_activities.extend(data)
...     page += 1
... 
... if all_activities:
...     df = pd.json_normalize(all_activities)
...     df.to_csv("strava_activities.csv", index=False)
...     print(f"Saved {len(df)} activities to strava_activities.csv")
... else:
...     print("No activities found.")
... 
python3 download_strava_activities.py


python3
Saved 2512 activities to strava_activities.csv
