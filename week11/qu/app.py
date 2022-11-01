import os
from Tasks import create_app , db

app = create_app()

# run server 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # PORT= int(os.environ.get('PORT', 5000))
    app.run(debug=True)