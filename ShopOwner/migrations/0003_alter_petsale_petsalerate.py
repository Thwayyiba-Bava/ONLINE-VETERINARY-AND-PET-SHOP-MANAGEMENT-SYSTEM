# Generated by Django 3.2.10 on 2021-12-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopOwner', '0002_alter_petsale_petsalerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsale',
            name='PetSaleRate',
            field=models.FloatField(),
        ),
    ]
