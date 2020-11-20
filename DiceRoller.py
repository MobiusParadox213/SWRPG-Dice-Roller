from random import randrange
from pyinputplus import inputNum
from sys import exit

MAX_SKILL_DICE = 5

# {dice type: {face: [success/failure, advantage/threat, triumph/despair]}}
# {'force': {face: [dark side, light side]}}
DIE_FACES = {'boost': {1: [0, 0, 0], 2: [0, 0, 0], 3: [1, 0, 0],
                       4: [1, 1, 0], 5: [0, 2, 0], 6: [0, 1, 0]},

             'setback': {1: [0, 0, 0], 2: [0, 0, 0], 3: [1, 0, 0],
                         4: [1, 0, 0], 5: [0, 1, 0], 6: [0, 1, 0]},

             'ability': {1: [0, 0, 0], 2: [1, 0, 0], 3: [1, 0, 0],
                         4: [2, 0, 0], 5: [0, 1, 0], 6: [0, 1, 0],
                         7: [1, 1, 0], 8: [0, 2, 0]},

             'difficulty': {1: [0, 0, 0], 2: [1, 0, 0], 3: [2, 0, 0],
                            4: [0, 1, 0], 5: [0, 1, 0], 6: [0, 1, 0],
                            7: [0, 2, 0], 8: [1, 1, 0]},

             'proficiency': {1: [0, 0, 0], 2: [1, 0, 0], 3: [1, 0, 0],
                             4: [2, 0, 0], 5: [2, 0, 0], 6: [0, 1, 0],
                             7: [1, 1, 0], 8: [1, 1, 0], 9: [1, 1, 0],
                             10: [0, 2, 0], 11: [0, 2, 0], 12: [0, 0, 1]},

             'challenge': {1: [0, 0, 0], 2: [1, 0, 0], 3: [1, 0, 0],
                           4: [2, 0, 0], 5: [2, 0, 0], 6: [0, 1, 0],
                           7: [0, 1, 0], 8: [1, 1, 0], 9: [1, 1, 0],
                           10: [0, 2, 0], 11: [0, 2, 0], 12: [0, 0, 1]},

             'force': {1: [1, 0], 2: [1, 0], 3: [1, 0], 4: [1, 0],
                       5: [1, 0], 6: [1, 0], 7: [2, 0], 8: [0, 1],
                       9: [0, 1], 10: [0, 2], 11: [0, 2], 12: [0, 2]}}


def roll_dice(num_dice, die_type):
    """Rolls against the DIE_FACES dict to get results"""
    result1, result2, result3 = 0, 0, 0
    if 'force' in die_type:
        for i in range(num_dice):
            result_list = DIE_FACES[die_type][randrange(1, len(DIE_FACES[die_type]))]
            result1 += result_list[0]
            result2 += result_list[1]
        return result1, result2
    else:
        for i in range(int(num_dice)):
            result_list = DIE_FACES[die_type][randrange(1, len(DIE_FACES[die_type]))]
            result1 += result_list[0]
            result2 += result_list[1]
            result3 += result_list[2]
    return result1, result2, result3


def main():
    """Gets the amount of each die from players until players quit."""
    while True:
        dice_amounts = {'boost': 0, 'setback': 0,
                        'ability': 0, 'difficulty': 0,
                        'proficiency': 0, 'challenge': 0,
                        'force': 0}
        for k, v in dice_amounts.items():
            dice_amounts[k] = inputNum(prompt=k.capitalize() + ' Dice: ',
                                       default=int(0), min=0, max=MAX_SKILL_DICE)
        print()
        get_results(dice_amounts)
        response = input('\nPress ENTER to roll again, or type QUIT to exit.')
        if response.lower() == 'quit':
            exit()


def get_results(num_dice):
    """Takes the number of dice and the type of dice and gives the results to the player."""
    successes, advantage, triumphs = 0, 0, 0
    failures, threats, despair = 0, 0, 0
    light_side, dark_side = 0, 0

    for k, v in num_dice.items():
        if v == 0:
            continue
        elif k in ('boost', 'ability', 'proficiency'):
            results = roll_dice(v, k)
            successes += results[0]
            advantage += results[1]
            triumphs += results[2]
        elif k in ('setback', 'difficulty', 'challenge'):
            results = roll_dice(v, k)
            failures += results[0]
            threats += results[1]
            despair += results[2]
        else:
            results = roll_dice(v, k)
            dark_side += results[0]
            light_side += results[1]

    print('Total Results:\n'
          'Successes: ', successes,
          '\nAdvantages: ', advantage,
          '\nTriumph: ', triumphs,
          '\nFailures: ', failures,
          '\nThreat: ', threats,
          '\nDespair: ', despair)
    if light_side > 0 or dark_side > 0:
        print('Light Side: ', light_side,
              '\nDark Side: ', dark_side, '\n')
    else:
        print()

    print('Net Results:')
    if successes > failures:
        print('Successes: ', successes - failures)
    elif failures > successes:
        print('Failures: ', failures - successes)

    if advantage > threats:
        print('Advantage: ', advantage - threats)
    elif threats > advantage:
        print('Threats: ', threats - advantage)

    if triumphs > 0: print('Triumphs: ', triumphs)
    if despair > 0: print('Despair: ', despair)
    if successes == failures == advantage == \
            threats == triumphs == despair == 0:
        print('Complete wash!')

    if light_side > 0: print('Light Side: ', light_side)
    if dark_side > 0: print('Dark Side: ', dark_side)


if __name__ == '__main__':
    main()
