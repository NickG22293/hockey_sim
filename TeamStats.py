from lxml import html, etree
import requests
import SeasonStats

# Stats class to hold all relevant stats for the prediction for a single team
# To be used in tandem with other TeamStats with the HockeySim methods
class TeamStats:
    def __init__(self):
        self.team = ""
        self.playoff_stats = PostSeasonStats()
        self.regular_stats = RegularSeasonStats()

    # Just print out appropriate stats
    def print_team_stats(self,stats):
        print "Shots: ", stats.shots
        print "Shot %: ", stats.shotperc
        print "Record: ", stats.record
        print "Save %: ", stats.svperc
        print "Shots PG: ", stats.shotspg
        if stats.__class__ == PostSeasonStats:
            print "Seed: ", stats.seed
            print "Playoff GP: ", stats.playoff_gp

    # Cols as follows:
    # AvAge, GP, W, L, OL, PTS, PTS%, GF, GA, SRS, SOS
    # TG/G, PPG, PPO, PP% PPA, PPO, PK%, SHG, SHA, S, S%
    SHOTS_COL = 21
    SHOTPERC_COL = 22
    SVPERC_COL = 24
    def fill_team_stats(self, table):
        # fill the regular season stats
        self.regular_stats.shots = table[self.SHOTS_COL]
        self.regular.shotspg = self.shots / 82
        self.regular.shotperc = table[self.SHOTPERC_COL]
        self.regular.svperc = table[self.SVPERC_COL]
        self.print_team_stats(self.regular_stats)

    # pull down info from stats site using lxml and requests
    def parse_hockey_stats(self, team):
        # build the URL using Team
        url = "http://www.hockey-reference.com/teams/" + team + "/2016.html"
        page = requests.get(url)
        # content is put in a nice tree format for xpath parsing
        tree = html.fromstring(page.content)
        # Xpath query for team's stats
        stats = tree.xpath('//table[@id="team_stats"]/tbody/*')
        assert isinstance(stats, object)
        # fill stats vars
        table = iter(stats)
        assert isinstance(table, object)
        self.fill_team_stats(table)
