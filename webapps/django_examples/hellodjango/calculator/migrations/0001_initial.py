# Generated by Django 2.2.4 on 2019-08-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('operation', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
