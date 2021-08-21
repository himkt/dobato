import argparse

from dobato.dobato import setup, notify  # noqa


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    setup_parser = sub_parser.add_parser("setup")
    setup_parser.set_defaults(fn=setup)

    notify_parser = sub_parser.add_parser("notify")
    notify_parser.add_argument("text")
    notify_parser.set_defaults(fn=notify)

    args = parser.parse_args()
    args.fn(args)
