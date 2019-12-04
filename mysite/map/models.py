from django.db import models

# Create your models here.

class Squirrel(models.Model):
	Latitude = models.FloatField()
	Longitude = models.FloatField()
	Unique_Squirrel_ID = models.CharField(max_length=30,primary_key=True)
	Shift_Choices = (
		('AM','AM'),
		('PM','PM'),
	)
	Shift = models.CharField(max_length=2, choices=Shift_Choices)
	Date = models.IntegerField()
	Age = models.CharField(max_length=10)
	Primary_Fur_Color = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	Specific_Location = models.CharField(max_length=100)

	TF_Choices = (
		('TRUE','TRUE'),
		('FALSE','FALSE'),
	)
	Running = models.CharField(max_length=5,choices=TF_Choices)
	Chasing = models.CharField(max_length=5,choices=TF_Choices)
	Climbing = models.CharField(max_length=5,choices=TF_Choices)
	Eating = models.CharField(max_length=5,choices=TF_Choices)
	Foraging = models.CharField(max_length=5,choices=TF_Choices)


	Other_Activities = models.CharField(max_length=100)
	
	Kuks = models.CharField(max_length=5,choices=TF_Choices)
	Quaas = models.CharField(max_length=5,choices=TF_Choices)
	Moans = models.CharField(max_length=5,choices=TF_Choices)
	Tail_flags = models.CharField(max_length=5,choices=TF_Choices)
	Tail_twitches = models.CharField(max_length=5,choices=TF_Choices)
	Approaches = models.CharField(max_length=5,choices=TF_Choices)
	Indifferent = models.CharField(max_length=5,choices=TF_Choices)
	Runs_from = models.CharField(max_length=5,choices=TF_Choices)
	