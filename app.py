from flask import Flask, request, jsonify, render_template
from game_multiverse import Player, quantum_choice

app = Flask(__name__)

# Dictionary to keep track of players
players = {}

@app.route('/')
def home():
    return render_template('index.html')  # Serve the index.html file

@app.route('/game', methods=['POST'])
def create_game():
    data = request.get_json()
    player_name = data['player_name']
    player = Player(player_name)
    players[player_name] = player
    return jsonify({
        "message": f"Welcome, {player_name}!",
        "health": player.health,
        "inventory": player.inventory,
        "allies": player.allies,
        "time_loops": player.time_loops
    })

@app.route('/select_character', methods=['POST'])
def select_character():
    data = request.get_json()
    player_name = data.get('player_name')  # Get the player name from the request
    character_class = data.get('character_class')  # Get the selected character class

    if player_name in players:
        player = players[player_name]
        player.choose_class(character_class)  # Set the player's character class
        return jsonify({"message": f"You have selected the {character_class} class!"})
    else:
        return jsonify({"error": "Player not found"}), 404

@app.route('/decision', methods=['POST'])
def make_decision():
    data = request.get_json()
    player_name = data['player_name']  # Get the player name from the request
    decision = data['decision']

    if player_name in players:
        player = players[player_name]
        response, ripple_effect = quantum_choice(player, decision)
        return jsonify({
            "response": response,
            "ripple_effect": ripple_effect,
            "health": player.health,
            "inventory": player.inventory,  # Return inventory
            "allies": player.allies,        # Return allies
            "time_loops": player.time_loops,
            "achievements": player.path      # Send achievements back to the frontend
        })
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
