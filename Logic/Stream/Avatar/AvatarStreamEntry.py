import json
from Utils.Writer import Writer




class AvatarStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 6
    
    def encode(self):

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        if self.player.Major <= 4: # Under v5.x.x
            self.writeInt(0)  # SenderAvatarHighID
            self.writeInt(1)  # SenderAvatarLowID

        self.writeString(self.player.Name)  # Name

        self.writeInt(1)  # SenderLevel
        if self.player.Major >= 5: # v5.x.x or above
            self.writeInt(0)  # SenderLeagueType
        self.writeInt(0)  # AgeSeconds

        self.writeByte(0)  # IsRemoved
        self.writeByte(1)  # IsNew