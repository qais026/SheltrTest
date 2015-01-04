from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Provider(models.Model):
	admin = models.ForeignKey(User) # This is what I just typed
	admin_firstname2 = models.CharField(max_length=45, null=True, blank=True)
	admin_lastname2 = models.CharField(max_length=45, null=True, blank=True)
	name = models.CharField(max_length=140)
	logo = models.CharField(max_length=140, null=True, blank = True)
	URL = models.CharField(max_length=140)
	street = models.CharField(max_length=140)
	city = models.CharField(max_length=60)
	zipcode = models.CharField(max_length=10)
	latitude = models.FloatField(default=0, null=True, blank=True)
	longitude = models.FloatField(default=0, null=True, blank=True)
	#Fill in later with the necessary fields from the CSV/Excel
	characteristics = models.CharField(max_length=500)


	def __unicode__(self):
		return self.name