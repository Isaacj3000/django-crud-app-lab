# Generated by Django 4.2.20 on 2025-05-06 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0002_wateringrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to=settings.AUTH_USER_MODEL),
        ),
    ]
