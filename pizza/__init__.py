from utils import app, db, migrate


def create_app():
    db.init_app(app)
    migrate.init_app(app)

    return app
