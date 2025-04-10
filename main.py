from integration.slack.slack import SlackIntegration
# Later: import GmailIntegration, ShopifyIntegration

class IntegrationManager:
    _integrations = {
        "slack": SlackIntegration,
        # "gmail": GmailIntegration,
        # "shopify": ShopifyIntegration,
    }

    @classmethod
    def get_integration(cls, name, **kwargs):
        integration_class = cls._integrations.get(name.lower())
        if not integration_class:
            raise ValueError(f"Unknown integration: {name}")
        return integration_class(**kwargs)
