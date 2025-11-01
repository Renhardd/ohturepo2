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
        self.stats = StatisticsService(
            PlayerReaderStub()
            )
        
    def test_loytyyko_pelaajat(self):
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")
        
        pelaaja = self.stats.search("asd")
        self.assertEqual(pelaaja, None)
        
    def test_tiimit(self):
        tiimi = self.stats.team("EDM")
        tiimihaettu = [pelaaja.name for pelaaja in tiimi]
        tiimin_nimet = ["Semenko", "Kurri", "Gretzky"]
        self.assertEqual(tiimihaettu, tiimin_nimet)
        
    def test_kovimmat_pisteet(self):
        kovin_tekiija = self.stats.top(1)
        self.assertEqual(kovin_tekiija[0].points, 124)


        
    