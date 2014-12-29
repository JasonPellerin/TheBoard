from django.db import models
from django.utils.encoding import smart_unicode
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from job.models import Department

# Create your models here.


LANG_CHOICES = (
	('EN', 'English'),
	('ES', 'Espanol'),
)


class Crew(models.Model):
	user		= models.OneToOneField(User, related_name="profile")
	first_name	= models.CharField(max_length=75)
	last_name      	= models.CharField(max_length=75)
	nickname      	= models.CharField(max_length=75, blank=True)
	phone		= models.BigIntegerField()
	department	= models.ForeignKey('job.Department', default='')
	lang		= models.CharField(max_length=2, choices=LANG_CHOICES)
	superint	= models.BooleanField(default=False)
	foreman		= models.BooleanField(default=False)
	estimator	= models.BooleanField(default=False)
	sales_rep	= models.BooleanField(default=False)
	crew_pic        = models.ImageField(upload_to="images/crewthumbs/")
	


	def __unicode__(self):
		return self.first_name


class UserProfile(models.Model):
	user		= models.OneToOneField(User, verbose_name=(u"user"), on_delete=models.CASCADE,)

	def __unicode__(self):
		return self.name
