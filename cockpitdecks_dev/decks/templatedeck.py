# Cockpitdecks Template Deck driver.
#
from cockpitdecks.deck import Deck
from .templatedeckmanager import TemplateDeckManager


class TemplateDeck(Deck):
    """
    Template
    """

    DECK_NAME = "templatedeck"
    DRIVER_NAME = "templatedeckdriver"
    MIN_DRIVER_VERSION = "0.0.0"
    DEVICE_MANAGER = TemplateDeckManager

    def __init__(self, name: str, config: dict, cockpit: "Cockpit", device=None):
        Deck.__init__(self, name=name, config=config, cockpit=cockpit, device=device)

        self.cockpit.set_logging_level(__name__)

    # #######################################
    #
    # Deck Specific Functions : Definition
    #
    def make_default_page(self):
        pass

    # #######################################
    #
    # Deck Specific Functions : Activation
    #
    def key_change_callback(self, key, state: int, data: dict | None = None) -> Event | None:
        """
        This is the function that is called when a key is pressed.
        For virtual decks, this function is quite complex
        since it has to take the "shape" of any "real physical deck" it virtualize
        Event codes:
         0 = Push/press RELEASE
         1 = Push/press PRESS
         2 = Turned clockwise
         3 = Turned counter-clockwise
         4 = Pulled
         9 = Slider, event data contains value
        10 = Touch start, event data contains value
        11 = Touch end, event data contains value
        12 = Swipe, event data contains value
        14 = Tap, event data contains value

        """
        # logger.debug(f"Deck {self.name} Key {key} = {state}")
        # print("===== handle_event", self.name, key, state, data)
        return None

    # #######################################
    #
    # Deck Specific Functions : Representation
    #
    def print_page(self, page: Page):
        """
        Ask each button to send its representation and create an image of the deck.
        """
        pass

    def render(self, button: Button):  # idx: int, image: str, label: str = None):
        pass

    # #######################################
    #
    # Deck Specific Functions : Operations
    #
    def start(self):
        pass

    def stop(self):
        pass

    @staticmethod
    def terminate_device(device, name: str = "unspecified"):
        logger.info(f"{name} terminated")
