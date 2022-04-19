from flask import jsonify, request
from flask.views import MethodView
from flask import abort
from werkzeug import Response
from models import AdvModel
from settings import db


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
                'status': 'Deleted'
            })
        return jsonify({
            'status': 'Not Deleted'
        })
