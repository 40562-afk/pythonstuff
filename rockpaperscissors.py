import random
import sys
player_points = 0
robot_points = 0
def game():
    global player_points, robot_points

    for attemps in range(3):
        print("\n\natempts made: " + str(attemps) + "/3")
        
        print("1 is for rock")
        print("2 is for paper")
        print("3 is for scissors")
        print("4 is for quitting losers")

        user_input = int(input("\n\nrock paper scissors shoot!: "))

        if user_input != 1 and user_input != 2 and user_input != 3:
            print("not 1 2 or 3")
            continue
        elif user_input == 1:
            print("player: rock")
        elif user_input == 2:
            print("player: paper")
        elif user_input == 3:
            print("player: scissors")
        elif user_input == 4:
            break

        rand_num = random.randint(1, 3)
        if rand_num == 1:
            print("chatGPT: rock")
        elif rand_num == 2:
            print("chatGPT: paper")
        elif rand_num == 3:
            print("chatGPT: scissors")

        if user_input == rand_num:
            print("tie")
        elif user_input == 1 and rand_num == 2:
            print("robo wins")
            robot_points += 1
        elif rand_num == 1 and user_input == 2:
            print("player wins")
            player_points += 1
        elif user_input == 1 and rand_num == 3:
            print("player wins")
            player_points += 1
        elif rand_num == 1 and user_input == 3:
            print("robo wins")
            robot_points += 1
        elif user_input == 2 and rand_num == 3:
            print("robo wins")
            robot_points += 1 
        elif rand_num == 2 and user_input == 3:
            print("player wins")
            player_points += 1
    win_lose()
    play_again()

  
def win_lose():
    if robot_points > player_points:
        print("robot wins: ", robot_points, "points")
    elif player_points > robot_points:
        print("player wins: ",  player_points, "points")
    else:
        print("tie")

def play_again():
    print("play again?")
    user_input = input("y/n: ")
    if user_input == "y":
        game()
    elif user_input == "n":
        sys.quit()
    else:
        print("not y or n")
game()



