from django.db import models

# Create your models here.

# model for food item details   
class Fooditem(models.Model):
    food_type = models.CharField(max_length = 30)
    description = models.TextField()
    item_name = models.CharField(max_length = 200, default=None,null=True)
    item_price = models.FloatField(null=True)

    def __str__(self):
        return self.food_type
    
# model for customer Contact
class CustContact(models.Model):
    cust_name=models.CharField(max_length=30)
    cust_email=models.CharField(max_length=50)
    cust_contact=models.IntegerField()
    fooditem=models.ForeignKey(Fooditem, on_delete=models.CASCADE)
    help=models.TextField()

    def __str__(self):
        return self.cust_name

# model for Feedback
class Feedback(models.Model):
    username=models.CharField(max_length=30)
    created_date=models.DateTimeField(auto_now_add=True)
    feedback=models.TextField()

    def __str__(self):
        return self.username
# model for supervisor
class Supervisor(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

