# Generated by Django 5.0.4 on 2024-04-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sle', '0003_alter_course_registered_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
