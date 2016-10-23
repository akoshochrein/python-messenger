# python-messenger
Messenger bot base class for python application

## Example

```py
from messenger import Bot

class EchoBot(Bot):
    def handle_message(self, messaging_event):
        self.send_text_message(messaging_event['sender']['id'], messaging_event['message']['text']
```