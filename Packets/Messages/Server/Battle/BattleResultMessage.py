from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        # Stuff
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        else:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        # Rewards
        if self.player.tutorial <= 1:
            exp_reward = [0, 0, 0]
            token_list = [0, 0, 0]
            practice_exp_reward = [0, 0, 0] 
            practice_token_list = [0, 0, 0]
            mvp_exp_reward = [0, 0]
        else:
            exp_reward = [8, 6, 4]
            token_list = [20, 15, 10]
            practice_exp_reward = [4, 3, 2]
            practice_token_list = [10, 8, 5]
            mvp_exp_reward = [10]
        # Trophy Balance
        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0
        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1
            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2
            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3
            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4
            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5
            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6
            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7
            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8
            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9
            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10
            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11
            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12
            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12
        # Result Rewards
        if self.player.battle_tokens <= 0 and self.player.collected_experience >= 1000:
            result = self.player.result + 6
        elif self.player.battle_tokens <= 0:
            result = self.player.result + 4
        elif self.player.collected_experience >= 1000:
            result = self.player.result + 2
        else:
            result = self.player.result
        if self.player.result == 0:
            gainedtrophies = 0
            if self.player.battle_result == 0:
                gainedtokens = practice_token_list[0]
                gainedexperience = practice_exp_reward[0]
                self.player.ThreeVSThree_wins += 1
                DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            if self.player.battle_result == 1:
                gainedtokens = practice_token_list[2]
                gainedexperience = practice_exp_reward[2]
            if self.player.battle_result == 2:
                gainedtokens = practice_token_list[1]
                gainedexperience = practice_exp_reward[1]
        else:
            if self.player.battle_result == 0:
                gainedtokens = token_list[0]
                gainedexperience = exp_reward[0]
                gainedtrophies = win_val
                self.player.ThreeVSThree_wins += 1
                DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            if self.player.battle_result == 1:
                gainedtokens = token_list[2]
                gainedexperience = exp_reward[2]
                gainedtrophies = lose_val
            if self.player.battle_result == 2:
                gainedtokens = token_list[1]
                gainedexperience = exp_reward[1]
                gainedtrophies = 0
                
        if self.player.battle_result in [0, 2]:
            if 0 <= result <= 15:
                starplayer = 1
            else:
                starplayer = 5
        else:
             if 0 <= result <= 15:
                starplayer = 1
             else:
                starplayer = 1
        # Star Player Info
        if starplayer == 5:
            starplayerexperience = mvp_exp_reward[0]
        else:
            starplayerexperience = 0
        # Results Balance
        if result in [0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27]:
            tokens = gainedtokens
        if result in [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]:
            tokens = 0
        if result in [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29]:
            mvpexperience = starplayerexperience
            experience = gainedexperience
        if result in [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]:
            mvpexperience = 0
            experience = 0
        if 0 <= result <= 31:
            trophies = gainedtrophies
            startoken = 0
        # DataBase Stuff            
        self.player.player_experience += experience + mvpexperience
        self.player.collected_experience += experience + mvpexperience
        if self.player.battle_tokens <= 0:
            token = 0
        if self.player.battle_tokens > tokens:
            token = tokens
        if tokens >= self.player.battle_tokens: 
            token = self.player.battle_tokens
        if self.player.tokenevent == 'true':
            tokenevent = token
        else:
            tokenevent = 0
        if self.player.tokensdoubler <= 0:
            doubledtokens = 0
        if self.player.tokensdoubler > token + tokenevent:
            doubledtokens = token + tokenevent
        if token + tokenevent >= self.player.tokensdoubler: 
            doubledtokens = self.player.tokensdoubler
        battle_tokens = self.player.battle_tokens - token
        remainingtokens = (self.player.tokensdoubler) - doubledtokens
        totaltokens = token + tokenevent + doubledtokens
        if self.player.coinevent == 'true':
            coinevent = totaltokens
        else:
            coinevent = 0
        new_gold = self.player.gold + coinevent
        new_trophies = self.player.trophies + trophies
        new_tokens = self.player.brawl_boxes + totaltokens
        new_startokens = self.player.big_boxes + startoken
        self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
        if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
            self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank - brawler_trophies_for_rank + brawler_trophies + trophies
        if self.player.tutorial <= 1:
            pass
        else:
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'availableTokens', battle_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, 'cappedExp', self.player.collected_experience)
            DataBase.replaceValue(self, 'gold', new_gold)
        
        self.writeVint(1) # Battle End Game Mode 
        self.writeVint(self.player.battle_result) # Result 
        self.writeVint(token) # Tokens Gained
        if self.player.result < 16:
            self.writeVint(0) # Trophies Result 
        if self.player.result >= 16:
            if gainedtrophies >= 0:
                self.writeVint(gainedtrophies) # Trophies Result
            if gainedtrophies < 0:
                self.writeVint(-65 - (gainedtrophies)) # Trophies Result
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(tokenevent) # Double Token Event
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time
        self.writeVint(0) # Unknown (Championship Related)
        self.writeVint(0) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVint(0) # Challenge Reward Ammount
        self.writeVint(0) # Championship Losses Left
        self.writeVint(0) # Championship Maximun Losses
        self.writeVint(coinevent) # Coin Shower Event
        self.writeVint(0) # Underdog Trophies
        if self.player.tutorial <= 1:
            self.writeVint(32) # Battle Result Type
        else:
            self.writeVint(result) # Battle Result Type
        self.writeVint(-64) # Championship Challenge Type
        self.writeVint(0) # Championship Cleared and Beta Quests
            
        # Players Array
        self.writeVint(self.player.players) # Battle End Screen Players
        
        self.writeVint(starplayer) # Team and Star Player Type
        self.writeScId(16, self.player.brawler_id) # Player Brawler
        self.writeScId(29, self.player.skin_id) # Player Skin
        self.writeVint(brawler_trophies) # Your Brawler Trophies
        self.writeVint(0) # Your Power Play Points
        self.writeVint(brawler_level) # Your Brawler Power Level
        self.writeBoolean(True) # HighID and LowID Array
        self.writeInt(self.player.high_id) # HighID
        self.writeInt(self.player.low_id) # LowID
        self.writeString(self.player.name) # Your Name
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Player Experience Level
        self.writeVint(28000000 + self.player.profile_icon) # Player Profile Icon
        self.writeVint(43000000 + self.player.name_color) # Player Name Color
        self.writeVint(0) # Unknown
            
        if self.player.team == 0:
            if self.player.bot1_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot1_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot1) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Power Play Points
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString(self.player.bot1_n) # Bot 1 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(0) # Unknown
            
        if self.player.team == 0:
            if self.player.bot2_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot2_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot2) # Bot 2 Brawler
        self.writeVint(0) # Bot 2 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Power Play Points
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString(self.player.bot2_n) # Bot 2 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(0) # Unknown

        if self.player.team == 0:
            if self.player.bot3_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot3_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot3) # Bot 3 Brawler
        self.writeVint(0) # Bot 3 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Power Play Points
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString(self.player.bot3_n) # Bot 3 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(0) # Unknown

        if self.player.team == 0:
            if self.player.bot4_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot4_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot4) # Bot 4 Brawler
        self.writeVint(0) # Bot 4 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Power Play Points
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString(self.player.bot4_n) # Bot 4 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(0) # Unknown

        if self.player.team == 0:
            if self.player.bot5_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot5_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot5) # Bot 5 Brawler
        self.writeVint(0) # Bot 5 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Power Play Points
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString(self.player.bot5_n) # Bot 5 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(0) # Unknown
        
        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Gained
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(mvpexperience) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Trophies Bar Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Player Experience
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Player Experience for Level
        
        self.writeScId(28, self.player.profile_icon)  # Player Profile Icon (Unused since 2017)
        if 16 <= result <= 23:
            self.writeBoolean(True) # Play Again
        else:
            self.writeBoolean(False)  # Play Again
            
        if self.player.battle_result == 0:
            if self.player.tutorial <= 1:
                self.player.tutorial += 1
                DataBase.replaceValue(self, 'tutorial', self.player.tutorial)
                self.player.ThreeVSThree_wins -= 1
                DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            else: 
                self.player.tutorial = 0
      