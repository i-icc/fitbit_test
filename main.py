import fitbit
import json

with open("./env.json", "r") as f:
    tokens = json.load(f)
    CLIENT_ID = tokens["client_id"]
    CLIENT_SECRET = tokens["client_secret"]
    TOKEN = tokens["token"]

def main():
    print(CLIENT_ID)
    print(CLIENT_SECRET)
    print(TOKEN)

if __name__ == "__main__":
    main()