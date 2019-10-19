from Database import db, Puppy

#creates all the tables to a db table
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',6)

# these should print none because these arent added to database yet
print(sam.id)
print(frank.id)


#this line adds the names to the database
db.session.add_all([sam,frank])


db.session.commit()

# After adding to the database the id's should be different
print(sam.id)
print(frank.id)
