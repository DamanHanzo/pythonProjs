import cards

def setup():
    my_deck = cards.Deck()
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a tableau (a list of 8 lists, the dealt cards)
    """
    foundation = [[],[],[],[]]
    cell = [[],[],[],[]]
    my_deck.shuffle()
    new_card=my_deck.pretty_print()
    tableau=[[],[],[],[],[],[],[],[]]
    column = 0
    while not my_deck.is_empty():
        tableau[column].append(my_deck.deal())
        column += 1
        if column % 8 == 0:
            column = 0
    for i in range(4):
        print("tableau",i,tableau[i])

    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    tableau=tableau
    foundation=foundation
    t_col=t_col
    f_col=f_col

    

    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    pass


def move_to_cell(tableau,cell,t_col,c_col):
    tableau=tableau
    cell=cell
    t_col=t_col
    f_col=f_col
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    pass

def move_to_tableau(tableau,foundation,t_col,f_col):
    tableau=tableau
    foundation=foundation
    t_col=t_col
    f_col=f_col
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    pass
        

def is_winner(foundation):
    foundation=foundation
    if len(foundation)==52:
        x=True
    else:
        x=False
    return x
       

def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    pass
        

def print_game(foundation, tableau,cell):
    tableau=tableau
    cell=cell
    foundation=foundation


 
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(c[0]), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(stack[-1]), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:8s}'.format(stack[i]), end = '')
            except IndexError:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    while True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            if r == 't2f':
                move_to_foundation(tableau,foundation,t_col,f_col)                          
            elif r == 't2t':
                pass # you implement                          
            elif r == 't2c':
                pass # you implement                          
            elif r == 'c2t':
                pass # you implement                          
            elif r == 'c2f':
                pass # you implement                          
            elif r == 'q':
                break
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    

