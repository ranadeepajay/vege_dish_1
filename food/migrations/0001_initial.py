# Generated by Django 5.0.7 on 2024-07-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_description', models.TextField()),
                ('dish_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
