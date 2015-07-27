"""
Defend mode:
- place ships (1) 3 (1) 5 (2) 2
- horizontal or vertical
- must check bounds of board
- must check for overlapping ships

will receive random attacks
prompt after fire if hit or miss
(check for truth)
no repeat fires
EC: more than random targeting

Board: A-J and 1-10 for columns

00 01 02 03 04 05...
10
20
30
40
50

"""

import random

board = [[" " for x in range(10)] for q in range(10)]  # 2 D array , create an empty aray ,( fill Nones for 3 rows) then repeat for the 3 cols


# how are we going to store all the ships on the board
    

def draw_board():
    #draw row indicator
    for col_number in range(1,11):
        #print ' ' + str(col_number) + ' |'
        pass
    
    for row in board:
        print row
         #i = board.index(row)
         #for col in row:
            #j = row.index(col)
            #print str(i) + str(j) 
            #print "\n"
            
already_called = []
ships = {"aircraft":[]}  #update_board[x][y]
ship_lengths = {"aircraft":5}

def place_ships():  # cycle through each ship type and prompt, or let user decide
    global ships
    # place ships (1) 3pegs (1) 5pegs (2) 2pegs
    ship_start_position = raw_input("Please select upper left position for Carrier: ")
    #ship_orientation = raw_input("(H)orizontal or (V)ertical")
    #check bounds
    
    if is_position_valid(ship_start_position,"aircraft"):
        position = position_to_tuple(ship_start_position)
        position_row, position_col = position
        ship_length = ship_lengths["aircraft"]
        # horizontal only, (0,0) (0,1)... col incremented by 1
        # loop from start position to length of ship and place all tuples
        for extend_ship in range(0,ship_length):
            newposition =  tuple((position_row,position_col+extend_ship))
            ships["aircraft"].append(newposition)
            
    #print ships["aircraft"]

def is_position_valid(position, boat_type):
    return True
        

def generate_random_shot():
    guessrow = random.randint(0, 9)
    guesscol = random.randint(0, 9)
    return guessrow,guesscol

def check_shot(position): 
    global ships
    position_tuple = position
    
    if position_tuple in already_called:
        print "Position was already fired"
        return False
    
    # see if it's a hit or not - check the ship dictionaries?
    is_hit = False
    print ships
    print position_tuple
    for ship_name,ship_positions in ships.iteritems():
        if position_tuple in ship_positions:
            #hit
            #update board
            board[position_tuple[0]][position_tuple[1]] = 'X'
            #now clear from ships dictionary
            ships[ship_name].remove(position_tuple)
            #add position to list of already called positions
            already_called.extend(position_tuple)
            is_hit = True
        return "Hit"
    
    if is_hit == False:
        board[position_tuple[0]][position_tuple[1]] = '-'
        already_called.extend(position_tuple) 
    
    return "Miss"
                    
    


#board[0][1] = X
#ships[ship1].remove(1,2) #< delete tuple from ship to indicate a hit
# hit OR miss put tuple in already_called list

    
def position_to_tuple(position): # convert A1 to 01, B2 to 22, etc
    if position[0].lower() == 'a':
        position_row = 0
    if position[0].lower() == 'b':
        position_row = 1
    if position[0].lower() == 'c':
        position_row = 2
    if position[0].lower() == 'd':
        position_row = 3
    if position[0].lower() == 'e':
        position_row = 4
    if position[0].lower() == 'f':
        position_row = 5
    if position[0].lower() == 'g':
        position_row = 6
    if position[0].lower() == 'h':
        position_row = 7
    if position[0].lower() == 'i':
        position_row = 8
    if position[0].lower() == 'j':
        position_row = 9
    
    position_col = int(position[1]) - 1 
    return int(position_row), int(position_col) # returns needed array indexes as a tuple
    
    #(0,1)
    #row = postiion[0] 
    #col = position[1]
    #board[row][col] = "X"
    
    

def place_ship(ship_type,starting_position,orientation):
    ship_type = raw_input("Select a ship to place: (S)ubmarine, (A)ircraft Carrier, (P)atrol Boat-2")
    ship_start_position = position_to_tuple(raw_input("Select starting left or top position of ship"))
    ship_orientation = raw_input("Select (H)orizontal or (V)ertical placement")
    #if ship_type_available():
        #if placement_valid(): #check board overflow and ship overlap
    pass
            #update board with ship
    

def is_hit(position): #<--- A1,B1,.... [0][1]
    pass

def select_mode():
    game_mode = raw_input("(D)efend or (A)ttack: ")
    
    return game_mode


def fire():
    #if is_hit_array(not empty):
    pass

def game_won():
    for ship, ship_positions in ships.iteritems():
        if len(ship_positions) > 0:
            return False
    return True
      
if __name__ == "__main__":

    game_mode = select_mode();
    
    if game_mode == 'D':
        
        draw_board()
        place_ships()
        
        while not game_won():
            random_position = generate_random_shot()
            # remember to avoid duplicate positions - updated random
            print "Computer firing at: "+str(random_position)
            if check_shot(random_position):
                
        
        
                
        
        
    elif game_mode == 'A':
        pass
   
    
    
    
