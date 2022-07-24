from django.db import models
from django.urls import reverse
# Create your models here.

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  age = models.IntegerField()
  
  def __str__(self):
    return f'Dog named {self.name}. Breed: {self.breed}. Age of: {self.age} '

  def get_absolute_url(self):
    return reverse('detail', kwargs={'dog_id': self.id})

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"