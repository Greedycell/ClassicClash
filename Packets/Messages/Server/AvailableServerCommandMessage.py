from Utils.Writer import Writer
from Logic.Player import Player
from Packets.Commands.Server.LogicJoinAllianceCommand import *
from Packets.Commands.Server.LogicLeaveAllianceCommand import *
from Packets.Commands.Server.LogicChangeAvatarNameCommand import *
from Packets.Commands.Server.LogicDonateAllianceUnitCommand import *
from Packets.Commands.Server.LogicAllianceUnitReceivedCommand import *
from Packets.Commands.Server.LogicAllianceSettingsChangedCommand import *
from Packets.Commands.Server.LogicDiamondsAddedCommand import *
from Packets.Commands.Server.LogicChangeAllianceRoleCommand import *
from Packets.Commands.Client.LogicMatchmakingCommand import *


class AvailableServerCommandMessage(Writer):

    def __init__(self, device, ID, arg1):
        super().__init__(device)
        self.device = device
        self.player = Player(device)
        self.commandID = ID
        self.arg1 = arg1
        self.id = 24111

    def encode(self):

        if self.commandID == 0:
            return

        commands = {
            1: LogicJoinAllianceCommand,
            2: LogicLeaveAllianceCommand,
            3: LogicChangeAvatarNameCommand,
            4: LogicDonateAllianceUnitCommand,
            5: LogicAllianceUnitReceivedCommand,
            6: LogicAllianceSettingsChangedCommand,
            7: LogicDiamondsAddedCommand,
            8: LogicChangeAllianceRoleCommand,
            #700: LogicMatchmakingCommand
        }

        if self.commandID in commands:
            self.writeInt(self.commandID)

            commands[self.commandID].encode(self)

            print(f'[SERVER] Handled command ID: {self.commandID}')
        else:
            print(f"[SERVER] Unhandled command ID: {self.commandID}")