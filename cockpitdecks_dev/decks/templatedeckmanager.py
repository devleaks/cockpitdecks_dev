""" Virtual Deck Manager.

Discover virtual web decks
"""

from .templatedeck import TemplateDeck


class TemplateDeckManager:

    @staticmethod
    def enumerate() -> Dict[str, TemplateDeck]:
        """Returns all the template deck devices available to Cockpitdecks."""
        return {}
