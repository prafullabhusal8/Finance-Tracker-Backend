from flask import Flask
from models import db
from routes.api_routes import api_bp
from routes.web_routes import web_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

# Register Blueprints
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
