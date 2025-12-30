import json
from Utils.Writer import Writer



class AllianceStreamEntryMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24312

    def encode(self):

        self.writeInt(0)  # StreamEntryType

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeInt(0)  # SenderAvatarHighID
        self.writeInt(1)  # SenderAvatarLowID

        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeLowID

        self.writeString(self.player.Name)  # Name

        self.writeInt(1)  # SenderLevel
        self.writeInt(0)  # SenderLeagueType
        self.writeInt(0)  # AgeSeconds

        self.writeByte(0)  # IsRemoved
        self.writeByte(1)  # IsNew