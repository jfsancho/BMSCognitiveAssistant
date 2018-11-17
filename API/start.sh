# start.sh
#linux
export FLASK_APP=./api_app/__init__.py
#export FLASK_ENV=development
#export APP_CONFIG_FILE=/var/www/yourapp/config/production.py

#windows
#run with sh in GIT BASH PROMPT
flask run -h 0.0.0.0 #run our Flask application listening to all interfaces on the computer (-h 0.0.0.0).
