# Generated by Django 4.1.7 on 2023-04-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptMe', '0015_alter_profile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default=1, upload_to='posts'),
            preserve_default=False,
        ),
    ]
