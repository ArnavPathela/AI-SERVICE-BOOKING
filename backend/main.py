from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
from models import db 
db.init_app(app)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    
    app.run(debug=True)
