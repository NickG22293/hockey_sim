#!/usr/bin/env python

# This file is intended to be the tools needed for the simulation of one game.
# Info is gathered from hockey-reference.com using web scraping to parse out
# relevant info from their static HTML pages.
# This is designed to be used in a large capacity for high-volume series simulations
# so optimization will have to be kept in mind.

from lxml import html, etree
import requests

# pull down info from stats site using lxml and requests
def parse_hockey_stats(team):
    # build the URL using Team
    url = "http://www.hockey-reference.com/teams/" + team + "/2016.html"
    page = requests.get(url)
    # content is put in a nice tree format for xpath parsing
    tree = html.fromstring(page.content)
    # Xpath query for team's stats
    stats = tree.xpath('//table[@id="team_stats"]/*/*')
    rows = iter(stats)
    for row in rows:
        values = [col.text for col in row]
        for c in values:
            if c:
                print 'Stats: ', c

def main():
    parse_hockey_stats('PIT')

main()