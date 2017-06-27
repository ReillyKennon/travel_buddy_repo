# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import re
# Create your models here.

def validate_name(value):
    letters = re.compile('[A-Za-z]+$')

    if letters.match(value) == None:
        raise ValidationError('Name must only contain letters')

    if len(value) < 2:
        raise ValidationError('Name must be longer than 2 characters')

def validate_password(value):

    if len(value) < 8:
        raise ValidationError('Password must contain 8 or more characters')

class TripManager(models.Manager):
    def add(self, postData):
        trip = Trip.objects.create(planner=postData['planner'], destination=postData['destination'], start=postData['start'], end=postData['end'], description=postData['description'])
        trip.save()

    def join(self, postData):
        join_trip = User.objects.get(request.POST['email'])
        trip.users.add(join_trip)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    email = models.CharField(max_length=30, unique=True, )
    password = models.CharField(max_length=1000, validators=[validate_password])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Trip(models.Model):
    planner = models.CharField(max_length=60)
    destination = models.CharField(max_length=100)
    start = models.TextField()
    end = models.TextField()
    description = models.TextField()
    buddies = models.ManyToManyField(User, related_name="buddies", default=None)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    objects = TripManager()
