# Generated by Django 5.0.8 on 2024-08-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0011_alter_relationship_goals_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='costume_user',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
