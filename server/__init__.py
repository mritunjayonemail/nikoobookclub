from flask import Flask, session
from server.book_club_server import book_club_bp
from datetime import timedelta
from common.util import get_logger
from uuid import uuid4

app = Flask(__name__, template_folder='../web/templates', static_folder='../web/static')
app.secret_key = str(uuid4())

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)

app.register_blueprint(book_club_bp)