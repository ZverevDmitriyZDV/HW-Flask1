from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.views import MethodView
from datetime import datetime
from flask import abort
from werkzeug import Response

PG_DSN = 'postgresql://admin:1234@127.0.0.1:5431/flask_test'
app = Flask('test_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdvModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(64), index=True, unique=True)
    owner = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    date_created = db.Column(db.DateTime(), default=datetime.today().strftime('%Y-%m-%d'))


class AdvView(MethodView):

    def get(self, id_needed):
        result = []
        if id_needed is None:
            instance = db.session.query(AdvModel).all()
        else:
            instance = [db.session.query(AdvModel).get(id_needed)]

        if instance is []:
            return jsonify({'result': None})

        for elem in instance:
            result.append({
                'id': elem.id,
                'header': elem.header,
                'data_created': elem.date_created,
                'owner': elem.owner,
                'description': elem.description
            })
        return jsonify(result)

    def post(self):
        new_adv = AdvModel(**request.json)
        db.session.add(new_adv)
        db.session.commit()
        return jsonify({
            'id': new_adv.id,
            'header': new_adv.header,
            'data_created': new_adv.date_created,
            'owner': new_adv.owner,
            'description': new_adv.description
        })

    def delete(self, id_needed):
        instance = db.session.query(AdvModel).get(id_needed)
        if instance is None:
            return abort(Response('ERROR 404 No such data! Check your input data', 404))
        db.session.query(AdvModel).filter_by(id=id_needed).delete()
        db.session.commit()
        if db.session.query(AdvModel).get(id_needed) is None:
            return jsonify({
                'status':'Deleted'
            })
        return jsonify({
            'status': 'Not Deleted'
        })


adv_view = AdvView.as_view('adv_api')

app.add_url_rule('/advs/', defaults={'id_needed': None},
                 view_func=adv_view, methods=['GET', ])
app.add_url_rule('/advs/', view_func=adv_view, methods=['POST', ])
app.add_url_rule('/advs/<int:id_needed>', view_func=adv_view,
                 methods=['GET', 'DELETE'])

app.run(host='0.0.0.0', port=8080)
