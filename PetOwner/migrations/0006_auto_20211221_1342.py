# Generated by Django 3.2.9 on 2021-12-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetOwner', '0005_alter_petdisease_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='buypet',
            name='DeliveryAddress',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='buyproduct',
            name='DeliveryAddress',
            field=models.TextField(null=True),
        ),
    ]