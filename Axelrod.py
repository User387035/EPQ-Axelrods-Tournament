import random
import matplotlib.pyplot as plt
from itertools import combinations

p1_points_arr = []  
p2_points_arr = []

########################### STRATEGIES ################################
def random_s(prev_move_1, prev_move_2, turn):
    return random.choice(['C', 'D'])

def always_c(prev_move_1, prev_move_2, turn):
    return 'C'  

def always_d(prev_move_1, prev_move_2, turn):
    return 'D'

def tit_for_tat(prev_move_1, prev_move_2, turn):
    if prev_move_2 is None: 
        return 'C'
    else:
        return prev_move_1 

def grofman(prev_move_1, prev_move_2, turn):
    if prev_move_1 == prev_move_2:
        prob = random.randint(1, 7)
        if prob <= 2:
            return 'C'
        else:
            return 'D'
    else:
        return 'C'

def grudger(prev_move_1, prev_move_2, turn):
    if prev_move_1 == 'D':
        return 'D'
    elif prev_move_2 == 'D':
        return 'D'
    else:
        return 'C'
    
def davis(prev_move_1, prev_move_2, turn):
    if turn < 10:
        return 'C'
    else:
        if prev_move_1 == 'D':
            return 'D'
        elif prev_move_2 == 'D':
            return 'D'
        else:
            return 'C'


#######################################################################

######################### STRATEGIES ARRAYS #############################
total_random = []
total_always_c = []
total_always_d = []
total_tit_for_tat = []
total_grofman = []
total_grudger = []
total_davis = []
#######################
def match(strategy1, strategy2):
    prev_move_1 = None
    prev_move_2 = None
    p1_points = 0
    p2_points = 0  
    
    for turn in range(199): 
        move_1 = strategy1(prev_move_1, prev_move_2, turn)
        move_2 = strategy2(prev_move_1, prev_move_2, turn)
        prev_move_1 = move_1
        prev_move_2 = move_2
        if move_1 == 'C' and move_2 == 'D':
            p1_points += 0
            p2_points += 5
        elif move_1 == 'D' and move_2 == 'C':
            p1_points += 5
            p2_points += 0
        elif move_1 == 'D' and move_2 == 'D':
            p1_points += 1
            p2_points += 1
        else: 
            p1_points += 3
            p2_points += 3
        print(move_1, move_2)  # testing
    
    strategy_points_mapping = {
        random_s: total_random,
        always_c: total_always_c,
        always_d: total_always_d,
        tit_for_tat: total_tit_for_tat,
        grofman: total_grofman,
        grudger: total_grudger,
        davis: total_davis
    }
    
    strategy_points_mapping[strategy1].append(p1_points)
    strategy_points_mapping[strategy2].append(p2_points)

    print(total_random)
    print(total_always_c)
    print(total_always_d)
    print(total_tit_for_tat)
    print(total_grofman)
    print(total_grudger)

    if p1_points > p2_points:
        print(f"Player 1 wins with {p1_points} points") 
    elif p1_points < p2_points:
        print(f"Player 2 wins with {p2_points} points")




def game(strategies__):
    for i, (p1, p2) in enumerate(combinations(strategies__, 2)):
        print(f"Match between ", p1, "and ", p2)
        match(p1, p2)
        print()
    
    for i, p1 in enumerate(strategies__):
        print(f"Match between ", p1, 'and itself')
        match(p1, p1)
        print()

    total_points = [sum(total_random), sum(total_always_c), sum(total_always_d), sum(total_tit_for_tat), sum(total_grofman), sum(total_grudger), sum(total_davis)]

    print('randoms total points are ', sum(total_random))
    print('alwac=ys c ', sum(total_always_c))
    print('always d', sum(total_always_d))
    print('tft', sum(total_tit_for_tat))
    print('Grofman', sum(total_grofman))
    print('grudger ', sum(total_grudger))
    print('Davis ', sum(total_davis))

    _, ax = plt.subplots()

    bar_colours = ['tab:red', 'tab:orange', 'y', 'tab:green', 'tab:blue', 'tab:purple', 'tab:pink']
    strategies_str = ['Random', 'Always Cooperate', 'Always Defect', 'Tit-for-Tat', 'Grofman', 'Grudger', 'Davis']
    ax.bar(strategies_str, total_points, color=bar_colours)

    plt.show()

if __name__ == "__main__":
    strategies = [random_s, always_c, always_d, tit_for_tat, grofman, grudger, davis]

    game(strategies)
