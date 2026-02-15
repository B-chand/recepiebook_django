from home.models import Student
import time

def run_this_function():
    print("This function is running...")
    time.sleep(1)  # Simulating a long-running task
    print("Function has completed.")

    #shell is also used if we are using resources from another file, 
    # we can import that file and use its functions or classes.
    # For example, if we want to use the Student model from models.py,
    # we can import it in this utils.py file and then use it to interact with the database.
    # We can create new student records, retrieve existing records, update records, or delete records using the Student model.