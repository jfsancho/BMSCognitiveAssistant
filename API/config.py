
DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com" # For use in application emailsration variables via app.config["VAR_NAME"].

"""
The config.py file should contain one variable assignment per line.
When your app is initialized, the variables in config.py are used to configure
Flask and its extensions are accessible via the app.config dictionary – e.g. app.config["DEBUG"]
"""

SQLALCHEMY_ECHO = True
