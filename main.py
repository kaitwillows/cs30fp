import subprocess
import json

# subprocess.run(['python', 'game_loop.py'])

with open('scores.json', 'r') as file:
    scores = json.load(file)

print(scores['player'])
print(scores['enemy'])


with open('data.json', 'w') as file:
    json.dump(scores, file)

