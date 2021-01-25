from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from models import db

import os
import func
import logging


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['audiobook_db']
db.init_app(app)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def welcome():
    return func.welcome()


@ask.intent("AMAZON.ResumeIntent")
def resume_intent():
    while session.attributes.get('TASK') == 'REPEAT':
        shift = session.attributes.get('MESSAGE', {}).get('SHIFT')
        languages = session.attributes.get('MESSAGE', {}).get('LANGUAGES')
        if shift == 0:
            session.attributes.pop('MESSAGE', None)
            session.attributes.pop('TASK', None)
            break
        session.attributes['MESSAGE']['SHIFT'] = shift+1
        return func.read_next_sentence(update_state=False, shift=shift, languages=languages)
    return func.read_next_sentence()


@ask.intent("ReadyIntent")
def next_intent():
    while session.attributes.get('TASK') == 'REPEAT':
        shift = session.attributes.get('MESSAGE', {}).get('SHIFT')
        languages = session.attributes.get('MESSAGE', {}).get('LANGUAGES')
        if shift == 0:
            session.attributes.pop('MESSAGE', None)
            session.attributes.pop('TASK', None)
            break
        session.attributes['MESSAGE']['SHIFT'] = shift+1
        return func.read_next_sentence(update_state=False, shift=shift, languages=languages)
    return func.read_next_sentence()


@ask.intent("RepeatIntent", convert={'shift': int})
def repeat(shift, language, *arg, **argv):
    print(shift, language, *arg, **argv)
    language_mapping = {
        'german': 'de',
        'english': 'en'
    }

    if shift == None: shift = 1
    shift = -1 * shift

    languages = []
    if isinstance(language, str): 
        if language.lower() in language_mapping:
            languages.append(language_mapping[language.lower()])
    elif isinstance(language, list):
        languages = []
        for lang in list(language):
            if lang.lower() in language_mapping:
                languages.append(language_mapping[lang.lower()])

    session.attributes['TASK'] = 'REPEAT'
    session.attributes['MESSAGE'] = {'SHIFT': shift+1, 'LANGUAGES': languages}

    return func.read_next_sentence(update_state=False, shift=shift, languages=languages)


@ask.intent("ChangeLevelToEasyIntent")
def next_intent():
    return func.set_level(1)


@ask.intent("ChangeLevelToIntermediateIntent")
def next_intent():
    return func.set_level(2)


@ask.intent("ChangeLevelToAdvancedIntent")
def next_intent():
    return func.set_level(3)


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
