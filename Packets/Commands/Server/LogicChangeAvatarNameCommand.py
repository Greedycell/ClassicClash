from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, client):
        super().__init__(client)
        self.device = client
        self.player = Player(device)
        self.commandID = 3

    def encode(self):

        self.writeString(self.arg1)

        print(self.arg1)