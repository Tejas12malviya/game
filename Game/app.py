from flask import Flask, render_template, request, jsonify
import random
import socket

app = Flask(__name__)

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
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f' * Local network URL: http://{local_ip}:5000')
    app.run(host='0.0.0.0', port=5000)