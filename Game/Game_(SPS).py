from flask import Flask, render_template, request, jsonify, url_for
import random
import os
from pyngrok import ngrok

app = Flask(__name__)

# Add static folder configuration
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    comp_choice = random.choice(['Stone', 'Paper', 'Scissors'])
    
    result = f"Computer chose: {comp_choice}<br>"
    winner = None
    
    if user_choice == comp_choice:
        result += "It's a tie!"
    elif ((user_choice == 'Stone' and comp_choice == 'Scissors') or
          (user_choice == 'Paper' and comp_choice == 'Stone') or
          (user_choice == 'Scissors' and comp_choice == 'Paper')):
        result += "You won!"
        winner = 'user'
    else:
        result += "Computer won!"
        winner = 'computer'
    
    return jsonify({
        'result': result, 
        'winner': winner,
        'computerChoice': comp_choice.lower()
    })

if __name__ == '__main__':
    # Create a tunnel to port 5000
    public_url = ngrok.connect(5000)
    print(f' * Public URL: {public_url}')
    app.run(host='0.0.0.0', port=5000, debug=False)