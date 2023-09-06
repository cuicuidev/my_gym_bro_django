from django.db import models
from django.contrib.auth.models import User

##############################################################################################################################

class Exercise(models.Model):

    name = models.CharField(max_length = 64)

##############################################################################################################################

class Session(models.Model):

    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    user_id = models.ForeignKey(User, verbose_name="user_id", on_delete=models.CASCADE)

##############################################################################################################################

class Workout(models.Model):

    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    user_id = models.ForeignKey(User, verbose_name="user_id", on_delete=models.CASCADE)

    session_id = models.ForeignKey(Session, verbose_name="session_id", on_delete=models.CASCADE)

##############################################################################################################################

class SetEntry(models.Model):
    
    timestamp = models.DateTimeField("timestamp")

    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    user_id = models.ForeignKey(User, verbose_name="user_id", on_delete=models.CASCADE)

    workout_id = models.ForeignKey(Workout, verbose_name="workout_id", on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, verbose_name="exercise_id", on_delete=models.CASCADE)

    weight = models.FloatField("weight")
    repetitions = models.FloatField("repetitions")
    repetitions_in_reserve = models.FloatField("repetitions_in_reserve")
    
    duration = models.TimeField("duration")
    rest = models.TimeField("rest")

    drop_set = models.ForeignKey('self', null = True, blank = True, on_delete = models.SET_NULL, related_name = 'parent_set')

##############################################################################################################################




##############################################################################################################################