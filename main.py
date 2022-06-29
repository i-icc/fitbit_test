import json
from fitbit import Fitbit

with open("./env.json", "r") as f:
    tokens = json.load(f)
    CLIENT_ID = tokens["client_id"]
    CLIENT_SECRET = tokens["client_secret"]
    TOKEN = tokens["token"]


def main():
    fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, TOKEN)
    print(fitbit.user())


if __name__ == "__main__":
    main()
