from Packets.Messages.Client.ClientHelloMessage import *
from Packets.Messages.Client.LoginMessage import *
from Packets.Messages.Client.KeepAliveMessage import *
from Packets.Messages.Client.ChangeAvatarNameMessage import *
from Packets.Messages.Client.ReportUserMessage import *
from Packets.Messages.Client.GoHomeMessage import *
from Packets.Messages.Client.EndClientTurnMessage import *
from Packets.Messages.Client.SearchAlliancesMessage import *
from Packets.Messages.Client.CreateAllianceMessage import *
from Packets.Messages.Client.ChangeAllianceSettingsMessage import *
from Packets.Messages.Client.InviteToClanMessage import *
from Packets.Messages.Client.ChatToAllianceStreamMessage import *
from Packets.Messages.Client.AskForAllianceDataMessage import *
from Packets.Messages.Client.AskForJoinableAlliancesListMessage import *
from Packets.Messages.Client.AskForAllianceUnitDonationsMessage import *
from Packets.Messages.Client.AskForAvatarProfileMessage import *
from Packets.Messages.Client.VisitHomeMessage import *
from Packets.Messages.Client.AttackNpcMessage import *
from Packets.Messages.Client.JoinAllianceMessage import *
from Packets.Messages.Client.AskForAllianceRankingListMessage import *
from Packets.Messages.Client.AskForAvatarRankingListMessage import *
from Packets.Messages.Client.AskForAvatarLocalRankingListMessage import *
from Packets.Messages.Client.SendGlobalChatLineMessage import *

from Packets.Messages.Client.CloseClientSocket import *

availablePackets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10117: CloseClientSocket, # WIP: AttackNpcMessage
    10212: ChangeAvatarNameMessage,
    14101: GoHomeMessage,
    14102: EndClientTurnMessage,
    14134: CloseClientSocket, # WIP: AttackNpcMessage
    14301: CloseClientSocket, # WIP: CreateAllianceMessage
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14305: CloseClientSocket, # WIP: JoinAllianceMessage
    14309: CloseClientSocket, # WIP: AskForAllianceUnitDonationsMessage
    14113: CloseClientSocket, # WIP: GoHomeMessage
    14315: CloseClientSocket, # WIP: ChatToAllianceStreamMessage
    14316: CloseClientSocket, # WIP: ChangeAllianceSettingsMessage
    14322: CloseClientSocket, # WIP: InviteToClanMessage
    14324: CloseClientSocket, # WIP: SearchAlliancesMessage
    14325: AskForAvatarProfileMessage,
    14401: AskForAllianceRankingListMessage,
    14403: AskForAvatarRankingListMessage,
    14404: AskForAvatarLocalRankingListMessage,
    14715: SendGlobalChatLineMessage,
}