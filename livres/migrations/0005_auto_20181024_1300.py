# Generated by Django 2.1.2 on 2018-10-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livres', '0004_auto_20181024_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='livre_images', verbose_name='image'),
        ),
    ]
