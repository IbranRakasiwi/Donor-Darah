# Generated by Django 2.2.12 on 2020-11-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasien',
            name='ttl',
            field=models.CharField(max_length=240, null=True),
        ),
    ]