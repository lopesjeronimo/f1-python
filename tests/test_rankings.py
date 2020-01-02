import unittest
from f1.rankings import ChampionshipRankings


class ChampionshipRankingsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ranking = ChampionshipRankings()

    def test_score_by_runnerup_titles(self):
        scores = self.ranking.score_by_runnerup_titles()
        self.assertEqual(scores['Ayrton Senna'], 9)
        self.assertEqual(scores['Kimi Raikkonen'], 6)
        self.assertEqual(scores['Jacques Villeneuve'], 0)

    def test_score_by_runnerup_titles_at_that_time(self):
        scores = self.ranking.score_by_runnerup_titles_at_that_time()
        self.assertEqual(scores['Ayrton Senna'], 5)
        self.assertEqual(scores['Michael Schumacher'], 2)
        self.assertEqual(scores['Kimi Raikkonen'], 0)


if __name__ == '__main__':
    unittest.main()
