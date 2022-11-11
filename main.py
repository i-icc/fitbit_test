import json
from fitbit import Fitbit
import datetime

with open("./env.json", "r") as f:
    tokens = json.load(f)
    CLIENT_ID = tokens["client_id"]
    CLIENT_SECRET = tokens["client_secret"]
    TOKEN = tokens["token"]


def main():
    fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, TOKEN)
    # print(fitbit.user())
    # print(fitbit.get_activity_log("2022-06-25"))
    print(fitbit.get_sleep_log_graph())
    # print(fitbit.get_hrv())


if __name__ == "__main__":
    main()
