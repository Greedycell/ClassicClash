from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.OwnHomeDataMessage import *
from Packets.Messages.Server.Avatar.AvatarStreamMessage import *


class GoHomeMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self):
        OwnHomeDataMessage(self.client, self.player).Send()
        AvatarStreamMessage(self.client, self.player).Send()