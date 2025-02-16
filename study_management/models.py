from django.db import models

class Study(models.Model):
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    SPONSER_NAME = [
        ('Sponser I', 'Sponser I'),
        ('Sponser II', 'Sponser II'),
        ('Sponser III', 'Sponser III'),
        ('Sponser IV', 'Sponser IV'),
    ]

    study_name = models.CharField(max_length=100)
    study_phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=100, choices=SPONSER_NAME)
    study_description = models.TextField()

    def __str__(self):
        return self.study_name
