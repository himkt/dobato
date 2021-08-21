## Dobato - 堂鳩

[Dobato (堂鳩)](https://www.suntory.co.jp/eco/birds/encyclopedia/detail/4642.html)
is a simple tool to send a message to slack/discord.


### Install

`pip install dobato`


### Configure discord webhook

Run `python -m dobato setup`.

```bash
> poetry run python -m dobato setup
Discord webhook url: https://example.com/webhook
```


### Notify as a command

```bash
python3 -m dobato notify "Hello, World."
```


### Using dobato in a Python script

```python
from dobato import notify_fn

notify_fn("text")
```
