from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 500

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    # Time Complexity O(logn), Space Complexity O(1)
    # Function returns score at closest offset
    # If you need exact offset match uncomment if statement
    if (
        type(game_stamps) is not list
        or len(game_stamps) < 1
        or type(game_stamps[0]) is not dict
        or 'offset' not in game_stamps[0]
        or 'score' not in game_stamps[0]
        or 'home' not in game_stamps[0]['score']
        or 'away' not in game_stamps[0]['score']
    ):
        raise ValueError('Incorrect game_stamps')
    
    if type(offset) is not int or offset < 0:
        raise ValueError('Incorrect offset')
    if offset > game_stamps[-1]['offset']:
        raise ValueError('There is no such offset')

    left = 0
    right = len(game_stamps)
    while left < right:
        mid = (right + left) // 2
        if offset <= game_stamps[mid]['offset']:
            right = mid - 1
        else:
            offset > game_stamps[mid]['offset']
            left = mid + 1
    # if game_stamps[left]['offset'] != offset:
    #     raise ValueError('There is no such offset')
    return game_stamps[left]['score']['home'], \
        game_stamps[left]['score']['away']
