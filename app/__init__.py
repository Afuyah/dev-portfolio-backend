


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# Initialize the extensions without binding to the app yet
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mail = Mail()
jwt = JWTManager()

def create_app(config_class=Config):
    # Create the Flask app instance
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    mail.init_app(app)
    jwt = JWTManager(app)

    # Import and register blueprints
    from app.routes.experience import bp as experience_bp
    from app.routes.skills import bp as skills_bp
    from app.routes.projects import bp as projects_bp
    from app.routes.contact import bp as contact_bp
    from app.routes.login import bp as login_bp
    from app.routes.register import bp as register_bp
    from app.routes.admin import bp as admin_bp


    app.register_blueprint(login_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(register_bp)
    
    app.register_blueprint(admin_bp)
    
    # Default route (for testing)
    @app.route('/')
    def home():
        return {"message": "Portfolio Backend API"}

    return app

