import json
from Utils.Writer import Writer
from Logic.Stream.Avatar.AvatarStreamEntry import *



class JoinAllianceResponseAvatarStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 3
    
    def encode(self):

        if self.player.Major >= 5: # v5.x.x or above
            self.writeInt(0)  # AllianceHighID
            self.writeInt(1)  # AllianceLowID

            self.writeString('Clashers')  # AllianceName

            self.writeInt(13000000)  # AllianceBadge

            self.writeString('Attention Clanmates: ')  # Message

            self.writeByte(1)

            self.writeInt(0)  # SenderHomeHighID
            self.writeInt(1)  # SenderHomeLowID
        else:
            self.writeInt(3)  # StreamEntryType

            AvatarStreamEntry.encode(self)

            self.writeInt(0)  # AllianceHighID
            self.writeInt(1)  # AllianceLowID

            self.writeString('Clashers')  # AllianceName

            self.writeInt(13000000)  # AllianceBadge