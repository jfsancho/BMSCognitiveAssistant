import sys
import traceback
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine('mysql://root:Sancho16@localhost:3306/bmscognitiveassistant')
except Exception:
    print(traceback.format_exc())
    


Session = sessionmaker(bind=engine)

Base = declarative_base()
