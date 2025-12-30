from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.AllianceJoinOkMessage import *


class CreateAllianceMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):

        self.AllianceName = self.readString() # AllianceName
        self.AllianceDesc = self.readString() # AllianceDesc
        self.AllianceBadge = self.readInt()   # AllianceBadge
        self.AllianceType = self.readInt()    # AllianceType
        self.RequiredScore = self.readInt()   # RequiredScore
        self.WarFrequency = self.readInt()    # WarFrequency
        self.AllianceOrigin = self.readInt()  # AllianceOrigin

    def process(self):
        AllianceJoinOkMessage(self.client, self.player).Send()