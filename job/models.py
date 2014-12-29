from django.db import models
from django.utils.encoding import smart_unicode
#from crew.models import *


# Create your models here.


LEVEL_CHOICES = (
	('ON', 'Level 1'),
	('TW', 'Level 2'),
	('TH', 'Level 3'),
)


DEPT_CHOICES = (
	('AS', 'Asphalt'),
        ('CR', 'Concrete'),
        ('SC', 'Seal Coat'),
        ('SS', 'Slurry Seal'),
        ('ST', 'Striping'),
)



class Job(models.Model):
	job_number		= models.CharField(max_length=12, unique=True)
	slug			= models.SlugField(unique=True)
	department		= models.ForeignKey('Department')
	job_name		= models.CharField(max_length=200)
	city			= models.CharField(max_length=100)
	map_address		= models.CharField(max_length=200, help_text='Input like: City, Street Address')
	level			= models.CharField(max_length=2, choices=LEVEL_CHOICES)
	job_date		= models.DateField()
	contact_phone           = models.BigIntegerField()
	go_back			= models.BooleanField(default=False)
	touch_up		= models.BooleanField(default=False)
	job_desc		= models.TextField(blank=True)

	def __unicode__(self):
		return self.slug


class Department(models.Model):
	name			= models.CharField(max_length=50)
	slug			= models.SlugField(unique=True)

        def __unicode__(self):
                return self.name
