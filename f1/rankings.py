import csv
from collections import OrderedDict


class ChampionshipRankings:

    def __init__(self):
        with open('datasets/champions_by_season.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            self.dataset = list(reader)

        self.list_of_champions = [r['champion'] for r in self.dataset]

    def score_by_runnerup_titles(self) -> OrderedDict:
        """
        Season champion score must be equals to the number of titles of the runner up
        """
        resultset = {}
        for season in self.dataset:
            champion = season['champion']
            resultset.setdefault(champion, 0)
            resultset[champion] += self.list_of_champions.count(season['runner'])

        return OrderedDict(sorted(resultset.items(), key=lambda x: x[1], reverse=True))
