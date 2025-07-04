# Generated by Django 4.2.5 on 2023-10-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_subject_student_grade_delete_grade_subject_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Unknown', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_no',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Unknown', max_length=20, null=True),
        ),
    ]
