# Generated by Django 4.1.7 on 2023-04-16 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdoptMe', '0004_alter_post_caracteristicas'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
