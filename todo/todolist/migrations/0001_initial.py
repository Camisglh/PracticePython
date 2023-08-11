# Generated by Django 4.2.4 on 2023-08-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('active', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='todolist.category')),
            ],
        ),
    ]
