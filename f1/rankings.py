import csv
from collections import OrderedDict, defaultdict


class ChampionshipRankings:

    def __init__(self):
        with open('datasets/champions_by_season.csv') as csvfile:
            self.dataset = list(csv.DictReader(csvfile))

    def score_by_runnerup_titles(self) -> OrderedDict:
        """
        Season champion score must be equals to the number of titles of the runner up
        """
        resultset = defaultdict(int)
        list_of_champions = [r['champion'] for r in self.dataset]
        for season in self.dataset:
            champion = season['champion']
            resultset[champion] += list_of_champions.count(season['runner'])

        return OrderedDict(sorted(resultset.items(), key=lambda x: x[1], reverse=True))

    def score_by_runnerup_titles_at_that_time(self) -> OrderedDict:
        """
         Season champion score must be equals to the number of titles the runner up holds on that year
        """
        titles_by_driver = defaultdict(int)
        resultset = defaultdict(int)
        for season in self.dataset:
            champion = season['champion']
            titles_by_driver[champion] += 1
            resultset[champion] += titles_by_driver.get(season['runner'], 0)

        return OrderedDict(sorted(resultset.items(), key=lambda x: x[1], reverse=True))
