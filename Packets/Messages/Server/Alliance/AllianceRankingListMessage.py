import json
from Utils.Writer import Writer
from Logic.AllianceRankingEntry import AllianceRankingEntry


class AllianceRankingListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24403
    
    def  encode(self):

        self.count = 0
        
        self.writeInt(0)  # DefaultHighID
        self.writeInt(1)  # DefaultLowID
        self.writeString('Clashers') # Name
        self.writeInt(self.count + 1)
        self.writeInt(0) # Score
        self.writeInt(200)

        AllianceRankingEntry.encode(self)

        #if count >= 199:
        #    break


        self.writeInt(self.count)
        self.writeInt(0)

        self.writeInt(604800) # Tournament Seconds left - 7 Days -> 604800 (GetSecondsUntilNextMonth)

        self.writeInt(3) # Reward Count
        self.writeInt(100000) # #1 Reward
        self.writeInt(10000) # #2 Reward
        self.writeInt(1000) # #3 Reward