# Generated by Django 5.0.5 on 2024-05-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mecanicoimg'),
        ),
        migrations.AlterField(
            model_name='tipoempleado',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
