# Generated by Django 2.2.5 on 2019-10-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
