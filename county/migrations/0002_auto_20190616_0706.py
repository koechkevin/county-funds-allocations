# Generated by Django 2.2.2 on 2019-06-16 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('county', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='sub_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='county.SubLocation'),
        ),
    ]
