import json
from Utils.Writer import Writer
from Logic.AvatarRankingEntry import AvatarRankingEntry


class AvatarLocalRankingListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24403
    
    def  encode(self):

        self.count = 0
        
        self.writeInt(self.player.HighID)  # DefaultHighID
        self.writeInt(self.player.LowID)  # DefaultLowID
        self.writeString(self.player.Name) # Name
        self.writeInt(self.count + 1)
        self.writeInt(self.player.Score) # Score
        self.writeInt(200) 

        AvatarRankingEntry.encode(self)
        self.count += 1


        self.writeInt(self.count)
        self.writeInt(0)