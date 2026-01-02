import json
import string
import random
from tinydb import TinyDB, Query
from Utils.Helpers import Helpers

class DataBase:

    def loadAccount(self):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.Token))
        if user_data:
            self.player.HighID = user_data[0]["info"]["highID"]
            self.player.LowID = user_data[0]["info"]["lowID"]
            self.player.Name = user_data[0]["info"]["name"]
            self.player.Token = user_data[0]["info"]["token"]
            self.player.HomeVillage = user_data[0]["info"]["homeVillage"]
            self.player.TutorialSteps = user_data[0]["info"]["tutorialSteps"]
            self.player.ExpLevel = user_data[0]["info"]["expLevel"]
            self.player.ExpPoints = user_data[0]["info"]["expPoints"]
            self.player.NameSetByUser = user_data[0]["info"]["nameSetByUser"]
            self.player.IsInAlliance = user_data[0]["info"]["isInAlliance"]
            self.player.AllianceLowID = user_data[0]["info"]["allianceLowID"]
            self.player.AllianceRole = user_data[0]["info"]["allianceRole"]
            self.player.Gold = user_data[0]["info"]["gold"]
            self.player.Elixir = user_data[0]["info"]["elixir"]
            self.player.Diamonds = user_data[0]["info"]["diamonds"]
            self.player.Score = user_data[0]["info"]["score"]
            self.player.LeagueType = user_data[0]["info"]["leagueType"]

    def createAccount(self):

        db = TinyDB('Database/Player/data.db')

        data = {
            "info":
            {
                "highID": self.player.HighID,
                "lowID": self.player.LowID,
                "name": self.player.Name,
                "token": str(self.player.Token),  
                "homeVillage": self.player.HomeVillage,
                "tutorialSteps": self.player.TutorialSteps,
                "isInAlliance": self.player.IsInAlliance,
                "allianceHighID": self.player.AllianceHighID,
                "allianceLowID": self.player.AllianceLowID,
                "allianceRole": self.player.AllianceRole,
                "gold": self.player.Gold,
                "elixir": self.player.Elixir,
                "diamonds": self.player.Diamonds,
                "expLevel": self.player.ExpLevel,
                "expPoints": self.player.ExpPoints,
                "nameSetByUser": self.player.NameSetByUser,
                "score": self.player.Score,
                "leagueType": self.player.LeagueType
            }

        }

        db.insert(data)

    def replaceValue(self, value_name, new_value):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        print(self.player.Token)
        data = db.search(query.token == str(self.player.Token))
        user_data = data[0]
        user_data["info"][str(value_name)] = new_value
        db.update(user_data, query.token == str(self.player.Token))

    def createAlliance(self, allianceid):
        alliancedb = TinyDB('Database/Alliance/alliance.db')
        chatdb = TinyDB('Database/Alliance/chat.db')

        data = {
            "allianceID": allianceid,
            "info": {
                "name": self.allianceName,
                "description": self.alliancedescription,
                "region": "IL",
                "badgeID": self.alliancebadgeID,
                "type": self.alliancetype,
                "trophiesneeded": self.alliancetrophiesneeded,
                "trophies": self.player.trophies,
                "members": {
                    "totalmembers": 1,
                    str(self.player.LowID): self.player.name
                }
            }
        }
        alliancedb.insert(data)
        if False:
            msgData = {
                allianceid: {
                    "Total": 1,
                    "1": {
                        "Event": 2,
                        "Tick": 1,
                        "PlayerID": self.player.low_id,
                        "PlayerName": self.player.name,
                        "PlayerRole": 2,
                        "Message": "Welcome to your new alliance!"
                    }
                }
            }

    def CountAlliance(self, minMembers, maxMembers, allianceType, maxListLength):
        db = TinyDB('Database/Alliance/alliance.db')
        query = Query()
        alliance_list = []

        for alliance in db.all():
            alliance_id = alliance['allianceID']
            allianceInfo = db.search(query.allianceid == alliance_id)[0]['info']
            print(allianceInfo)
            # if info["members"]["totalmembers"] >= minMembers and info["members"]["totalmembers"] < maxMembers and info["type"] <= allianceType and self.AllianceCount <= maxListLength:

    def loadAlliance(self, allianceid):
        db = TinyDB('Database/Alliance/alliance.db')
        query = Query()
        data = db.search(query.allianceID == self.player.AllianceID)
        alliance_data = data[0]
        self.plrids = []
        self.allianceName = alliance_data["info"]["name"]
        self.alliancedescription = alliance_data["info"]["description"]
        self.allianceregion = alliance_data["info"]["region"]
        self.alliancebadgeID = alliance_data["info"]["badgeID"]
        self.alliancetype = alliance_data["info"]["type"]
        self.alliancetrophiesneeded = alliance_data["info"]["trophiesneeded"]
        self.alliancetrophies = alliance_data["info"]["trophies"]
        self.alliancemembercount = alliance_data["info"]["members"]["totalmembers"]
        for plridentifier, data in alliance_data["info"]["members"].items():
            if plridentifier != "totalmembers":
                self.plrids.append(int(plridentifier))

    def GetMemberData(self, allianceID):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        member_list = []

        for i in db.all():
            token = i['token']
            member = db.search(query.token == str(token))[0]['info']
            if member['allianceLowID'] == allianceID:
                member_list.append(member)
        return member_list

    def replaceAllianceValue(self, target, inf1, inf2, inf3, inf4):
        db = TinyDB('Database/Alliance/alliance.db')
        query = Query()
        data = db.search(query.allianceID == target)
        print(data, target)
        alliance_data = data[0]

        alliance_data["info"]["description"] = inf1
        alliance_data["info"]["badgeID"] = inf2
        alliance_data["info"]["type"] = inf3
        alliance_data["info"]["trophiesneeded"] = inf4


        db.update(alliance_data, query.allianceID == target)
