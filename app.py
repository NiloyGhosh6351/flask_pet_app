from flask import Flask, render_template, redirect, url_for  # type: ignore
from models import db, Pet  # type: ignore
from forms import PetForm  # type: ignore

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'Niloy'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('index'))
    
    pets = Pet.query.all()
    return render_template('view_pets.html', form=form, pets=pets)

# Create database tables before running the app
with app.app_context():
    db.create_all()

if __name__ == '_main_':
    app.run(debug=True)