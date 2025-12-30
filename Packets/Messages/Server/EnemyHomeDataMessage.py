from Utils.Writer import Writer
from Logic.ClientAvatar import LogicClientAvatar
from Logic.EnemyHome import EnemyHome
from Logic.EnemyAvatar import EnemyAvatar


class EnemyHomeDataMessage(Writer):

    def __init__(self, client, player, enemy):
        super().__init__(client)
        self.device = client
        self.player = player
        self.enemy = enemy
        self.id = 24107

    def encode(self):

        self.writeInt(10)  # SecondsSinceLastSave

        EnemyHome.encode(self)  # LogicClientHome
        EnemyAvatar.encode(self)  # OwnerLogicClientAvatar

        LogicClientAvatar.encode(self)  # AttackerLogicClientAvatar

        self.writeInt(3) 
        self.writeByte(0)