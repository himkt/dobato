#!/usr/bin/env python3

import argparse
import json
import os


class WebhookNotifier:
    def __init__(self, provider: str = "auto", dry_run: bool = False):
        key, url = self._load_webhook_url(provider)
        self.key = key
        self.url = url
        self.dry_run = dry_run

    def _load_webhook_url(self, provider: str):
        home_dir = os.getenv("HOME")
        if home_dir is None:
            raise ValueError("$HOME is not determined")

        if provider in ("discord", "auto"):
            discord_config = os.path.join(home_dir, ".discord")
            if os.path.exists(discord_config):
                return "content", open(discord_config).read().rstrip("\n")

        if provider in ("slack", "auto"):
            slack_config = os.path.join(home_dir, ".slack")
            if os.path.exists(slack_config):
                return "text", open(slack_config).read().rstrip("\n")

        raise Exception(
            "You have to put discord webhook url on $HOME/.discord"
            " or slack webhook url on $HOME/.slack"
        )

    def _construct_command(self, text: str):
        payload = json.dumps({self.key: text})
        return (
            "curl {}"
            " -X POST"
            " -H \"Content-Type: application/json\""
            " -d '{}'"
        ).format(self.url, payload)

    def notify(self, text: str) -> None:
        command = self._construct_command(text)

        if self.dry_run:
            print(command)
        else:
            os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, default="empty")
    parser.add_argument("--provider", type=str, default="auto")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    notifier = WebhookNotifier(
        dry_run=args.dry_run,
        provider=args.provider
    )
    notifier.notify(args.text)
