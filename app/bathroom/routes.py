from flask import Blueprint, request

bathroom_bp = Blueprint('bathroom', __name__, url_prefix='/api/v1/bathroom')


@bathroom_bp.route("/sinks", methods=['GET'])
def sinks():
    if request.method == 'GET':
        pass