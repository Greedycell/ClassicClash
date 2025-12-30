from Utils.Reader import Reader
from Logic.Player import Player
from Database.DataBase import DataBase
from Packets.Messages.Server.AvailableServerCommandMessage import *
from Packets.Messages.Server.AvatarNameChangeFailedMessage import *


class ChangeAvatarNameMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):

        self.Name = self.readString()  # Name

    def process(self):
        if 3 <= len(self.Name) <= 15:
            print("Changed named to: ", self.Name)
            self.player.Name = self.Name
            self.player.Gold += 1000
            self.player.TutorialSteps = 13
            self.player.ExpLevel = 10
            self.player.NameSetByUser = 1

            DataBase.replaceValue(self, 'nameSetByUser', self.player.NameSetByUser)
            DataBase.replaceValue(self, 'name', self.Name)

            AvailableServerCommandMessage(self.client, 3, self.Name).Send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).Send()