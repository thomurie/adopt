from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

dog_url = 'https://www.thefarmersdog.com/digest/wp-content/uploads/2020/07/Bowie_December-768x918.jpg'
cat_url = 'https://mymodernmet.com/wp/wp-content/uploads/2020/10/maine-coon-cats-7.jpg'
porcupine_url = 'https://www.meigspointnaturecenter.org/wp-content/uploads/2020/05/nature-3588682_1280-1024x662.jpg'

dog = Pet(name= 'Fido', species = 'Dog', photo_url = dog_url, age = 6, notes = "mellow, cheerful, older lady", available = True)

cat = Pet(name= 'Mary', species = 'Cat', photo_url = cat_url, age = 6, notes = "mellow, cheerful, older man", available = True)

porcupine = Pet(name= 'Spikey', species = 'Porcupine', photo_url = porcupine_url, age = 6, notes = "mellow, cheerful, young lady", available = True)

db.session.add(dog)
db.session.add(cat)
db.session.add(porcupine)

db.session.commit()