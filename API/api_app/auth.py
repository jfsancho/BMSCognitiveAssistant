

import functools

from flask import (
    Blueprint, request, session, url_for, g
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=('POST'))
def login():

    #if user is None:
    #    error = 'Incorrect username.'
    #elif not check_password_hash(user['password'], password):
    #    error = 'Incorrect password.'
    #if error is None:
    #    session.clear()
    #    session['user_id'] = user['id'] #is a dictionary that stores data across requests.
    #    return "not login"

    return "login"

@bp.route('/logout')
def logout():
    session.clear() #clear the info of the previous user session
    return "success log out"

@bp.before_app_request  #registers a function that runs before the view function, no matter what URL is requested.
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None # it uses g to store important data in cache
    else:
        #g.user = getUserFromDB(user_id)
        g.user='1111' #para prueba



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
