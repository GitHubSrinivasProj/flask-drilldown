## This file is used to create the entries in the database
# this is trhe separate file and will import the models.py in the file inorder
# to create the instance of the class we created

from Models import db,Puppy,Owner,Toy

#creating two puppies

rufus = Puppy('Rufus')
sam = Puppy('Sammy')

# Add puppies to db

db.session.add_all([rufus,sam])
db.session.commit()

# check on this without the owner
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

#create owner object for rufus
shri = Owner('Shri',rufus.id)

#give some toys
toy1 = Toy('chew toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

# add to the database
db.session.add_all([shri,toy1,toy2])
db.session.commit()


#grab rufus after the addition of owner and toys
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()
