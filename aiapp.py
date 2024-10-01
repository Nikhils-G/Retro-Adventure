import openai  # Import OpenAI package
import random
from flask import Flask, request, jsonify, render_template
from game_multiverse import Player, quantum_choice  # Assuming your game_multiverse.py is imported here

app = Flask(__name__)

# Store player data globally
players = {}

# Add your OpenAI API key here
openai.api_key = 'your-openai-api-key-here'

# Function to generate AI-based responses
def get_ai_response(player_name, decision):
    prompt = f"{player_name} has decided to {decision}. Generate an alternate scenario with detailed storytelling."
    
    # OpenAI API call for generating response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response.choices[0].text.strip()

@app.route('/decision', methods=['POST'])
def make_decision():
    data = request.get_json()
    player_name = data['player_name']
    decision = data['decision']

    if player_name in players:
        player = players[player_name]
        
        # Get both a standard response and an AI-generated alternate response
        response, ripple_effect = quantum_choice(player, decision)
        ai_response = get_ai_response(player_name, decision)
        
        return jsonify({
            "response": response,
            "ripple_effect": ripple_effect,
            "ai_response": ai_response,  # Return the AI-generated response
            "health": player.health,
            "inventory": player.inventory,
            "allies": player.allies,
            "time_loops": player.time_loops,
            "achievements": player.path
        })
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
