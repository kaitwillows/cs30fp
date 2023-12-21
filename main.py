
import subprocess
import json
import os

os.system('cls')

while True:
    
    with open('scores.json', 'r') as file:
        scores = json.load(file)


    print("cool untitled game")
    print("==================")
    print(f"player wins: {scores['player']}")
    print(f"enemy wins: {scores['enemy']}")
    
    print("\nselect an option:")
    print("    [1] play game")
    print("    [2] quit game")
    print("    [3] reset scores")

    user_input = int(input(""))

    match user_input:
        case 1:
            os.system('cls')
            result = subprocess.run(['python', 'game_loop.py'], capture_output=True, text=True).returncode
            if result == 1:
                print("player won")
                scores['player'] += 1
            elif result == 2:
                print("enemy won")
                scores['enemy'] += 1
            
            with open('scores.json', 'w') as file:
                json.dump(scores, file)
            
        case 2:
            os.system('cls')
            print("thanks for playing")
            quit()
        case 3:
            os.system('cls')
            print("resetting scores...")

            scores['player'] = 0
            scores['enemy'] = 0

            with open('scores.json', 'w') as file:
                json.dump(scores, file)








# subprocess.run(['python', 'game_loop.py'])


print(scores['player'])
print(scores['enemy'])


with open('data.json', 'w') as file:
    json.dump(scores, file)

