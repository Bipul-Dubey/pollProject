# Generated by Django 4.0.4 on 2022-07-08 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollApp', '0004_rename_voters_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
