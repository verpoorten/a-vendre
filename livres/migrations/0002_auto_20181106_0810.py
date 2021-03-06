# Generated by Django 2.1.2 on 2018-11-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='neuf',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='livre',
            name='langue',
            field=models.CharField(choices=[('FR', 'Français'), ('ENG', 'Anglais'), ('DE', 'Allemand')], default='FR', max_length=5),
        ),
    ]
