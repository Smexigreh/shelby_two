# Generated by Django 4.0.3 on 2022-04-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Border_even_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('border_even', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Border_odd_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('border_odd', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='DateNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='InfoImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main_page/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Title_eveen_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_even', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Title_odd_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_odd', models.CharField(default=None, max_length=40)),
            ],
        ),
    ]