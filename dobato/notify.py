#!/usr/bin/env python3

import argparse
import json
import os


home_dir = os.getenv("HOME")
if home_dir is None:
    raise ValueError("$HOME is not determined")


def _load_webhook_url():
    discord_config = os.path.join(home_dir, ".discord")
    if os.path.exists(discord_config):
        return "content", open(discord_config).read().rstrip("\n")

    slack_config = os.path.join(home_dir, ".slack")
    if os.path.exists(slack_config):
        return "text", open(slack_config).read().rstrip("\n")

    raise Exception(
        "You have to put discord webhook url on $HOME/.discord"
        " or slack webhook url on $HOME/.slack"
    )


def notify(text: str, dry_run: bool = False) -> None:
    key, url = _load_webhook_url()
    payload = json.dumps({key: text})

    command = "curl {} -X POST -H \"Content-Type: application/json\" -d '{}'".format(
        url,
        payload,
    )

    if dry_run:
        print(command)

    else:
        os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, default="empty")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    notify(args.text, dry_run=args.dry_run)
