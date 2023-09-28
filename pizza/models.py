from django.db import models

# Create your models here.
class pizzas(models.Model):
    name = models.CharField(max_length=20)
    actual_price = models.IntegerField()
    discounted_price = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=10)
    discount = models.IntegerField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name