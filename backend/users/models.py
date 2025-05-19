from django.db import models

'''
This model is used to detail users accounts.
'''

class User(models.Model):
    """
    This model is used to detail users accounts.
    """

    # The username of the user
    username = models.CharField(max_length=150, unique=True)

    # The email of the user
    email = models.EmailField(unique=True)

    # The password of the user
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
