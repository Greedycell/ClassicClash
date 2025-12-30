import json
from Utils.Writer import Writer




class JoinRequestAllianceStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 3

    def encode(self):

        self.writeString('I want to join your Alliance')  # Message
        self.writeString(self.player.Name)  # ResponderName

        self.writeInt(0)  # State