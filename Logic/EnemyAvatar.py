import json
from Utils.Writer import Writer



class EnemyAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(0)  # DefaultHighID
        self.writeInt(1)  # DefaultLowID
        self.writeInt(0)  # CurrentHomeHighID
        self.writeInt(1)  # CurrentHomeLowID

        self.writeByte(0)  # IsInAlliance
        self.writeByte(0)
        self.writeByte(0)

        self.writeInt(0)  # LeagueType

        self.writeInt(0)
        self.writeInt(10)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString('Chief')  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(1)   # ExpLevel
        self.writeInt(0)  # ExpPoints
        self.writeInt(0)  # Diamonds
        self.writeInt(0)  # FreeDiamonds
        self.writeInt(0)  # AttackRating
        self.writeInt(0)  # AttackKFactor
        self.writeInt(0)  # Score
        self.writeInt(0)  # AttackWinCount
        self.writeInt(0)  # AttackLoseCount
        self.writeInt(0)  # DefenseWinCount
        self.writeInt(0)  # DefenseLoseCount
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeByte(0)  # NameSetByUser

        self.writeByte(0)

        self.writeInt(0) # CumulativePurchasedDiamonds

        ##### ARAYS #####

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)