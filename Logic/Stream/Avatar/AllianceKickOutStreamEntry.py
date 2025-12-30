import json
from Utils.Writer import Writer




class AllianceKickOutStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 5

    def encode(self):

        self.writeString('Bye!')  # Message

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString('Clashers')  # AllianceName

        self.writeInt(13000000)  # AllianceBadge