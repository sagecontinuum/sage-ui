# Generated by Django 3.0.4 on 2020-03-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_token_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]