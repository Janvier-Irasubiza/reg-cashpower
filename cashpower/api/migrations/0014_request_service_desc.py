# Generated by Django 5.0.6 on 2024-05-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_merge_20240518_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='service_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
