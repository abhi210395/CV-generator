# Generated by Django 3.1 on 2020-12-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=1000)),
                ('degree', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('previous_work', models.TextField(max_length=1000)),
                ('skiils', models.TextField(max_length=1000)),
            ],
        ),
    ]
