from Utils.Writer import Writer


class LogicJoinAllianceCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 1

    def encode(self):

        self.writeInt(0)
        self.writeInt(1)

        self.writeString()

        self.writeInt()

        self.writeByte()
