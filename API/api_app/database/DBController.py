
"""
from sqlalchemy import create_engine
import cx_Oracle

host=hostname
port=port
sid='sid'
user='username'
password='password'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

result = engine.execute('select * from TABLE')
"""

class DBController:


    def __init__(self):
