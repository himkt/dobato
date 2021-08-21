import argparse
import os
import json


DOBATO_DIR = os.path.join(os.path.expanduser("~"), ".config/dobato")
WEBHOOK_URL_PATH = os.path.join(DOBATO_DIR, "webhook_url")


def setup(_: argparse.ArgumentParser):
    webhook_url = input("Discord webhook url: ")

    os.makedirs(DOBATO_DIR, exist_ok=True)
    with open(WEBHOOK_URL_PATH, "w") as f:
        print(webhook_url, file=f)


def notify(args: argparse.ArgumentParser):
    notify_fn(args.text)


def notify_fn(text: str):
    if not os.path.exists(WEBHOOK_URL_PATH):
        raise Exception(
            "You have not configured dobato."
            " Run `dobato setup` to save a webhook url."
        )

    webhook_url = open(WEBHOOK_URL_PATH).readline().rstrip()
    payload = json.dumps({"content": text})
    command = (
        f"curl {webhook_url} -X POST"
        f" -H \"Content-Type: application/json\""
        f" -d '{payload}'"
    )
    os.system(command)
