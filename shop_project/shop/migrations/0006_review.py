# Generated by Django 2.2.5 on 2019-12-22 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191208_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('comment', models.CharField(max_length=3000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Product')),
            ],
        ),
    ]