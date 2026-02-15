#why do we do migrations?
# #Migrations are a way to propagate changes you make to your models (adding a field, deleting)
#migration knows about thte changes made in the schema by running the migrations internally, creates a state and,
#then compares the state and actual database and then creates a migration file which contains the changes that need to be made to the database to match the new state of the models.
