from networktables import NetworkTables

import logging
from constants import Constants
logging.basicConfig(level=logging.DEBUG)


class Vision():
    """A network table interface bewteen the robot 
       and the raspberry pi for vision tracking."""

    def __init__(self):
        NetworkTables.initialize()
        self.table = NetworkTables.getTable("vision")
        self.errors = []
        self.movement = [0, 0]

    def update(self):
        self.updateErrors()
        self.updateMovement()

    def updateErrors(self):
        self.errors = self.table.getNumberArray("error", [])

    def updateMovement(self):
        if len(self.errors) != 2:
            print(
                "ERROR: Expected 2 vison errors but only one was found, skipping updating movement")
            return
        self.movement[0] = self.errors[0] * Constants.VISION_MOVEMENT_KP_X
        self.movement[1] = self.errors[1] * Constants.VISION_MOVEMENT_KP_Y
        print(self.movement)

    def isAligned(self):
        if len(self.errors) != 2:
            return False
        return (abs(self.errors[0]) <= Constants.VISION_ERROR_THRESH_X) and (abs(self.errors[1]) <= Constants.VISION_ERROR_THRESH_Y)

    def _connectionListener(self, connected, info):
        """Outputs connection data."""
        print(info, "; Connected=%s" % connected)
