# Generated by Django 2.2 on 2019-04-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Darwin', '0022_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
    ]
