import json
from Utils.Writer import Writer

class AllianceRankingEntry(Writer):

    def encode(self):

        self.writeInt(13000000) # Badge
        self.writeInt(1) # Member Count