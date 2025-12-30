from random import choice
from string import ascii_uppercase
import json
import time
import random
from Utils.Reader import Reader
from Logic.Player import Player
from Utils.Helpers import Helpers
from Database.DataBase import DataBase
from Packets.Messages.Server.LoginOkMessage import *
from Packets.Messages.Server.LoginFailedMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *
from Packets.Messages.Server.Avatar.AvatarStreamMessage import *


class LoginMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.HighID = self.readInt()
        self.LowID = self.readInt()
        self.Token = self.readString()
        self.Major = self.readInt()
        self.Minor = self.readInt()
        self.Build = self.readInt()

    def process(self):
        print('Player: Id: ', self.HighID, ",", self.LowID, " Token: ", self.Token)
        print('Client Version: ', self.Major, ".", self.Minor, ".", self.Build)

        self.player.HighID = self.HighID
        self.player.LowID = self.LowID
        self.player.Token = self.Token
        self.player.Major = self.Major
        self.player.Minor = self.Minor
        self.player.Build = self.Build

        #LoginFailedMessage(self.client, self.player, 10, '', '').Send()

        if len(self.player.Token) == 40:
            DataBase.loadAccount(self)
            LoginOkMessage(self.client, self.player).Send()
            OwnHomeDataMessage(self.client, self.player).Send()
            if self.player.Major >= 5: # v5.x.x or above
                AvatarStreamMessage(self.client, self.player).Send()
        else:
            self.player.HighID = random.randint(0, 3)
            self.player.LowID = random.randint(0, 2147483647)
            self.player.Token = Helpers.randomStringDigits(self)
            DataBase.createAccount(self)
            LoginOkMessage(self.client, self.player).Send()
            OwnHomeDataMessage(self.client, self.player).Send()
            if self.player.Major >= 5: # v5.x.x or above
                AvatarStreamMessage(self.client, self.player).Send()