import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

class LoginOkMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(self.player.HighID)  # AccountHighID
        self.writeInt(self.player.LowID)  # AccountLowID
        self.writeInt(self.player.HighID)  # HomeHighID
        self.writeInt(self.player.LowID)  # HomeLowID

        if not self.player.Token:
            self.writeString('')  # PassToken
        else:
            self.writeString(self.player.Token)  # PassToken

        self.writeString(self.player.FacebookID)  # FacebookID
        self.writeString(self.player.GameCenterID)  # GameCenterID

        self.writeInt(self.player.Major)  # MajorVersion
        self.writeInt(self.player.Build)  # BuildVersion
        self.writeInt(self.player.Minor)  # ContentVersion

        if self.player.Major >= 5: # v5.x.x or above
            self.writeString(config['ServerEnvironment'])  # ServerEnvironment
        else:
            self.writeString('dev')  # ServerEnvironment

        self.writeInt(self.player.SessionCount)  # SessionCount
        self.writeInt(self.player.PlayTimeSeconds)  # PlayTimeSeconds
        self.writeInt(self.player.DaysSinceStartedPlaying)  # DaysSinceStartedPlaying

        if self.player.Major != 13:
            self.writeString(self.player.FacebookAppId)  # FacebookAppId

            if self.player.Major >= 4: # v4.x.x or above
                self.writeString(self.player.ServerTime)  # ServerTime
                self.writeString(self.player.AccountCreatedDate)  # AccountCreatedDate
                self.writeInt(self.player.StartupCooldownSeconds)  # StartupCooldownSeconds

                self.writeString(self.player.GoogleServiceId)  # GoogleServiceId
                self.writeString(self.player.Region)  # Region

                self.writeString(None)  # ???
                self.writeInt(1)  # ???
                self.writeString(None)  # ???
                self.writeString(None)  # ???
                self.writeString(None)  # ???
                
                self.writeString(None)  # m_contentUrlList
                
                self.writeString(None)  # m_chronosContentUrlList