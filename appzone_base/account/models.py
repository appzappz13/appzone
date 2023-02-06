from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now



class User(AbstractUser):
	# sponsor_name=models.CharField(blank=True, max_length=150, verbose_name='sponsor_name')
	status = models.IntegerField(default=0,verbose_name='status', null=True)
	wallet_amount = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'uploads/',null=True)
	address = models.CharField(max_length=250,null=True)
	city = models.CharField(max_length=250,null=True)
	country = models.CharField(max_length=250,null=True)
	postal_code = models.IntegerField(null=True)
	about_me = models.CharField(max_length=750,null=True)
	sponsor_name = models.ForeignKey("account.User",null=True, on_delete=models.CASCADE)

	REQUIRED_FIELDS = []
	def __str__(self):
       	 return self.username

      


		 
		 
		
   