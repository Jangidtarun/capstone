# Generated by Django 5.0.4 on 2024-04-10 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admission_type',
            field=models.CharField(choices=[('regular', 'regular'), ('distance', 'non-regular')], default='regular', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='batch',
            field=models.IntegerField(default=2020),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('course_code', models.CharField(max_length=64)),
                ('duration', models.DurationField(verbose_name='course duration')),
                ('credit', models.IntegerField(default=1)),
                ('registered_students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_point', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sle.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]