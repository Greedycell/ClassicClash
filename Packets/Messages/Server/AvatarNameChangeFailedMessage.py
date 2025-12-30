import json
from Utils.Writer import Writer



class AvatarNameChangeFailedMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20205
        self.version = 1

    def encode(self):
        self.writeInt(1)