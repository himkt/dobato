#!/usr/bin/env python3

import argparse
import json
import os


home_dir = os.getenv("HOME")
if home_dir is None:
    raise ValueError("$HOME is not determined")
discord_config = os.path.join(home_dir, ".discord")


def _load_webhook_url():
    if os.path.exists(discord_config):
        return open(discord_config).read().rstrip("\n")
    raise Exception("You have to put discord webhook url on $HOME/.discord")


def notify(text: str, dry_run: bool = False) -> None:
    payload = json.dumps({
        "wait": True,
        "content": text,
    })

    command = "curl {} -X POST -H \"Content-Type: application/json\" -d '{}'".format(
        _load_webhook_url(),
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
