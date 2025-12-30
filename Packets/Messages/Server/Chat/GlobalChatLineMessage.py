import json
from Utils.Writer import Writer
from Packets.Messages.Client.SendGlobalChatLineMessage import *




class GlobalChatLineMessage(Writer):

    def __init__(self, device, player, message):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 24715
        self.message = message

    def encode(self):

        self.writeString(self.message)  # Message
        self.writeString(self.player.Name)  # AvatarName

        self.writeInt(1)  # AvatarExpLevel

        self.writeInt(0)
        self.writeInt(1)

        self.writeInt(0)
        self.writeInt(1)

        self.writeByte(1)  # IsInAlliance

        self.writeInt(0)
        self.writeInt(1)

        self.writeString('Clashers')

        self.writeInt(13000000)