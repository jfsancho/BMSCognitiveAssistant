#  api_app/__init__.py

app = Flask(__name__, instance_relative_config=True)
# Load the default configuration
app.config.from_object('config')
# Load the configuration from the instance folder
app.config.from_pyfile('config.py')
