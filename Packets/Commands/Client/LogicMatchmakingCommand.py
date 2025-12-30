from Utils.Writer import Writer
from Logic.Player import Player
from Packets.Messages.Server.EnemyHomeDataMessage import *


class LogicMatchmakingCommand(Writer):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def encode(self):
        self.enemy = self.player # TODO: Enemies
        EnemyHomeDataMessage(self.device, self.player, self.enemy).Send()

        # TODO: Remove Shield

        if self.player.State == 'Battle': # TODO: SetDefender
            pass