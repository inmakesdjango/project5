# Generated by Django 4.2.3 on 2023-07-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmakes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='pics')),
                ('description1', models.TextField()),
            ],
        ),
    ]
