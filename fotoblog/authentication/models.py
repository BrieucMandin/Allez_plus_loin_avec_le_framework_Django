from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = [
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    ]


    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=SUBSCRIBER)

    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    