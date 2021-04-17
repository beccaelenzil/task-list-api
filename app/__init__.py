from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/tasks_list_api_development'    
    else:
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/tasks_list_api_test'    
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import tasks_bp, goals_bp, root_bp
    app.register_blueprint(tasks_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(root_bp)

    from .routes import root_bp
    app.register_blueprint(root_bp)

    with app.app_context():
        db.create_all()

    return app
