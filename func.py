from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from models import db, books, users


def welcome():
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)
    if userstate is not None:
        response = render_template('welcome_back', title=userstate.book, page=userstate.sentence + 1)
    else:
        response = render_template('welcome', title=books.default_book)
        users.create_user_state(user_id, books.default_book)

    return question(response)


def set_level(level=0):
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)
    users.set_level(userstate, level)
    response = render_template('level_updated', level=level)

    return question(response)


def read_next_sentence(update_state=True, shift=0, languages=[]):
    user_id = session.user.userId

    userstate = users.get_user_state(user_id)

    sentence_id = userstate.sentence
    sentence = books.get_sentences()[sentence_id + shift]

    if languages == []:
        reader = 'read_sentence_beginner'
        if userstate.level == 2:
            reader = 'read_sentence_intermediate'
        if userstate.level == 3:
            reader = 'read_sentence_advanced'
        response = render_template(reader, de=sentence['de'], en=sentence['en'])
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
