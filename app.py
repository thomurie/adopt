from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import NewPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

# ROUTES

@app.route('/', methods = ['GET'])
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets = pets)

@app.route('/add', methods = ['GET', 'POST'])
def new_pet_form():
    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} to pets")
        return redirect('/')
    else:
        return render_template('add_form.html', form = form)

@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def edit_pet_form(pet_id):
    form = EditPetForm()

    pet = Pet.query.filter_by(id = pet_id).first()

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name}")
        return redirect('/')

    else:
        return render_template('edit_post.html', pet = pet, form = form)



