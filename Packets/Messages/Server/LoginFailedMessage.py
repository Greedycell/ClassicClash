import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

class LoginFailedMessage(Writer):

    def __init__(self, device, player, errorCode, Reason, Fingerprint):
        super().__init__(device)
        self.device = device
        self.player = player
        self.errorCode = errorCode
        self.Reason = Reason
        self.Fingerprint = Fingerprint
        self.id = 20103
        self.version = 1

    # Codes:
    # 7 = Content Update
    # 8 = Update Available
    # 10 = Maintenance
    # 11 = Banned
    # 12 = Played too long

    def encode(self):
        self.writeInt(self.errorCode) # Error Code
        self.writeString(self.Fingerprint) # Fingerprint
        self.writeString(None)
        self.writeString(config['ContentURL']) # Content Update URL
        self.writeString(None) # Update URL
        self.writeString(self.Reason) # Reason