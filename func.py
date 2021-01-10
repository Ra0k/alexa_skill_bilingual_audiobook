from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from models import db, books, users


def welcome():
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)
    if userstate is not None:
        response = render_template('welcome_back', page=userstate.sentence + 1)
    else:
        response = render_template('welcome')
        users.create_user_state(user_id, 'Harry Potter and the Philosopher\'s Stone')

    return question(response)


def read_next_sentence(update_state=True, shift=0, languages=[]):
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)

    sentence_id = userstate.sentence
    sentence = books.get_sentences()[sentence_id + shift]

    if languages == []:
        response = render_template('read_sentence', de=sentence['de'], en=sentence['en'])
    else:
        de, en = None, None
        if 'de' in languages:
            de = sentence['de']
        if 'en' in languages:
            en = sentence['en']

        response = render_template('repeat_sentence', de=de, en=en)

    if update_state:
        users.next_sentence(userstate)

    want_countinue = render_template('want_countinue')
    return question(response).reprompt(want_countinue)
