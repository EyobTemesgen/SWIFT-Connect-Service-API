# Generated by Django 5.0.1 on 2024-01-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_swiftconnection'),
    ]

    operations = [
     
        migrations.AddField(
            model_name='swiftconnection',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
        
    ]
