from flask import render_template, session, jsonify, request
from .forms import SimpleForm
from .models import SimpleModel, CountModel
from app import app, db


@app.route('/index')
def index():
    form = SimpleForm(request.form)
    strings = SimpleModel.query.all()

    if CountModel.query.all():
        count = CountModel.query.get(1)
        count.counter += 1
    else:
        count = CountModel(counter=0)

    db.session.add(count)
    db.session.commit()

    return render_template('index.html', strings=strings,
                           form=form, count=count)


@app.route('/form', methods=['POST'])
def post():

    form = SimpleForm(request.form)

    if form.validate_on_submit():
        try:
            string = SimpleModel(string=request.form['inputer'])

            db.session.add(string)
            db.session.commit()

            data = {'status': 1, 'message': 'String added {}.' \
                    .format(form.inputer.data)}
        except Exception as e:
            data = {'status': 2, 'message': "{}".format(repr(e))}
    else:
            data = {'status': 0, 'message': 'Validation faild! {}'\
                    .format(form.inputer.errors[0])}
    return jsonify(data)

@app.route('/delete/<forDel>', methods=['DELETE'])
def delete(forDel):
    data = {'status': 0, 'message': 'Error'}

    try:
        db.session.query(SimpleModel).filter_by(id=forDel).delete()
        db.session.commit()
        data = {'status': 1, 'message': 'String deleted'}

    except Exception as e:
        data = {'status': 0, 'message': repr(e)}

    return jsonify(data)
