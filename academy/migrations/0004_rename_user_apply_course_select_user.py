# Generated by Django 4.0 on 2022-04-06 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_apply_course_cnic_back_apply_course_cnic_front_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply_course',
            old_name='user',
            new_name='select_user',
        ),
    ]
