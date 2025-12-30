import json
import time

from Utils.Reader import Reader
from Logic.Player import Player

from Packets.Messages.Server.Avatar.AvatarStreamEntryMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *

config = json.load(open("config.json", "r+"))

class ChatToAllianceStreamMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        global Message
        Message = self.readString()  # Message

    def process(self):
        AvatarStreamEntryMessage(self.device, self.player).Send()
        print(Message)
        time.sleep(1)