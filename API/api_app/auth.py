

import functools

from flask import (
    Blueprint, request, session, url_for, g, redirect, jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=["POST", "GET"])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        session.clear()
        session['user_id'] = username #is a dictionary that stores data across requests.
        #return redirect(url_for('request.makeRequest'))
        return jsonify( {"Respuesta": "successful login", "username": username})
    else:
        return jsonify( {"Respuesta": "you have to login first"})



@bp.route('/logout')
def logout():
    session.clear() #clear the info of the previous user session
    return '{"Respuesta": "success log out"}'

@bp.before_app_request  #registers a function that runs before the view function, no matter what URL is requested.
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None # it uses g to store important data in cache
    else:
        #g.user = getUserFromDB(user_id)
        g.user=user_id #para prueba


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            print(g.user)

        return view(**kwargs)

    return wrapped_view
