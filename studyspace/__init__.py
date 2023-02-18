import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (studyspace/config.py)
app.config.from_object('studyspace.config')

import studyspace.views
