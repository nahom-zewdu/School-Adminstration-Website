# Generated by Django 4.2.5 on 2023-09-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_parent_user_alter_student_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(blank=True, max_length=44, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=44, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, max_length=44, null=True),
        ),
    ]
