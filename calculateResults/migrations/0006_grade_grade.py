# Generated by Django 2.1a1 on 2018-10-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculateResults', '0005_auto_20181013_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
