# Generated by Django 4.1.1 on 2022-10-03 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_student_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='age_field',
        ),
    ]