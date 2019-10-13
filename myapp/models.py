from django.db import models

class Users(models.Model):

   name = models.CharField(max_length = 50)
   phone = models.CharField(max_length = 50)
   email = models.CharField(max_length = 50)
   address = models.CharField(max_length = 50)
   description = models.CharField(max_length = 50)

   class Meta:
      db_table = "users"