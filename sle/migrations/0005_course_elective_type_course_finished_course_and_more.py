# Generated by Django 5.0.4 on 2024-04-12 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sle', '0004_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='elective_type',
            field=models.CharField(choices=[('LA', 'Liberal Arts'), ('DCT', 'Departmental Core Theory'), ('DCL', 'Departmental Core Lab'), ('FE', 'Free Elective')], default='LA', max_length=60),
        ),
        migrations.AddField(
            model_name='course',
            name='finished_course',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='registered_students',
            field=models.ManyToManyField(blank=True, related_name='ongoing', to=settings.AUTH_USER_MODEL),
        ),
    ]
