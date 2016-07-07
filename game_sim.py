#!/usr/bin/env python

# This file is intended to be the tools needed for the simulation of one game.
# Info is gathered from hockey-reference.com using web scraping to parse out
# relevant info from their static HTML pages.
# This is designed to be used in a large capacity for high-volume series simulations
# so optimization will have to be kept in mind.

import SeasonStats
import TeamStats

class HockeySim:
    def __init__(self):
        self.winner = ""

    def build_playoff_bracket(self):
        url = ""
        home = TeamStats()
        home.parse_hockey_stats('WSH')
        away = TeamStats()
        away.parse_hockey_stats('PIT')
        print '\n'

sim = HockeySim()
sim.build_playoff_bracket()