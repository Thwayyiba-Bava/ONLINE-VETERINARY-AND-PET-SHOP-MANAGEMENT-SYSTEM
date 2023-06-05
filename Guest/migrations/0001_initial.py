# Generated by Django 3.2.9 on 2021-12-05 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BasicEntry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=20)),
                ('ShopContact', models.CharField(max_length=20)),
                ('ShopEmail', models.CharField(max_length=20)),
                ('ShopLicencenumber', models.CharField(max_length=20)),
                ('ShopProof', models.FileField(upload_to='Uploads/ShopProof/')),
                ('ShopUsername', models.CharField(max_length=20)),
                ('ShopPassword', models.CharField(max_length=20)),
                ('shopStatus', models.BooleanField(default=False)),
                ('ShopPlace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BasicEntry.place')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=20)),
                ('CustomerGender', models.CharField(max_length=20)),
                ('CustomerContact', models.CharField(max_length=20)),
                ('CustomerEmail', models.EmailField(max_length=20, unique=True)),
                ('CustomerImage', models.FileField(null=True, upload_to='Uploads/PetOwnerPhotos/')),
                ('CustomerUsername', models.CharField(max_length=20)),
                ('CustomerPassword', models.CharField(max_length=20)),
                ('CustomerPlace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BasicEntry.place')),
            ],
        ),
    ]
