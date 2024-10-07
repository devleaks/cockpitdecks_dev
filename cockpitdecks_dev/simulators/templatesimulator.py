# Class for interface with X-Plane using UDP protocol.
#
from cockpitdecks.simulator import Simulator, Instruction, SimulatorEvent


class SimulatorTemplate(Simulator):
    """ """

    name = "simulator-template"

    def __init__(self, cockpit, environ):
        self.init()

    def init(self):
        if self._inited:
            return
        self._inited = True

    def __del__(self):
        if not self._inited:
            return

    def create_instruction(self, name, **kwargs):
        return Instruction(name=name)

    def create_replay_event(self, name: str, value):
        return SimulatorEvent(sim=self)

    def runs_locally(self) -> bool:
        return True

    # ################################
    # Simulator Interface
    #
    def start(self):
        pass

    def stop(self):
        pass

    # ################################
    # Cockpit interface
    #
    def terminate(self):
        pass
