#first import all the libraries needed
from board import tic_tac_toe
import matplotlib.pyplot as plt
import numpy as np
import random
# from IPython.display import clear_output


game = tic_tac_toe()
game.printBoard()

def choose_move(avail_moves, current_state, states_and_values, epsilon = 0.1):
    """
    inputs
    -------
    avail_moves - moves that are available to choose from
    current_state - the current state vector of the game
    states_and_values - a dictionary containing all the past states and their values
    epsilon - the probability the algorithm will explore new moves default at 0.1
    
    output
    -------
    action - this function outputs the most rewarding move
    """    
    #exploration. choose 0 and 1 with a given probability. and explore if 0 is chosen
    explore = np.random.choice([0, 1], p = [epsilon, 1 - epsilon])
    
    if explore == 0:
        
        #randomly choose action
        action = np.random.choice(avail_moves)
    
    else:
        
        #max val
        max_val = -999
        
        #iterate through all the available moves
        for avail_move in avail_moves:

            #current state
            cs = current_state
            cs.append(avail_move) #add the available move to the current state
            
            #check if this move has already been played 
            if tuple(cs) in states_and_values.keys():
                
                #if the move is played get the value
                val = states_and_values[tuple(cs)]
            
            else:
                
                val = 0
                
            #check if its higher than the max val
            if val > max_val:

                #if it is higher we will choose that value for next action
                action = avail_move
                max_val = val
                    
            #remove this move from the list before moving on to the next iteration (next available move)
            cs.remove(avail_move)       
        
    return action
#create a state_values dictionary
# states_and_values = {(1): 0.1, (1, 5): 0.9, (2):5, (2, 3, 1): 7, (2, 3, 9): 4, (1, 6): 3} 

# #choose_move(avail_moves, current_state, states_and_values, epsilon = 0.1):

# #hypothetical situation 1 
# current_state = [1]
# avail_moves = [2, 3, 4, 5, 6, 7, 8, 9]

#run 100 its
# move1 = []
# for i in range(100):
#     move1.append(choose_move(avail_moves, current_state, states_and_values))
    
# #situation 2
# current_state = [2, 3]
# avail_moves = [1, 4, 5, 6, 7, 8, 9]

# #run 100 its 
# move2 = []
# for i in range(100):
#     move2.append(choose_move(avail_moves, current_state, states_and_values))
i=0
#plot histograms to see which move was selected
# fig, ax = plt.subplots(1, 2, figsize = (10, 3))
# ax[0].hist(move1)
# ax[1].hist(move2)
# ax[0].set_title('Hypothetical situation 1')
# ax[1].set_title('Hypothetical situation 2')
# plt.show()
def give_reward(states_and_values, states, reward, alpha, gamma):
    
    """
    inputs
    ---------
    states_and_values - a dictionary containing states and each state's values
    states - states at the end of the current game
    reward - the awarded reward or penalty value 
    alpha - the learning_rate by default set to 0.5
    gamma - the discount factor when giving rewards to earlier states. Default is 0.1
    
    output
    -------
    states_and_values - a dictionary after the moves with the new reward added
    """
        
    for state in reversed(states):
        
        if tuple(state) in states_and_values.keys():
            
            states_and_values[tuple(state)] += alpha * (gamma * reward - states_and_values[tuple(state)])
        
        
        elif (tuple(state) not in states_and_values.keys()) and (i != (len(states) - 1)):       
            
            states_and_values[tuple(state)] = alpha * gamma * reward
        
        reward = states_and_values[tuple(state)]
        
    return states_and_values
def self_play(num_its, strategy_p1, strategy_p2, epsilon_p1 = 0.5, epsilon_p2 = 0.1, alpha_p1 = 0.2, alpha_p2 = 0.2, \
              gamma_p1 = 0.9, gamma_p2 = 0.9, print_game = False):
    
    """
    inputs
    -------
    num_its = number of iterations
    strategy_p1 = strategy of player 1. The strategy is either "random" or "rl" for both players
    strategy_p2 = strategy of player 2. The strategy is either "random" or "rl" for both players
    epsilon_p1 = exploration rate for player 1
    epsilon_p2 = exploration rate for player 2
    alpha_p1 = learning rate of player 1
    alpha_p2 = learning rate of player 2
    gamma_p1 = discount factor for player 1
    gamma_p2 = discount factor for player 2
    print_game = print every 1000 games true or false
    
    Outputs
    -------
    p1_wins = a vector containing 1 for wins and 0 for losses & draws for player 1
    p2_wins = a vector containing 1 for wins and 0 for losses & draws for player 2
    draw - a vector containing 1 for a draw game and 0 if a player won
    player1 = states and values for player 1
    player2 = states and values for player 2  
    
    """
        
    #player 1 memory NEWWWWWW
    player1 = {}
    p1_wins = []

    #p2
    player2 = {}
    p2_wins = []

    #draws
    draw = []

    for i in range(num_its):

        #player 1 is always first
        player = 1

        #game_on
        game_on = True

        #initialize the game
        game = tic_tac_toe()

        #initial values
        move_number = 1
        avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        current_state = []
        winner = ''

        #lists
        states1 = []
        states2 = []

        while move_number < 10:
            #choose move for each player

            if player == 1:
                
                if strategy_p1 == 'rl':
                    move = choose_move(avail_moves, current_state, player1, epsilon_p1)
                elif strategy_p1 == 'random':
                    print("--")
                    move = np.random.choice(avail_moves)
                    
            elif player == 2:
                
                if strategy_p2 == 'rl':
                    move = choose_move(avail_moves, current_state, player2, epsilon_p2)
                elif strategy_p2 == 'random':
                    print("++")
                    move = np.random.choice(avail_moves)
                    
            #play the move
            _, avail_moves = game.play(move, player)
            winner = game.check_winner()

            #change the move number
            move_number = move_number + 1
            #append the move to the current state
            current_state.append(move)

            #append all moves
            states1.append(list(current_state))
            states2.append(list(current_state))

            #switch turns
            if player == 1:

                player = 2

            elif player == 2:
                player = 1

        if winner == 'O':

            #player 1
            player1 = give_reward(player1, states1, 1, alpha_p1, gamma_p1)        

            #player 2
            player2 = give_reward(player2, states2, -1, alpha_p2, gamma_p2)

            p1_wins.append(1)
            p2_wins.append(0)
            draw.append(0)

        elif winner == 'X':

            #Player 2
            player2 = give_reward(player2, states2, 1, alpha_p2, gamma_p2)

            #player 1
            player1 = give_reward(player1, states1, -1, alpha_p1, gamma_p1)

            p1_wins.append(0)
            p2_wins.append(1)
            draw.append(0)


        elif winner is None:

            #player 1
            player1 = give_reward(player1, states1, 0.5, alpha_p1, gamma_p1)

            #player 2
            player2 = give_reward(player2, states2, 0.5, alpha_p2, gamma_p2)


            p1_wins.append(0)
            p2_wins.append(0)
            draw.append(1)
            
    return p1_wins, p2_wins, draw, player1, player2

#plot game and number of wins
def cum_sum(p_wins):
    """
    input
    ------
    p_wins - vector containing 1's and 0's
    
    output
    ------
    x + 1 - an array that represent each game
    y - cumulative sum at each x value
    
    """
    
    x = np.arange(0, len(p_wins))
    y = []
    s = 0
    
    for i in range(len(x)):
        
        s += p_wins[i]
        y.append(s)
        
    
    y = np.array(y)           
    
    return x + 1, y 
p1_wins, p2_wins, draw, player1, player2 = self_play(500, 'random', 'rl', print_game = True)
#plot the results
#for player 1 and 2 find the cumulative sum 

x1, y1 = cum_sum(p1_wins)
x2, y2 = cum_sum(p2_wins)
dx, dy = cum_sum(draw)

# plt.figure(figsize = (10, 6))
# plt.xkcd()
# plt.plot(x1, y1, color = 'r', linewidth = 2, label = 'Player O - Reinforcement Learning agent')
# plt.plot(x2, y2, color = 'b', linewidth = 2, label = 'Player X - Random agent')
# plt.plot(dx, dy, color = 'k', linewidth = 2, label = 'Draw')
# plt.title('RL agent vs random agent')
# plt.xlabel('Game number')
# plt.ylabel('Number of Wins')
# plt.legend()
# plt.show()

#print winning percentage 
print('Winning percentage for player 1 (Random agent): {} %'.format(np.round(sum(p1_wins)/len(p1_wins)*100, 4)))
print('Winning percentage for player 2 (RL agent): ', np.round(sum(p2_wins)/len(p2_wins)*100, 4), '%')
print('Percentage of a game being draw: ', np.round(sum(draw)/len(draw)*100, 4), '%')