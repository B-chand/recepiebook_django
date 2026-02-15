from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, null=True, blank=True)

    #notes 1:
    #We use Django shell to interact with data and test database data quickly, while models are used only to define database structure.
    # we can use the following commands:python manage.py shell
    #objects here means the model manager, which is used to interact with the database. It provides methods to create, retrieve, update, and delete records in the database.
    #we dont need to save the object after creating it, because the create() method automatically saves the object to the database. However, if we create an object using the constructor (e.g., product = Product(name='Laptop', price=999.99)), we need to call product.save() to save it to the database.
    #to get all product details , we can use Product.objects.all()
    #product.objects.all()[0] will give us the first product in the database. We can access its attributes like product.objects.all()[0].name, product.objects.all()[0].price, etc.

    #note 2:
    # to get a students id we can use Student.objects.all()[0].id,
    # which will give us the id of the first student in the database.
    # We can also use Student.objects.get(id=1) to get the student with a specific id.
    
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()
    color = models.CharField(max_length=50)
    model_year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.car_name
