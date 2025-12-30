import json
from Utils.Writer import Writer


starting_home = json.load(open("Gamefiles/level/starting_home.json", "r"))
starting_home_beta = json.load(open("Gamefiles/level/starting_home_beta.json", "r"))

class LogicClientHome(Writer):

    def encode(self):

        self.writeInt(0) # NPC Timestamp

        if self.player.Major > 6 or (self.player.Major == 6 and self.player.Minor >= 253): # v6.253.x or above
            self.writeInt(0)

        self.writeInt(self.player.HighID)  # HighID
        self.writeInt(self.player.LowID)  # LowID

        if self.player.Major > 5: # Global Release
            if not self.player.HomeVillage:
                self.player.HomeVillage = json.dumps(starting_home)
                self.writeString(self.player.HomeVillage) # HomeJSON
            else:
                self.writeString(self.player.HomeVillage) # HomeJSON
        else: # Beta Release
            if not self.player.HomeVillage:
                self.player.HomeVillage = json.dumps(starting_home_beta)
                self.writeString(self.player.HomeVillage) # HomeJSON
            else:
                self.writeString(self.player.HomeVillage) # HomeJSON

        self.writeInt(0)  # ShieldDurationSeconds
        self.writeInt(0)  # DefenseRating
        self.writeInt(0)  # DefenseKFactor