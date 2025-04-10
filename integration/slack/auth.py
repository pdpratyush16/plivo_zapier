class SlackAuth:
    def __init__(self, token: str):
        if not token.startswith("xoxb-"):
            raise ValueError("Invalid Slack token format.")
        self.token = token

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
