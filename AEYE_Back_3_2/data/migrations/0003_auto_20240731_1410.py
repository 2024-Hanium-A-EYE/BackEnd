# Generated by Django 3.2 on 2024-07-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_datamodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Initiate_AI_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Request_Data_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='DataModel',
        ),
    ]
