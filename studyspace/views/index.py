import flask
import studyspace

@studyspace.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)


# this is where ping.py will hit and analysis.py will get triggered
@studyspace.app.route('/api/update_connections/', methods=['POST'])
def update_connections():
    result = {"status": "success"}
    
    return flask.jsonify(**result), 201
    


