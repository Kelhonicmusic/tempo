# Generated by Django 5.1.2 on 2024-11-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_booking_booked_at_remove_enrollment_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='main_app.lesson'),
        ),
    ]
