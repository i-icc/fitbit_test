import requests
import datetime
from matplotlib import pyplot


class Fitbit:
    def __init__(self, client_id, client_secret, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token
        self.url = "https://api.fitbit.com/1/user/-/"
        self.url2 = "https://api.fitbit.com/1.2/user/-/"

    def user(self):
        endpoint = "profile.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url2+endpoint, headers=headers)
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
        else:
            params["afterDate"] = Date
        r = requests.get(self.url2+endpoint, headers=headers, params=params)
        if r.reason == "Bad Request":
            print(r.reason)
            print('Maybe the format is different." The "beforeDate" and "afterDate" should be in the format yyyy-MM-dd.')
        return r.json()

    def get_sleep_log(self, Date=datetime.date.today()):
        endpoint = f"sleep/date/{Date}.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url2+endpoint, headers=headers)
        return r.json()

    def get_hrv(self, Date=datetime.date.today()):
        endpoint = f"hrv/date/{Date}.json"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(self.url+endpoint, headers=headers)
        return r.json()

    def get_sleep_log_graph(self, Date=datetime.date.today()):
        datas = self.get_sleep_log(Date)
        sleep_level_log = []
        levels = {
            "wake": 3,
            "rem": 2,
            "light": 1,
            "deep": 0
        }
        for data in datas["sleep"][0]["levels"]["data"]:
            sleep_level_log += [levels[data["level"]]
                                for i in range(data["seconds"])]
        pyplot.plot(range(len(sleep_level_log)), sleep_level_log)
        pyplot.yticks([0, 1, 2, 3],
                      ['deep', 'light', 'rem', "wake"])
        pyplot.show()

    def get_sleep_frequency_graph(self, Date=datetime.date.today()):
        datas = self.get_sleep_log(Date)
        sleep_level_frequency = [0, 0, 0, 0]
        levels = {
            "wake": 3,
            "rem": 2,
            "light": 1,
            "deep": 0
        }
        for data in datas["sleep"][0]["levels"]["data"]:
            sleep_level_frequency[levels[data["level"]]] += data["seconds"]
        pyplot.bar(range(len(sleep_level_frequency)), sleep_level_frequency)
        pyplot.xticks([0, 1, 2, 3],
                      ['deep', 'light', 'rem', "wake"])
        pyplot.show()
