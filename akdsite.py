from webapp import app, db
from webapp.models import Watchables, Status, Episodes


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Watchables': Watchables, 'Status': Status, 'Episodes': Episodes}
