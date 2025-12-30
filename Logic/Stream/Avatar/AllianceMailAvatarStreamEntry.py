import json
from Utils.Writer import Writer




class AllianceMailAvatarStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 6

    def encode(self):

        self.writeString('Attention Clanmates: ')  # Message

        self.writeByte(1)

        self.writeInt(0)  # SenderHomeHighID
        self.writeInt(1)  # SenderHomeLowID

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString('Clashers')  # AllianceName

        self.writeInt(13000000)  # AllianceBadge