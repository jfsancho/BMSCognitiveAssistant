from flask import (
    Blueprint, request, session, url_for, g
)

bp = Blueprint('request', __name__, url_prefix='/request')

@app.route('/',methods =('POST'))
def makeRequest():
    return "request"
