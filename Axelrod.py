import random
import matplotlib.pyplot as plt
from itertools import combinations

p1_points_arr = []  
p2_points_arr = []


########################### STRATEGIES ################################
def random_s(a, b, c, d, e, f, g):    #returns a random choice
    return random.choice(['C', 'D'])

def always_c(a, b, c, d, e, f, g):    # always cooperates
    return 'C'  

def always_d(a, b, c, d, e, f, g):      # always defects
    return 'D'

def tit_for_tat(prev_move_1, prev_move_2, turn, p1, p2, f, g):     # starts with cooperation. Plays whatever the opponent just played
    if turn == 0: 
        return 'C'
    else:
        if tit_for_tat == p1:
            return prev_move_2 
        elif tit_for_tat == p2:
            return prev_move_1
        else:
            return None

def grofman(prev_move_1, prev_move_2, c, d, e, f, g):    # if the players did different things last round, grofman cooperates with probability 2/7. If they did the same thing, it cooperates
    if prev_move_1 != prev_move_2:
        prob = random.randint(1, 7)
        if prob <= 2:
            return 'C'
        else:
            return 'D'
    else:
        return 'C'

def grudger(prev_move_1, prev_move_2, c, p1, p2, f, g):     # constantly cooperates until the opponent defects, then defects for the rest of the match
    if grudger == p1:
        if prev_move_2 == 'D':
            return 'D'
        elif prev_move_1 == 'D':
            return 'D'
        else:
            return 'C'
    elif grudger == p2:             # p1 and p2 logic aren't needed here, but they might be for optimisation so i'll leave it in for now
        if prev_move_1 == 'D':
            return 'D'
        elif prev_move_2 == 'D':
            return 'D'
        else:
            return 'C'

def davis(prev_move_1, prev_move_2, turn, d, e, f, g):     #cooperates for the first 10 turns, then plays grudger
    if turn < 10:
        return 'C'
    else:
        if prev_move_1 == 'D':
            return 'D'
        elif prev_move_2 == 'D':
            return 'D'
        else:
            return 'C'
        
def joss(prev_move_1, prev_move_2, turn, p1, p2, f, g):      #Starts with C. If the opponent cooperates, Joss cooperates 90% of the time. Always defects following a defect
    if turn == 0:
        return 'C'
    if joss == p2:
        if prev_move_1 == 'C':
            prob1 = random.randint(1, 10)
            if prob1 == 1:
                return 'D'
            else:
                return 'C'
        elif prev_move_1 == 'D':
            return 'D'
    elif joss == p1:
        if prev_move_2 == 'C':
            prob2 = random.randint(1, 10)
            if prob2 == 1:
                return 'D'
            else:
                return 'C'
        elif prev_move_2 == 'D':
            return 'D'

def tullock(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr):   # lots of unnecesary logic just to show how it works
    if turn < 10:                                                                  # cooperates on first ten moves, then cooperates ten percent less than the opponent just did
        return 'C'
    else:
        if tullock == p1:
            no_c = 0
            for i in range(10):
                if p2_moves_arr[i] == 'C':
                    no_c += 1
            probability = no_c - 1
            num1 = random.randint(1, 10)
            if num1 <= probability:
                return 'C'
            else:
                return 'D'
        elif tullock == p2:
            no_c2 = 0
            for i in range(10):
                if p1_moves_arr[i] == 'C':
                    no_c2 += 1
            probability2 = no_c2 - 1
            num2 = random.randint(1, 10)
            if num2 <= probability2:
                return 'C'
            else:
                return 'D'
            
def shubik(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr):
    if turn == 0:
        return 'C'
    else:
        if shubik == p1:
            co_d = 0
            if prev_move_2 == 'D':
                co_d += 1
                if turn > 2:
                    for i in range(1, turn):
                        if p2_moves_arr[turn - i] == 'D':
                            co_d += 1
                            return 'C'
                        else:
                            print(co_d)
                            co_d = 0
                            return 'C'
                            break
            print(co_d)
            if co_d == 0:
                return 'C'
            else:
                return 'D'
        elif shubik == p2:
            co_d = 0
            if prev_move_1 == 'D':
                co_d += 1
                if turn > 2:
                    for i in range(1, turn):
                        if p1_moves_arr[turn - i] == 'D':
                            co_d += 1
                            return 'C'
                        else:
                            print(co_d)
                            co_d = 0
                            return 'C'
                            break
            print(co_d)
            if co_d == 0:
                return 'C'
            else:
                return 'D'      # shubik not working. too many logic errors
            
def feld(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr):
    return None # TFT, except prob of cooperation after cooperation decreases from 1 (turn 1) to 0.5 (turn 200)
# will need to probability distribute to test
            


def testing_strat(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr):    # a testing strategy. should always be the last strategy so that logic errors involving p1 and p2 logic can be spotted
    return random.choice(['C', 'D'])

#######################################################################

######################### STRATEGIES ARRAYS #############################
total_random = []
total_always_c = []
total_always_d = []
total_tit_for_tat = []
total_grofman = []
total_grudger = []
total_davis = []
total_joss = []
total_tullock = []
total_shubik = []
total_testing_strat = []
#########################################
def match(p1, p2):
    prev_move_1 = None
    prev_move_2 = None
    p1_points = 0
    p2_points = 0 
    p1_moves_arr = []
    p2_moves_arr = []
    
    for turn in range(20): 
        move_1 = p1(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr)
        move_2 = p2(prev_move_1, prev_move_2, turn, p1, p2, p1_moves_arr, p2_moves_arr)
        prev_move_1 = move_1
        prev_move_2 = move_2
        p1_moves_arr.append(prev_move_1)
        p2_moves_arr.append(prev_move_2)
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
        davis: total_davis,
        joss: total_joss,
        tullock: total_tullock,
        shubik: total_shubik,
        testing_strat: total_testing_strat
    }
    
    strategy_points_mapping[p1].append(p1_points)
    strategy_points_mapping[p2].append(p2_points)

    print(total_random)
    print(total_always_c)
    print(total_always_d)
    print(total_tit_for_tat)
    print(total_grofman)
    print(total_grudger)
    print(total_joss)
    print(total_tullock)
    print(total_shubik)
    print(total_testing_strat)

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

    total_points = [sum(total_random), sum(total_always_c), sum(total_always_d), 
                    sum(total_tit_for_tat), sum(total_grofman), sum(total_grudger), 
                    sum(total_davis), sum(total_joss), sum(total_tullock),
                    sum(total_testing_strat), sum(total_shubik)]

    print('randoms total points are ', sum(total_random))
    print('alwac=ys c ', sum(total_always_c))
    print('always d', sum(total_always_d))
    print('tft', sum(total_tit_for_tat))
    print('Grofman', sum(total_grofman))
    print('grudger ', sum(total_grudger))
    print('Davis ', sum(total_davis))
    print('Joss', sum(total_joss))
    print('Tullock', sum(total_tullock))
    print('Shubik ', sum(total_shubik))
    print('Testing', sum(total_testing_strat))

    _, ax = plt.subplots()

    bar_colours = ['xkcd:red', 'xkcd:orange', 'xkcd:gold', 'xkcd:pea green', 'xkcd:deep green', 'xkcd:royal', 'xkcd:water blue', 'xkcd:wisteria', 'xkcd:bubblegum', 'xkcd:cyan', 'xkcd:light lavender']
    strategies_str = ['Random', 'Always Cooperate', 'Always Defect', 'Tit-for-Tat', 'Grofman', 'Grudger', 'Davis', 'Joss', 'Tullock', 'Shubik',   'Test']
    ax.bar(strategies_str, total_points, color=bar_colours)

    plt.show()

if __name__ == "__main__":
    strategies = [random_s, always_c, always_d, tit_for_tat, grofman, grudger, davis, joss, tullock, shubik, testing_strat]

    game(strategies)
