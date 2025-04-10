import requests

class SlackActions:
    def __init__(self, auth):
        self.auth = auth

    def send_message(self, channel: str, text: str):
        url = "https://slack.com/api/chat.postMessage"
        payload = {
            "channel": channel,
            "text": text
        }
        headers = self.auth.get_headers()
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
