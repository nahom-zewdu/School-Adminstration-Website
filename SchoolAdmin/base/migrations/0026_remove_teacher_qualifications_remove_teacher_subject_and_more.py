# Generated by Django 4.2.5 on 2023-10-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_student_parent_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teaches_grade',
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('S', 'Social'), ('N', 'Natural'), ('PE', 'Physical Education')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]
