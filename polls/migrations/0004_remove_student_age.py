# Generated by Django 4.1.1 on 2022-10-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
