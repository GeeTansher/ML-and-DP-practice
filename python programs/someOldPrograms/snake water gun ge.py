# by geetansh verma your subscriber
# SNAKE , WATER AND GUN GAME...

import random

print("\n\t\t\t\t\t\t\t\t\t@__WELCOME TO THE ROYAL GAME OF SNAKE, WATER AND GUN__@")
print(
    "HELP - You will play with computer in this arena. You will choose any one from snake , water and gun as yours weapon."
    "\n       Now acc. to the information of who will win over whom below the points of both computer and you will be taken."
    "\n         1. SNAKE =(WIN OVER)=> WATER"
    "\n         2. WATER =(WIN OVER)=> GUN"
    "\n         3. GUN =(WIN OVER)=> SNAKE"
    "\n       Game will be played 10 times and the winner will be decided..."
    "\n\t\t\t\t\t\t\t\t\t\t       !!!BEST OF LUCK!!!")
chance = 1
comp_po = 0
user_po = 0
game = ["SNAKE", "WATER", "GUN", "WATER", "SNAKE", "WATER", "SNAKE", "GUN", "WATER"]
game1 = {"S": "SNAKE", "W": "WATER", "G": "GUN"}
try:
    while chance <= 10:
        comp = random.choice(game)
        print(f"\nEnter your choice or weapon from:\n  1. S for {game[0]}\n  2. W for {game[1]}\n  3. G for {game[2]}")
        user1 = input()
        user = user1.upper()
        for key, value in game1.items():
            print(f"YOU ENTERED :{game1[user]}                         \t\t\t\t\t\t COMPUTER DECIDED :{comp}")
            if game1[user] == game[0] and comp == game[0]:
                print("It's a tie . No marks to anyone. Try hard again......")
            elif game1[user] == game[0] and comp == game[1]:
                print("HURRAH!! YOU WON. YOU GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                user_po = user_po + 1
            elif game1[user] == game[0] and comp == game[2]:
                print("SORRY!! COMPUTER WON. COMPUTER GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                comp_po = comp_po + 1
            elif game1[user] == game[1] and comp == game[0]:
                print("SORRY!! COMPUTER WON. COMPUTER GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                comp_po = comp_po + 1
            elif game1[user] == game[1] and comp == game[1]:
                print("It's a tie . No marks to anyone. Try hard again......")
            elif game1[user] == game[1] and comp == game[2]:
                print("HURRAH!! YOU WON. YOU GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                user_po = user_po + 1
            elif game1[user] == game[2] and comp == game[0]:
                print("HURRAH!! YOU WON. YOU GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                user_po = user_po + 1
            elif game1[user] == game[2] and comp == game[1]:
                print("SORRY!! COMPUTER WON. COMPUTER GOT A POINT . LET'S HOPE GOOD FOR NEXT TURN......")
                comp_po = comp_po + 1
            elif game1[user] == game[2] and comp == game[2]:
                print("It's a tie . No marks to anyone. Try hard again......")
            else :
                print("SORRY!! YOU ENTERED SOMETHING WRONG. PLEASE RESTART THE GAME......")
            break
        chance = chance + 1
        print(f"{10 - chance} left out of 10")
    print("\n\n\t\t\t\t\t\t      ...RESULTS TIME...")
    print(f"YOUR SCORE :{user_po} \t\t\t  COMPUTER'S SCORE :{comp_po} ")
    if user_po > comp_po :
        print("\nHURRAH!!! YOU GOT IT . YOU WON THE GAME . CONGRATULATIONS...\n\t\t\t YOU ARE TRULY A GENIUS...")
    elif comp_po > user_po :
        print(
            "\nSORRY!!! YOU LOST THE GAME . WELL TRIED . TRY MORE HARD NEXT TIME...\n\t\t\t YOU WILL TRULY BE A GENIUS ONE DA IN THIS...")
    else:
        print("WOW!!! AMAZING!!! YOU AND COMPUTER GOT A TIE . WELL DONE . HOPE TO WIN NEXT TIME . GOOD DAY THEN...")

except Exception as e:
    print("SORRY!! YOU ENTERED SOMETHING WRONG. PLEASE RESTART THE GAME......")