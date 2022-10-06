# Generated by Django 4.1.1 on 2022-10-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_rename_age_student_age_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='state',
            new_name='State',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age_field',
        ),
        migrations.AddField(
            model_name='student',
            name='Age_field',
            field=models.IntegerField(default='-'),
        ),
    ]
