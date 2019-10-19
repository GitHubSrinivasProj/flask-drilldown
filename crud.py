from Database import db, Puppy

## create ##

my_puppy = Puppy('Snoopy',6)
db.session.add(my_puppy)
db.session.commit()


## Read ##
# using the ORM filter operations

#returns the list of all the puppies existing in the database
all_puppies = Puppy.query.all()
print(all_puppies)

## select by id ##
puppy_one = Puppy.query.get(1)
print(puppy_one)

## filtering out ##
# produce the SQL code for us
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
print(puppy_frankie.all())

########## Updating ##########

first_puppy = Puppy.query.get(1)
first_puppy.age = 20
db.session.add(first_puppy)
db.session.commit()


########### deleting ##########

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


###
all_puppies = Puppy.query.all()
print(all_puppies)
