#!/usr/bin/env python3

import os
import sys
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def __get_br_player_stats():

    url = "https://api.fortnitetracker.com/v1/profile/"
    endpoint = url + profile + '/' + epicname
    headers = {'content-type': 'application/json', 'TRN-Api-Key': apikey}

    # ==============================================
    # Submit the request to the fortnite tracker API
    # ==============================================
    s = requests.Session()
    r = s.get(endpoint, headers=headers, verify=False)
    brps = r.json()

    return brps


def __get_br_match_stats():
    pass


if __name__ == "__main__":

    profile = 'pc'

    if os.path.isfile('credentials.txt'):
        apikey, epicname = open('credentials.txt').read().strip().split(',')
    else:
        print("Cannot find credentials file")
        sys.exit(1)

    player_stats = __get_br_player_stats()
    match_stats = __get_br_match_stats()

    # ======================
    # Get the lifetime stats
    # ======================
    lifetime_stats = player_stats['lifeTimeStats']

    # =============================
    # Create a new blank dictionary
    # =============================
    # =============================
    dicts_by_key = {}

    # ========================================================
    # Lifetime stats are represented in the variable lt_stats
    # This comes in as a list of dictionaries that we need to
    # iterate over.
    # I am adding each dictionary to dicts_by_key which should
    # result in 12 dictionary objects.
    # ========================================================

    for dicts in lifetime_stats:
        dicts_by_key[dicts['key']] = dicts

    # ============================================================
    # Now setup some lifetime_total vairables from the dictionarys
    # ============================================================
    lt_total_wins = dicts_by_key['Wins']
    lt_total_kills = dicts_by_key['Kills']
    lt_total_score = dicts_by_key['Score']
    lt_top_25s = dicts_by_key['Top 25s']
    lt_top_10s = dicts_by_key['Top 10']
    lt_top_5s = dicts_by_key['Top 5s']
    lt_total_matches_played = dicts_by_key['Matches Played']

    # ====================================================
    # I now setup list objects with the dictionary values
    # I use lists so that I can reference the index value.
    # ====================================================
    lt_total_wins_val_list = list(lt_total_wins.values())
    lt_total_kills_val_list = list(lt_total_kills.values())
    lt_total_score_val_list = list(lt_total_score.values())
    lt_top_25s_val_list = list(lt_top_25s.values())
    lt_top_10s_val_list = list(lt_top_10s.values())
    lt_top_5s_val_list = list(lt_top_5s.values())
    lt_total_matches_played_val_list = list(lt_total_matches_played.values())

    # ===========================================
    # This is the final output of our application
    # ===========================================
    print("=======================")
    print("Fortnite Tracker (v0.1)")
    print("=======================")
    print(("Player: {}").format(epicname))
    print("\t====================")
    print("\tLifetime Statistics:")
    print("\t====================")
    print(f"\tTotal Wins    : {lt_total_wins_val_list[1]}")
    print(f"\tKills         : {lt_total_kills_val_list[1]}")
    print(f"\tMatches Played: {lt_total_matches_played_val_list[1]}")
    print(f"\tOverall Score : {lt_total_score_val_list[1]}")
    print()
    print(f"\t=========")
    print(f"\tPlacings:")
    print(f"\t=========")
    print(f"\tNo. Top 25s   : {lt_top_25s_val_list[1]}")
    print(f"\tNo. Top 10s   : {lt_top_10s_val_list[1]}")
    print(f"\tNo. Top 5s    : {lt_top_5s_val_list[1]}")
