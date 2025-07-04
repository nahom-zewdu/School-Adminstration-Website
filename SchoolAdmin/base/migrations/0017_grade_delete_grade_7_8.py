# Generated by Django 4.2.5 on 2023-09-21 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_grade_7_8_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('5', 'Grade 5'), ('6', 'Grade 6'), ('7', 'Grade 7'), ('8', 'Grade 8'), ('9', 'Grade 9'), ('10', 'Grade 10')], max_length=2)),
                ('physics', models.CharField(max_length=4)),
                ('chemistry', models.CharField(max_length=4)),
                ('biology', models.CharField(max_length=4)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Grade_7_8',
        ),
    ]
