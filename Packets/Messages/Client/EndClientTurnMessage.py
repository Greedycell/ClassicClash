from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommandMessage import *


class EndClientTurnMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.subTick = self.readInt()  # SubTick
        self.Checksum = self.readInt()  # Checksum
        self.CommandsCount = self.readInt()  # CommandsCount
        self.Type = self.readInt()
        #if self.Type != 0: 
        #    print(f"[ENDCLIENTTURNMESSAGE] Subtick: {self.subTick}, Checksum: {self.Checksum}, "
        #          f"CommandsCount: {self.CommandsCount}, Type: {self.Type}")


    def process(self):
        pass
        #AvailableServerCommandMessage(self.device, self.Type).Send()