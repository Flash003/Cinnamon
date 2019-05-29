# Generated by Django 2.0.6 on 2018-07-12 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Darwin', '0010_marks_exam_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('present', 'present'), ('absent', 'absent')], max_length=10)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Darwin.Teacher')),
            ],
        ),
    ]
