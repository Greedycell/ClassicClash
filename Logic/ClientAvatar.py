import json
from Utils.Writer import Writer



class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(self.player.HighID)  # DefaultHighID
        self.writeInt(self.player.LowID)  # DefaultLowID
        self.writeInt(self.player.HighID)  # CurrentHomeHighID
        self.writeInt(self.player.LowID)  # CurrentHomeLowID

        self.writeByte(self.player.IsInAlliance)  # IsInAlliance
        if self.player.IsInAlliance:
            self.writeInt(0)  # AllianceHighID
            self.writeInt(1)  # AllianceLowID

            self.writeString('Clashers')  # AllianceName

            self.writeInt(13000000)  # AllianceBadge
            self.writeInt(0)  # AllianceRole

            if self.player.Major >= 5: # v5.x.x or above
                self.writeByte(0)

            if self.player.Major > 6 or (self.player.Major == 6 and self.player.Minor >= 253): # v6.253.x or above
                self.writeInt(0)
                self.writeInt(1)

        if self.player.Major >= 5: # v5.x.x or above
            self.writeInt(self.player.LeagueType) # LeagueType

        self.writeInt(0) # Alliance Castle Level
        self.writeInt(10) # Alliance Total Capacity
        self.writeInt(0) # Alliance Used Capacity
        self.writeInt(0) # Townhall Level

        self.writeString(self.player.Name)  # Name
        self.writeString(self.player.FacebookID)  # FacebookID

        self.writeInt(self.player.ExpLevel)   # ExpLevel
        self.writeInt(self.player.ExpPoints)  # ExpPoints
        self.writeInt(self.player.Diamonds)  # Diamonds
        self.writeInt(self.player.FreeDiamonds)  # FreeDiamonds
        self.writeInt(self.player.AttackRating)  # AttackRating
        self.writeInt(self.player.AttackKFactor)  # AttackKFactor
        self.writeInt(self.player.Score)  # Score
        if self.player.Major >= 5: # v5.x.x or above
            self.writeInt(self.player.AttackWinCount)  # AttackWinCount
            self.writeInt(self.player.AttackLoseCount)  # AttackLoseCount
            self.writeInt(self.player.DefenseWinCount)  # DefenseWinCount
            self.writeInt(self.player.DefenseLoseCount)  # DefenseLoseCount
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        
        self.writeByte(self.player.NameSetByUser)  # NameSetByUser

        if self.player.Major >= 5: # v5.x.x or above
            self.writeInt(self.player.CumulativePurchasedDiamonds) # CumulativePurchasedDiamonds

        ##### ARAYS #####

        if self.player.Major >= 5:
            self.writeInt(0)#6) #array 1, resource cap data
            #self.writeInt(3000000)
            #self.writeInt(1000000)
            #self.writeInt(3000001)
            #self.writeInt(2000000000)
            #self.writeInt(3000002)
            #self.writeInt(2000000000)
            #self.writeInt(3000003)
            #self.writeInt(2000000000)
            #self.writeInt(3000007)
            #self.writeInt(2000000000)
            #self.writeInt(3000008)
            #self.writeInt(2000000000)
            
            self.writeInt(3) #array 2, resource data slot data
            # Gold
            self.writeInt(3000001)
            self.writeInt(self.player.Gold)
            # Elixir
            self.writeInt(3000002)
            self.writeInt(self.player.Elixir)
            # Dark Elixir
            self.writeInt(3000003)
            self.writeInt(self.player.DarkElixir)
            
            self.writeInt(0) #array 3, unit slot data
            self.writeInt(0) #array 4, spell slot data
            self.writeInt(0) #array 5, unit upgrade slot
            self.writeInt(0) #array 6, spell upgrade slot
            self.writeInt(0) #array 7, hero upgrade slot
            self.writeInt(0) #array 8, hero health slot
            self.writeInt(0) #array 9, hero state slot
            self.writeInt(0) #array 10, alliance unit data

            if self.player.Major == 5: # v5.x.x
                self.writeInt(0) #array 11, tutorial steps data
            else:
                self.player.TutorialSteps = 10 if self.player.NameSetByUser == 0 else 35
                self.writeInt(self.player.TutorialSteps)  #array 11, tutorial steps data
                for i in range(self.player.TutorialSteps):
                    self.writeInt(21000000 + i)

            self.writeInt(0) #array 12, achievement rewards data
            self.writeInt(0) #array 13, achievement progress data

            self.writeInt(50) #array 14, npc map progress data
            for i in range(17000000, 17000050):
                self.writeInt(i)
                self.writeInt(3)

            self.writeInt(0) #array 15, npc looted gold data
            self.writeInt(0) #array 16, npc looted elixir data
        else:
            self.writeInt(0)
            
            if self.player.Major >= 3: # Run for v3
                self.writeInt(3) #array 2, resource data slot
                # Gold
                self.writeInt(3000001)
                self.writeInt(self.player.Gold)
                # Elixir
                self.writeInt(3000002)
                self.writeInt(self.player.Elixir)
                # Dark Elixir
                self.writeInt(3000003)
                self.writeInt(self.player.DarkElixir)
            else:
                self.writeInt(2) #array 2, resource data slot
                # Gold
                self.writeInt(3000001)
                self.writeInt(self.player.Gold)
                # Elixir
                self.writeInt(3000002)
                self.writeInt(self.player.Elixir)

            self.writeInt(0) #array 3, unit slot data
            self.writeInt(0) #array 4, spell slot data
            self.writeInt(0) #array 5, unit upgrade slot
            self.writeInt(0) #array 6, spell upgrade slot
            self.writeInt(0) #array 7, hero upgrade slot
            self.writeInt(0) #array 8, hero health slot
            self.writeInt(0) #array 9, hero state slot

            if self.player.Major == 4: # v4.x.x
                self.writeInt(0) #array 10, alliance unit data
                self.writeInt(0) #array 11, achievement progress data
                self.writeInt(0) #array 12, npc map progress data
                self.writeInt(0) #array 13, npc looted gold data
                self.writeInt(0) #array 14, npc looted elixir data