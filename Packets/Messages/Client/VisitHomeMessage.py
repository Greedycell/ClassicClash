from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.VisitedHomeDataMessage import *


class VisitHomeMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.readInt()  # HighID
        self.readInt()  # LowID

    def process(self):
        VisitedHomeDataMessage(self.device, self.player).Send()