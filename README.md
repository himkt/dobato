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
python3 -m discord_webhook.notify --text "hello, world"
```

### From script

```python
from discord_webhook import notify


notify.notify("sample from script", dry_run=False)
```
