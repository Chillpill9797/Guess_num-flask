from flask import Flask, render_template, request
from random import choice
from replit import db

app = Flask(__name__)

if 'guesses' not in db:
  db['guesses']=[]
if 'comuter_number' not in db:
  db['computer_number']=choice(range(1,101))


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    guess=int(request.form['number_guess'])
    message=check_number_show_message(guess, db['computer_number'])
    db['guesses'].append(message)
    print(db['computer_number'])
    print(db['guesses'])
  return render_template('index.html', guesses=reversed(db['guesses']))
@app.route('/reset')
def reset():
  db['computer_number']=choice(range(1,101))
  db['guesses']=[]
  return render_template('index.html', guesses=db['guesses']) 
def check_number_show_message(guess_number, computer_number):
  if guess_number<computer_number:
    return f"{guess_number} is too low!"
  elif guess_number>computer_number:
    return f"{guess_number} is too high!"
  else:
    return f"{guess_number} is correct!"
print(check_number_show_message(5,50))    
  
app.run(host='0.0.0.0', port=81)
