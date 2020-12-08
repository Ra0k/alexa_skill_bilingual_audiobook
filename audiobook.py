from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from models import db

import func
import logging


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://audiobook:audiobook1234@167.99.243.10/audiobook'
db.init_app(app)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def welcome():
    return func.welcome()


@ask.intent("AMAZON.ResumeIntent")
def resume_intent():
    return func.read_next_sentence()


@ask.intent("ContinueIntent")
def next_round():
    return func.read_next_sentence()


#@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
#def answer(first, second, third):
#    winning_numbers = session.attributes['numbers']
#    if [first, second, third] == winning_numbers:
#        msg = render_template('win')
#    else:
#        msg = render_template('lose')
#
#    return statement(msg)


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    fallback = render_template('fallback')
    want_countinue = render_template('want_countinue')
    return question(fallback).reprompt(want_countinue)


@app.before_first_request
def initialize_database():
    db.create_all()


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True, port=5000)
