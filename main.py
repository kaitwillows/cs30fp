
import subprocess
import json
import os

os.system('cls')

while True:
    
    with open('scores.json', 'r') as file:
        scores = json.load(file)


    print("welcome to untitled shoot game")
    print("==============================")
    print(f"player wins: {scores['player']}")
    print(f"enemy wins: {scores['enemy']}")
    
    print("\nselect an option:")
    print("    [1] play game")
    print("    [2] reset scores")
    print("    [3] quit game")

    user_input = int(input(""))

    match user_input:
        case 1:
            os.system('cls')
            result = subprocess.run(['python', 'game_loop.py'], capture_output=True, text=True).returncode
            if result == 1:
                print("enemy won :(\n")
                scores['enemy'] += 1
            elif result == 2:
                print("player won!!!\n")
                scores['player'] += 1
            
            with open('scores.json', 'w') as file:
                json.dump(scores, file)
        case 2:
            os.system('cls')
            print("resetting scores...")

            scores['player'] = 0
            scores['enemy'] = 0

            with open('scores.json', 'w') as file:
                json.dump(scores, file)
        case 3:
            os.system('cls')
            print("thanks for playing")
            quit()








# subprocess.run(['python', 'game_loop.py'])


print(scores['player'])
print(scores['enemy'])


with open('data.json', 'w') as file:
    json.dump(scores, file)

