# Generated by Django 3.1 on 2020-11-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='fingerprint',
            field=models.CharField(max_length=1630, null=True),
        ),
    ]