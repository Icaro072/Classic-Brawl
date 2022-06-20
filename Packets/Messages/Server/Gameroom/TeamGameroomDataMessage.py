from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.playerCount = 1

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        else:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        DataBase.loadGameroom(self)
        if self.player.room_id != 0:
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(1)
        
            self.writeInt(0)
            self.writeInt(self.player.room_id)

            self.writeVint(1594036200)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            self.writeScId(15, self.mapID)               # MapID

            for player,values in self.playersdata.items():
                # Player
                self.writeVint(self.playerCount)
                self.writeVint(self.playersdata[player]["IsHost"])       # Gameroom owner boolean
                self.writeInt(0)                                      # HighID
                self.writeInt(int(self.playersdata[player]["LowID"]))         # LowID

                self.writeScId(16, self.playersdata[player]["brawlerID"])             # BrawlerID
                self.writeScId(29, self.player.skin_id)
                self.writeVint(brawler_trophies)
                self.writeVint(brawler_trophies_for_rank)
                self.writeVint(brawler_level)

                self.writeVint(3)                                   # Player State | 11: Events, 10: Brawlers, 9: Writing..., 8: Training, 7: Spectactor, 6: Offline, 5: End Combat Screen, 4: Searching, 3: Not Ready, 2: AFK, 1: In Combat, 0: OffLine
                self.writeVint(self.playersdata[player]["Ready"])    # Is ready
                self.writeVint(self.playersdata[player]["Team"])     # Team | 0: Blue, 1: Red
                self.writeVint(0)
                self.writeVint(2)

                self.writeString(self.playersdata[player]["name"])                  # Player name
                self.writeVint(0)
                self.writeVint(28000000 + self.playersdata[player]["profileIcon"])  # Player icon
                self.writeVint(43000000 + self.playersdata[player]["namecolor"])    # Player name color
                self.writeVint(0) #v29
                
                if self.useGadget:
                    self.writeScId(23, self.playersdata[player]["starpower"])       # Starpower
                    self.writeScId(23, self.playersdata[player]["gadget"])          # Gadget
                else:
                    self.writeScId(23, self.playersdata[player]["starpower"])       # Starpower
                    self.writeScId(0, 0)                                            # Gadget

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(6)
        else:
            print(self.player.room_id)
