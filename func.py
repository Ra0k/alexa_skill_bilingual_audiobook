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


def read_next_sentence():
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)

    sentence_id = userstate.sentence
    sentence =  books.get_sentences()[sentence_id]

    response = render_template('read_sentence', de=sentence['de'].split(' '), en=sentence['en'])
    want_countinue = render_template('want_countinue')

    users.next_sentence(userstate)

    return question(response).reprompt(want_countinue)