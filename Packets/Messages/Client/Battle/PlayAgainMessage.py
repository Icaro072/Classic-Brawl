from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Battle.PlayAgainStatusMessage import PlayAgainStatusMessage
from Packets.Messages.Server.Battle.PlayAgainBattleTestMessage import PlayAgainBattleTestMessage
from Packets.Messages.Server.Battle.BattleTestMessage import BattleTestMessage

from Utils.Reader import BSMessageReader


class PlayAgainMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        PlayAgainBattleTestMessage(self.client, self.player, 0).send()
        PlayAgainStatusMessage(self.client, self.player).send()
        BattleTestMessage(self.client, self.player, 0).send()