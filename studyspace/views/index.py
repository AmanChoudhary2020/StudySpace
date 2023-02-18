import flask
import studyspace

@studyspace.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)


@studyspace.app.route('/api/update_connections/', methods=['POST'])
def update_connections():
    result = {"status": "success"}
    return flask.jsonify(**result), 201
    


