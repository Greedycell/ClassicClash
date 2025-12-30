import json
from Utils.Writer import Writer



class AllianceFullEntry(Writer):

    def encode(self):

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString('Clashers')  # AllianceName
    
        self.writeInt(13000000)  # AllianceBadge

        self.writeInt(0)  # AllianceType
        self.writeInt(1)  # NumberOfMembers
        self.writeInt(0)  # Score
        self.writeInt(0)  # RequiredScore

        self.writeString('Welcome to Clash of Clans!')  # AllianceDescription
        
        self.writeInt(1)  # AllianceMembers

        self.writeInt(0)  # AvatarHighID
        self.writeInt(1)  # AvatarLowID

        self.writeString(None)  # FacebookID
        self.writeString(self.player.Name)  # Name

        self.writeInt(0)  # Role
        self.writeInt(1)  # ExpLevel
        self.writeInt(0)  # LeagueType
        self.writeInt(0)  # Score
        self.writeInt(0)  # Donations
        self.writeInt(0)  # DonationsReceived
        self.writeInt(0)  # Order
        self.writeInt(0)  # PreviousOrder

        self.writeByte(0)  # IsNewMember
        self.writeByte(1)

        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeHighID