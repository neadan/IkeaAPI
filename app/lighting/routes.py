from flask import Blueprint, request, Response, jsonify

from app.models import Lamp, db

lighting_bp = Blueprint('lighting', __name__, url_prefix='/api/v1/lighting')


@lighting_bp.route("/lamps", methods=['GET', 'POST'])
def lamps():
    if request.method == 'GET':
        return "blabla"
    if request.method == 'POST':
        data = request.form
        lamp_to_add = Lamp(brand=data['brand'], name=data['name'], year=data['year'], price=data['price'])
        db.session.add(lamp_to_add)
        db.session.commit()
        response = Response(status=200)
        response.headers['location'] = f"lamps/{lamp_to_add.id}"
        return response


@lighting_bp.route("/lamps/<int:lamp_id>", methods=['GET'])
def get_lamp_id(lamp_id):
    if request.method == 'GET':
        lamp = Lamp.query.get(lamp_id)
        return jsonify(lamp.to_dict())
