# Generated by Django 4.1.7 on 2023-04-17 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0009_alter_profile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default=1, upload_to='profiles'),
            preserve_default=False,
        ),
    ]
