# ###########################
#
import logging

from cockpitdecks import DECK_ACTIONS
from cockpitdecks.buttons.activation import Activation

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


class ActivationTemplate(Activation):
    """Template class for activation"""

    ACTIVATION_NAME = "activation-template"
    REQUIRED_DECK_ACTIONS = [DECK_ACTIONS.PRESS, DECK_ACTIONS.LONGPRESS, DECK_ACTIONS.PUSH]

    def __init__(self, button: "Button"):
        Activation.__init__(self, button=button)

    def activate(self, event):
        super().activate(event)
