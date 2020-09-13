## Dobato - 堂鳩

[Dobato (堂鳩)](https://www.suntory.co.jp/eco/birds/encyclopedia/detail/4642.html)
is a simple tool to send a message to slack/discord.

### Preparation

Create `.discord` on your HOME directory.

```bash
> cat $HOME/.discord
https://discordapp.com/api/webhooks/xxxxxxxxxxxx/yyyyyyyyyyyyyyyyyyyyyyyyy
```

### Install

`pip install .`

### From shell

```bash
python3 -m dobato.notify --text "hello, world"
```

### From script

```python
from dobato import notify


notify.notify("sample from script", dry_run=False)
```
