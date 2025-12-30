import json
from Utils.Writer import Writer




class AvatarStreamEntryMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.device = client
        self.player = player
        self.id = 24412
    
    def encode(self):

        pass
        
        #self.writeInt(1)  # StreamEntryType

        #self.writeInt(0)  # HighID
        #self.writeInt(1)  # LowID

        #self.writeInt(0)  # SenderAvatarHighID
        #self.writeInt(1)  # SenderAvatarLowID

        #self.writeString(self.player.Name)  # Name

        #self.writeInt(1)  # SenderLevel
        #self.writeInt(0)  # SenderLeagueType
        #self.writeInt(0)  # AgeSeconds

        #self.writeByte(0)  # IsRemoved
        # self.writeByte(1)  # IsNew