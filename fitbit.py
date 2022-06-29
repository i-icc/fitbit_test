import requests


class Fitbit:
    def __init__(self, client_id, client_secret, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token
        self.url = "https://api.fitbit.com/1/user/-/"

    def user(self):
        endpoint = "profile.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url+endpoint, headers=headers)
        user = {
            "fullName" : r.json()["user"]["fullName"],
            "age" : r.json()["user"]["age"],
            "dateOfBirth": r.json()["user"]["dateOfBirth"],
            "gender" : r.json()["user"]["gender"],
            "height" : r.json()["user"]["height"],
            "averageDailySteps" : r.json()["user"]["averageDailySteps"],
            "weight" : r.json()["user"]["weight"],
        }
        return user
