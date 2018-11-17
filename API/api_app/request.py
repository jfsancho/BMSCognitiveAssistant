from flask import (
    Blueprint, request, session, url_for, jsonify
)
from .auth import login_required

bp = Blueprint('request', __name__, url_prefix='/request')

@bp.route('/',methods =["POST", "GET"])
@login_required
def makeRequest():
    if request.method == 'POST':
        text=request.form['solicitud']
        return jsonify({"Respuesta": text})
    else:
        return jsonify({"Respuesta": "request"})
