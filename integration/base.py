class BaseIntegration:
    def __init__(self, **kwargs):
        self.auth = self.authenticate(**kwargs)

    def authenticate(self, **kwargs):
        raise NotImplementedError("Authentication method must be implemented.")
