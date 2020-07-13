from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):

	CATEGORIES_CHOICES = [
        ('WebDevelopment', 'WebDevelopment'),
        ('AndroidDevelopment', 'AndroidDevelopment'),
        ('BlockChain', 'BlockChain'),
        ('IOT', 'IOT'),
        ('MachineLearning', 'MachineLearning'),
		('IosDevelopment', 'IosDevelopment'),
		('DataScience', 'DataScience'),
		('Others', 'Others'),
    ]
	title=models.CharField(max_length=120)
	categories = models.CharField(max_length=100,choices=CATEGORIES_CHOICES,default='WebDevelopment',blank=False)
	image=models.ImageField(upload_to='Hookups/images/',blank=True)
	email=models.CharField(max_length=200)
	description=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	completed= models.BooleanField(default=False)
	user=models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

