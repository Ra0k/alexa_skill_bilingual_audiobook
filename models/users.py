from . import db

class UserState(db.Model):
    user_id  = db.Column(db.String(256), primary_key=True, nullable=False)
    book     = db.Column(db.String(256), primary_key=True, nullable=False)
    sentence = db.Column(db.Integer, nullable=False, default=0)
    level    = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<UserState %r>' % self.username


def get_user_state(user_id):
   return UserState.query.filter_by(user_id=user_id).first()

def create_user_state(user_id, book):
    new_user = UserState(user_id=user_id, book=book, sentence=0, level=0)
    db.session.add(new_user)
    db.session.commit()

    return new_user

def next_sentence(userstate):
    userstate.sentence += 1
    db.session.add(userstate)
    db.session.commit()

    return userstate


def set_level(userstate, level=0):
    userstate.level = level
    db.session.add(userstate)
    db.session.commit()

    return userstate