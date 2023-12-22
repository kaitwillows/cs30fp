
import subprocess
import json
import os


os.system('cls')
print("\n")

while True:
    
    with open('scores.json', 'r') as file:
        scores = json.load(file)


    print("welcome to untitled shoot game")
    print("==============================")
    print(f"player wins: {scores['player']}")
    print(f"enemy wins: {scores['enemy']}")
    
    print("\nselect an option:")
    print("    [1] play game")
    print(f"    [2] set screen resolution (currently ({scores['resolution_x']} x {scores['resolution_y']}))")
    print("    [3] reset scores")
    print("    [4] quit game")

    try:
        user_input = int(input(""))
    except:
        user_input = -1
        os.system('cls')
        print("please enter the number that corresponds to your selection (1, 2, 3, or 4)\n")

    match user_input:
        case 1: # play game
            os.system('cls')
            result = subprocess.run(['python', 'game_loop.py'], capture_output=True, text=True).returncode # exit codes are returned as a result of gameplay
            if result == 1:
                print("game window was closed\n")
            elif result == 2:
                print("enemy won :(\n")
                scores['enemy'] += 1
            elif result == 3:
                print("player won!!!\n")
                scores['player'] += 1
            
            with open('scores.json', 'w') as file:
                json.dump(scores, file)
        case 2: # set resolution
            os.system('cls')
            try:
                scores['resolution_x'] = int(input("set your x resolution (in pixels): "))
                scores['resolution_y'] = int(input("set your y resolution (in pixels): "))
                with open('scores.json', 'w') as file:
                    json.dump(scores, file)
                os.system('cls')
                print("set resolution successfully\n")
            except:
                os.system('cls')
                print("input was not a number, please try again\n")
        case 3: # reset scores
            os.system('cls')

            scores['player'] = 0
            scores['enemy'] = 0

            with open('scores.json', 'w') as file:
                json.dump(scores, file)

            print("scores reset\n")
        case 4: # quit
            os.system('cls')
            print("thanks for playing")
            quit()
        case _: # default case (invalid input)
            os.system('cls')
            print("please enter the number that corresponds to your selection (1, 2, 3, or 4)\n")
