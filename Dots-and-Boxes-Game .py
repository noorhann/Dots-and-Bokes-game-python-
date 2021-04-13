N, M = 5, 5
n_players = 2
marks = ['X', 'O']
count_boxes = [0 , 0]
grid=[['.' for i in range(M-1)]  for j in range(N-1)]
horizontal_grid=[[False for i in range(M)]  for j in range(N+1)]
vertical_grid =[[False for i in range(M+1)]  for i in range(N)]
#This function prints the grid of Dots-and-Boxes as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '------' * (M-1))
    for i in range(N):
        print(' . ', end = '')
        for j in range(M):
            print('---' if horizontal_grid[i][j] else '   ', end = '')
            if j < M-1:
                print(' . ', end = '')
        print()
        for j in range(M+1):
            print(' |  ' if vertical_grid[i][j] else '    ', end = '')
            if i < N-1 and j < M-1:
                print(grid[i][j] if grid[i][j] != '.' else ' ', end='')
            print(' ', end = '')
        print()
    for i in range(n_players):
        print('Player %c is %d'% (marks[i], count_boxes[i]))
    print('--' + '------' * (M-1))

#This function checks if the grid is full or not
def check_full():
    if sum(count_boxes) == (N-1)*(M-1):
        return True
    else :
        return False

#This function checks if the given side is empty or not
def check_empty_side(i1, j1, i2, j2):
    #horizontal_grid
    if i1 == i2 :
        if horizontal_grid[i1][j1] == False :
            return True
    #vertical_grid
    if j1 == j2 :
        if vertical_grid[i1][j1] == False :
            return True
    return False


#This function checks if the given position is valid in the grid or not
def check_valid_position(i, j):
    if i >= 0 and i < N and j>=0 and j < M:
        return True
    else:
        return False

#This function checks if given side is valid or not
def check_valid_side(i1, j1, i2, j2):
    if (i1-i2) == 0 and abs(j1-j2) == 1 :       #horizontal_grid
        return True
    if abs(i1-i2) == 1 and (j1-j2) == 0 :       #vertical_grid
        return True
    return False


#This function sets the given side
def set_side(i1, j1, i2, j2):
    #horizontal_grid
    if i1 == i2 :
        horizontal_grid[i1][j1] = True
    #vertical_grid
    if j1 == j2 :
        vertical_grid[i1][j1] = True

#This function checks and sets the neighbor completed boxes
def set_neighbor_boxes(i1, j1, i2, j2, player):
    counter = 0
    if horizontal_grid[i1][j1] == True:
        #---One Box----
        if horizontal_grid[i1-1][j1] == True and vertical_grid[i1-1][j1] == True and vertical_grid[i1-1][j1+1] == True and grid[i1-1][j1] == '.':
            grid[i1-1][j1] = marks[player]
            count_boxes[player] += 1
            counter += 1
        #---side neighbor boxes------
        if horizontal_grid[i1+1][j1] == True and vertical_grid[i1][j1] == True and vertical_grid[i1][j1] == vertical_grid[i1][j1+1] and grid[i1][j1] == '.':
            grid[i1][j1] = marks[player]
            count_boxes[player] += 1
            counter += 1
        # ---i___i
        if horizontal_grid[i1-1][j1] == True and horizontal_grid[i1+1][j1] == True and vertical_grid[i1-1][j1] == True and vertical_grid[i1-1][j1+1] == True and vertical_grid[i1][j1] == True and vertical_grid[i1][j1+1] == True and grid[i1-1][j1] == '.':
            grid[i1-1][j1] = marks[player]
            count_boxes[player] += 1
            counter += 1

    if vertical_grid[i1][j1] == True:
        if horizontal_grid[i1+1][j1-1] == vertical_grid[i1][j1] and horizontal_grid[i1][j1-1] == vertical_grid[i1][j1] and vertical_grid[i1][j1-1] == vertical_grid[i1][j1] and  grid[i1][j1-1] == '.':
            grid[i1][j1-1] = marks[player]
            count_boxes[player] += 1
            counter += 1
    if counter > 0:
        return  True
    else:
        return False


#This function arranges the points of the side
def arrange_side_points(i1, j1, i2, j2):
    #horizontal_grid
    if j1 > j2 :
        temp = j1
        j1 = j2
        j2 = temp
    #vertical_grid
    if i1 > i2 :
        temp2 = i1
        i1 = i2
        i2 = temp2
    return i1 , j1 , i2, j2

#This function clears the game structures
def grid_clear():
    for i in range (M-1) :
        for j in range (N-1) :
            grid[i][j]='.'
    count_boxes[:] = [0 , 0]
    horizontal_grid[:]=[[False for i in range(M)] for j in range(N+1)]
    vertical_grid[:] =[[False for i in range(M+1)] for i in range(N)]
#This function reads a valid and arranged side input
def read_input():
    i1, j1, i2, j2 = map(int, input('Enter the two points of the side: ').split())
    i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
    while not check_valid_position(i1, j1) or not check_valid_position(i2, j2) or \
          not check_valid_side(i1, j1, i2, j2) or not check_empty_side(i1, j1, i2, j2):
        i1, j1, i2, j2 = map(int, input('Enter a valid two points of the side: ').split())
        i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
    return i1, j1, i2, j2


#MAIN FUNCTION
def play_game():
    print("Dots-and-Boxes Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i1, j1, i2, j2 = read_input()
        #Set the input position with the mark
        set_side(i1, j1, i2, j2)
        #Set the neighbor boxes with the mark
        box_complete = set_neighbor_boxes(i1, j1, i2, j2, player)
        #Check if the state of the grid has a complete state
        if check_full():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            if count_boxes.count(max(count_boxes)) == 1:
                idx_max_player = count_boxes.index(max(count_boxes))
                print('Congrats, Player %s is won!' % marks[idx_max_player])
            else:
                print("Woah! That's a tie!")
            break
        #Keep the player if there is a complete box
        if not box_complete:
            #Player number changes after each turn
            player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
