import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_search_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 35)
        self.assertEqual(player.assists, 89)

    def test_team_returns_players(self):
        players = self.stats.team("EDM")
        
        self.assertEqual(len(players), 3)
        for player in players:
            self.assertEqual(player.team, "EDM")
        
    def test_top(self):
        players = self.stats.top(3)
        
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")


