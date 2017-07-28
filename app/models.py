from app import app, db


class SimpleModel(db.Model):
    __tablename__ = 'SimpleModel'
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(20))

    def __init__(self, string, **kwargs):
        db.Model.__init__(self, string=string, **kwargs)

    def __repr__(self):
        return '<SimpleModel {}, {}>'.format(self.id, self.string)


class CountModel(db.Model):
    __tablename__ = 'CountModel'
    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer)

    def __init__(self, counter, **kwargs):
        db.Model.__init__(self, counter=counter, **kwargs)

    def __repr__(self):
        return '<CountModel {}>'.format(self.counter)
