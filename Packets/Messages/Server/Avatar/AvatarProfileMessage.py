import json
from Utils.Writer import Writer
from Logic.AvatarProfile import AvatarProfile




class AvatarProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24334
    
    def  encode(self):

        pass

        AvatarProfile.encode(self)

        self.writeInt(0)  # Donations
        self.writeInt(0)  # DonationsReceived