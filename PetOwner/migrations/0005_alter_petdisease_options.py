# Generated by Django 3.2.9 on 2021-12-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetOwner', '0004_auto_20211209_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petdisease',
            options={'ordering': ['Status', 'Date']},
        ),
    ]
