# Generated by Django 2.2.5 on 2019-12-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191207_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compliant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=3000)),
            ],
        ),
    ]