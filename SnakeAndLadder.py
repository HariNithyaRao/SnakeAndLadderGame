from PIL import Image
import random

end = 100
def show_board():
    img = Image.open('snake.png')							# open any snake board image from your pc.
    img.show()   
def play():
    #input player names
    p1_name = input("player1,enter your name: ") 
    p2_name = input("player2, enter your name: ")
    #initial points of players
    pp1 = 0
    pp2 = 0

    #chance/turn of players
    turn = 0
    while(1):
        if turn % 2 == 0:
            #player1 turn
            print(p1_name, "your turn")
            # ask players choice to continue the game
            choice = input("press1 to continue/press 0 to quit: ")
            if choice == 0:
                print(p1_name,"score:",pp1)
                print(p2_name,"score:",pp2)
                print("THANKS FOR PLAYING")
                break
            dice = random.randint(1, 6) # generate a number from 1 to 6 inclusively
            print("dice showed:",dice)
            pp1 = pp1 + dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            if pp1 > end: # checking points of player if goes beyond the end
                pp1 = end
            print(p1_name,"your score: ",pp1)
            if reached_end (pp1):
                print(p1_name, "you won the game")
                break
                
        
        else:
             #player2 turn
             print(p2_name, "your turn")
             # ask players choice to continue the game
             choice = input("press1 to continue/press 0 to quit: ")
             if choice == 0:
                 print(p2_name,"score:",pp2)
                 print(p1_name,"score:",pp1)
                 print("THANKS FOR PLAYING")
                 break
             dice = random.randint(1, 6) # generate a number from 1 to 6 inclusively
             print("dice showed:",dice)
             pp2 = pp2 + dice
             pp2 = check_ladder(pp2)
             pp2 = check_snake(pp2)
             if pp2 > end: # checking points of player if goes beyond the end
                 pp2 = end
             print(p2_name,"your score: ",pp2)
             if reached_end (pp1):
                 print(p2_name, "you won the game")
                 break
        turn += 1
def check_ladder(points):
    if points == 8:
        print("ladder")
        return 26
    elif points == 21:
        print("ladder")
        return 82
    elif points == 43:
        print("ladder")
        return 77
    elif points == 50:
        print("ladder")
        return 91
    elif points == 54:
        print("ladder")
        return 93
    elif points == 62:
        print("ladder")
        return 96
    elif points == 66:
        print("ladder")
        return 87
    elif points == 80:
        print("ladder")
        return 100
    else:
        return points
def check_snake(points):
    if points == 44:
        print("Snake")
        return 22
    elif points == 46:
        print("Snake")
        return 5
    elif points == 48:
        print("Snake")
        return 9
    elif points == 52:
        print("Snake")
        return 11
    elif points == 55:
        print("Snake")
        return 7
    elif points == 59:
        print("Snake")
        return 17
    elif points == 64:
        print("Snake")
        return 36
    elif points == 69:
        print("Snake")
        return 33
    elif points == 46:
        print("Snake")
        return 5
    elif points == 73:
        print("Snake")
        return 1
    elif points == 83:
        print("Snake")
        return 19
    elif points == 92:
        print("Snake")
        return 51
    elif points == 95:
        print("Snake")
        return 24
    elif points == 98:
        print("Snake")
        return 28
    else:
        return points
def reached_end(points):
    if points == end:
        return True
    else:
        return False

show_board() 
play()            
