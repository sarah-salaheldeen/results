# Generated by Django 2.1a1 on 2018-10-28 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculateResults', '0009_auto_20181028_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='name',
        ),
    ]
