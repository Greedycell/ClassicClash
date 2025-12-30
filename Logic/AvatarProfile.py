import json
from Utils.Writer import Writer



class AvatarProfile(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(0)  # DefaultHighID
        self.writeInt(1)  # DefaultLowID
        self.writeInt(0)  # CurrentHomeHighID
        self.writeInt(1)  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString('Clashers')  # AllianceName

        self.writeInt(13000000)  # AllianceBadge
        self.writeInt(0)  # AllianceRole

        self.writeByte(1)

        self.writeInt(0)  # LeagueInstanceHighID
        self.writeInt(1)  # LeagueInstanceLowID

        self.writeByte(1)

        self.writeInt(0)  # LastLeagueInstanceHighID
        self.writeInt(1)  # LastLeagueInstanceLowID
        self.writeInt(0)  # LeagueType

        self.writeInt(0)
        self.writeInt(10)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString('You')  # Name
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