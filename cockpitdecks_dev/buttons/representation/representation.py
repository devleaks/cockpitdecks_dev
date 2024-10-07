from cockpitdecks.buttons.representation import Representation


class RepresentationTemplate(Representation):
    """Representation template"""

    REPRESENTATION_NAME = "representation-template"

    PARAMETERS = {}

    def __init__(self, button: "Button"):
        Representation.__init__(self, button=button)

    def render(self):
        """ """
        return None
