from django.db import models

# Create your models here.
class PurchasedCourse(models.Model):
    braintree_id = models.CharField(max_length=150, blank=True)