# Generated by Django 2.2 on 2019-04-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Darwin', '0023_client_login_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
