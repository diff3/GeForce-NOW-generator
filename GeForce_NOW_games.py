#!/usr/bin/env python3

"""
A Small script to download and compare game list from GeForce Now and
a users Steam gaming list. Do all configs in config.ini
"""

import configparser
import json
import urllib.request
import steamapi


def get_json(url_json):
    """
    Download json file from internet
    return json
    """
    with urllib.request.urlopen(url_json) as url:
        data = json.loads(url.read().decode())
    return data


def save_file(data, file_name):
    """
    Save a list to harddisk, one game per line
    """

    with open(file_name, 'w', encoding='utf8') as txt_file:
        for item in data:
            txt_file.write("%s\n" % item)


def generate_list(json_data):
    """
    Generates a Geforce list of game, also remove special characters for easier
    comparison.

    return list
    """

    global whitelist

    data = [''.join(filter(whitelist.__contains__,game['title'])).strip() for game in json_data]
    return data


def connect(api_key, userurl):
    """
    Downloads a list of games from Steam using it's API. Also removes special
    characters for easier comparison.

    return list
    """

    global whitelist

    steamapi.core.APIConnection(api_key=api_key, validate_key=True)
    user = steamapi.user.SteamUser(userurl=userurl)
    games = user.games
    games_list = [''.join(filter(whitelist.__contains__,game.name)).strip() for game in games]
    return games_list


def get_common(geforce_game_list, steam_game_list):
    """
    Comparies both lists and return a list with supported games
    """

    result = [game for game in steam_game_list if game in geforce_game_list]
    return result


if __name__ == "__main__":
    print("GeForce_NOW_games: Starting")

    # Config
    print("Loading configs")
    config = configparser.ConfigParser()
    config.read('config.ini')

    key = config['STEAM']['ApiKey']
    user = config['STEAM']['User']
    geforce_url = config['GEFORCE']['url']
    geforce = config['OUTPUT']['geforce']
    steam = config['OUTPUT']['steam']
    supported = config['OUTPUT']['supported']
    whitelist = set(config['WHITELIST']['list'])

    # GeForce Now
    print("Generating GeForce Now list")
    game_list = get_json(geforce_url)
    geforce_list = generate_list(game_list)
    geforce_list.sort()

    # Steam API
    try:
        print("Generating Steam list")

        steam_list = connect(key, user)
        steam_list.sort()
    except steamapi.errors.APIException:
        print("Couldn't get the game list from Steam.")
        input("Press Enter to exit...")
        exit(1)

    # Result
    print("Compare lists")
    result_data = get_common(geforce_list, steam_list)
    result_data.sort()

    # Save to files
    print("Saving lists")
    save_file(geforce_list, geforce)
    save_file(steam_list, steam)
    save_file(result_data, supported)

    print("Done!")
