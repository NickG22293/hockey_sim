# Parent class to hold apropo stats for playoff/regular season
class SeasonStats:
    def __init__(self):
        self.shots = 0      ## Total shots season
        self.shotspg = 0    ## Shots per game
        self.shotperc = 0   ## Shot % across team
        self.svperc = 0     ## Save % across goalies
        self.record = 0     ## Total record

# Regular season stats
class RegularSeasonStats(SeasonStats):
    def __init__(self):
        SeasonStats.__init__(self)

# Post season stats
class PostSeasonStats(SeasonStats):
    def __init__(self):
        SeasonStats.__init__(self)
        self.seed = 0           #Seed coming into playoffs
        self.playoff_gp = 0;    #Playoffs games played
