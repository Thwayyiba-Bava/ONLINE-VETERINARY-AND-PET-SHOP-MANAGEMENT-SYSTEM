# Generated by Django 3.2.9 on 2021-12-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetOwner', '0006_auto_20211221_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petdisease',
            old_name='Reply',
            new_name='DrDesc',
        ),
        migrations.AddField(
            model_name='petdisease',
            name='DrDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='petdisease',
            name='DrMeetingLink',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='petdisease',
            name='DrMessage',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='petdisease',
            name='DrTime',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
