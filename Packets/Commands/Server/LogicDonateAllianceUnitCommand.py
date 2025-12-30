from Utils.Writer import Writer


class LogicDonateAllianceUnitCommand(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 4

    def encode(self):
        pass