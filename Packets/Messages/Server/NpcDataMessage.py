import json
from Utils.Writer import Writer
from Logic.ClientAvatar import LogicClientAvatar


npcLevel = json.load(open("Gamefiles/level/starting_home.json", "r"))


class NpcDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24133

    def encode(self):

        self.writeInt(0)  # SecondsSinceLastSave

        self.writeString(json.dumps(npcLevel)) # NPCJSON

        LogicClientAvatar.encode(self)

        self.writeInt(0)  # NpcHighID
        self.writeInt(1)  # NpcLowID