# Generated by Django 5.0.4 on 2024-04-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sle', '0005_course_elective_type_course_finished_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='elective_type',
            field=models.CharField(choices=[('Liberal Arts', 'LA'), ('Departmental Core Theory', 'DCT'), ('Departmental Core Lab', 'DCL'), ('Free Elective', 'FE')], default='LA', max_length=60),
        ),
    ]