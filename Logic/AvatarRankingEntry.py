import json
from Utils.Writer import Writer

class AvatarRankingEntry(Writer):

    def encode(self):

        self.writeInt(self.player.ExpLevel) # Exp Level
        self.writeInt(self.player.AttackWinCount) # Attack Win Count
        self.writeInt(self.player.AttackLoseCount) # Attack Lose Count
        self.writeInt(self.player.DefenseWinCount) # Defense Win Count
        self.writeInt(self.player.DefenseLoseCount) # Defense Lose Count
        self.writeInt(self.player.LeagueType) # League Type

        self.writeString(self.device.Language) # Country
        self.writeInt(self.player.HighID)  # DefaultHighID
        self.writeInt(self.player.LowID)  # DefaultLowID

        #if (AllianceId > 0)
        #{
        #    var alliance = await Resources.AllianceCache.GetAlliance(AllianceId)

        #    if (alliance != null)
        #    {
        #        stream.WriteBool(true)
        #        self.writeLong(AllianceId) # Clan Id
        #        self.writeString(alliance.Name) # Clan Name
        #        self.writeInt(alliance.Badge) # Badge
        #    }
        #    else
        #    {
        #        AllianceId = 0
        #        stream.WriteBool(false)
        #    }
        #}
        #else
        #{
        self.writeByte(0) # 0=False, 1=True
        #}