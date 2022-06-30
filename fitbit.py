import requests
import datetime

class Fitbit:
    def __init__(self, client_id, client_secret, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token
        self.url = "https://api.fitbit.com/1.2/user/-/"

    def user(self):
        endpoint = "profile.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url+endpoint, headers=headers)
        user = {
            "fullName": r.json()["user"]["fullName"],
            "age": r.json()["user"]["age"],
            "dateOfBirth": r.json()["user"]["dateOfBirth"],
            "gender": r.json()["user"]["gender"],
            "height": r.json()["user"]["height"],
            "averageDailySteps": r.json()["user"]["averageDailySteps"],
            "weight": r.json()["user"]["weight"],
        }
        return user

    def get_activity_log(self, Date=datetime.date.today(), isBefore=True, sort="asc", limit=10, offset=0):
        endpoint = "activities/list.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "sort": sort,
            "limit": limit,
            "offset": offset,
        }
        if isBefore:
            params["beforeDate"] = Date
        else :
            params["afterDate"] = Date
        r = requests.get(self.url+endpoint, headers=headers, params=params)
        if r.reason == "Bad Request":
            print(r.reason)
            print('Maybe the format is different." The "beforeDate" and "afterDate" should be in the format yyyy-MM-dd.')
        return r.json()
    
    def get_sleep_log(self, Date=datetime.date.today()):
        endpoint = f"sleep/date/{Date}.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url+endpoint, headers=headers)
        return r.json()
