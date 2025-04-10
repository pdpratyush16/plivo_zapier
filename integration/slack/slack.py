from .auth import SlackAuth
from .actions import SlackActions
from ..base import BaseIntegration

class SlackIntegration(BaseIntegration):
    def authenticate(self, **kwargs):
        return SlackAuth(token=kwargs.get("token"))

    def send_message(self, channel: str, text: str):
        actions = SlackActions(self.auth)
        return actions.send_message(channel, text)
