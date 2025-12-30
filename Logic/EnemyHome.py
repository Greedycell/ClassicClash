import json
from Utils.Writer import Writer


starting_home = json.load(open("Gamefiles/level/starting_home.json", "r"))

class EnemyHome(Writer):

    def encode(self):

        self.writeInt(0)

        if self.player.Major > 6 or (self.player.Major == 6 and self.player.Minor >= 253): # v6.253.x or above
            self.writeInt(1)

        self.writeInt(self.player.HighID)  # HighID
        self.writeInt(self.player.LowID)  # LowID

        self.writeString(json.dumps(starting_home)) # HomeJSON

        self.writeInt(0)  # ShieldDurationSeconds
        self.writeInt(0)  # DefenseRating
        self.writeInt(0)  # DefenseKFactor