from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants', null=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    watering_frequency = models.IntegerField(help_text="Days between watering")
    last_watered = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    care_tasks = models.ManyToManyField('CareTask', related_name='plants', blank=True)

    def __str__(self):
        return f"{self.name} ({self.species})"

    class Meta:
        ordering = ['name']

class WateringRecord(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='watering_records')
    watered_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Watered {self.plant.name} on {self.watered_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-watered_at']

class CareTask(models.Model):
    TASK_TYPES = [
        ('fertilize', 'Fertilize'),
        ('prune', 'Prune'),
        ('repot', 'Repot'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_tasks')
    name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    frequency = models.IntegerField(help_text="Days between tasks")
    last_completed = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_task_type_display()}: {self.name}"

    class Meta:
        ordering = ['task_type', 'name']
