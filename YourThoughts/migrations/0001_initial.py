# Generated by Django 3.1.1 on 2020-09-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=25)),
                ('email_id', models.CharField(max_length=65)),
                ('phone_nu', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Birthday', models.DateField()),
            ],
        ),
    ]