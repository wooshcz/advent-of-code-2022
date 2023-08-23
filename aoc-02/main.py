
points_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_outcome = {'lose': 0, 'draw': 3, 'win': 6}
shape_opponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
shape_encrypted = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
rules = {
    'AX': 'draw',
    'AY': 'win',
    'AZ': 'lose',
    
    'BX': 'lose',
    'BY': 'draw',
    'BZ': 'win',

    'CX': 'win',
    'CY': 'lose',
    'CZ': 'draw',
    }

file = open('input.txt', 'r')
list_rounds = file.readlines()

def _calculate_score(round: str) -> int:
    sco = 0
    (opponent, encrypted) = round.split(' ')
    outcome = rules["".join((opponent, encrypted)).strip()]
    sco += points_outcome[outcome]
    sco += points_shape[shape_encrypted[encrypted.strip()]]
    return sco

print("How many rounds are in the list? %d" % len(list_rounds))

total_score = 0
for rnd in list_rounds:
    score = _calculate_score(rnd)
    #print("Score for the round: %d" % score)
    total_score += score

print("What would your total score be if everything goes exactly according to your strategy guide? %d" % total_score)

strategy_encrypted = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
rules_v2 = {
    'AA': 'draw',
    'AB': 'win',
    'AC': 'lose',
    
    'BA': 'lose',
    'BB': 'draw',
    'BC': 'win',

    'CA': 'win',
    'CB': 'lose',
    'CC': 'draw',
    }

def _calculate_score_v2(round: str) -> int:
    sco = 0
    (opponent, encrypted) = round.split(' ')
    strategy = strategy_encrypted[encrypted.strip()]
    #print(strategy)
    sco += points_outcome[strategy]
    for variant in ['A', 'B', 'C']:
        if rules_v2[opponent+variant] == strategy:
            sco += points_shape[shape_opponent[variant]]

    return sco

total_score2 = 0
for rnd in list_rounds:
    score = _calculate_score_v2(rnd)
    #print("Score for the round: %d" % score)
    total_score2 += score

print("""
    Following the Elf's instructions for the second column,
    what would your total score be if everything goes exactly
    according to your strategy guide? %d"""
    % total_score2)