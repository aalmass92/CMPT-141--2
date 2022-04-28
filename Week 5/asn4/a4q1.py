# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

i = 1
p2score = 0
p1score = 0
while True:
    if p1score == 3 or p2score ==3:
        break
    while True:
        if p1score == 3 or p2score ==3:
            break
        print ("Round "+str(i)+":" )
        while True:
            player1 = input("Player1, Hide Coin left or right hand? (l/r): ")
            if player1 == 'r' or player1 == 'l':
                break

        player2 = input("Player2, Guess! Left or right hand? (l/r): ")


        while True:
               if player2 == 'r' or player2 == 'l':
                break
               if player2 != 'l' or player2 != 'r':
                    player2 = input("Player2 , Please make a valid guess ! Left or right hand ? ( l / r ) : ")

        if player2 == player1:
            print("Player2, You guessed it correctly!")
            p2score = p2score + 1
        else :
            print("Player2, You guessed it wrong!")
            p1score = p1score + 1

        if p1score == 3:
            print("Player 1 wins!")

        if p2score ==3:
            print("Player 2 wins!")

        i = i + 1







