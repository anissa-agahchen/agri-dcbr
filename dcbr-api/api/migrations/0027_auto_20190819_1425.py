# Generated by Django 2.2 on 2019-08-19 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20190819_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association_membership',
            old_name='reg_num',
            new_name='registrationNumber',
        ),
        migrations.RenameField(
            model_name='inspection',
            old_name='reg_num',
            new_name='registrationNumber',
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='reg_num',
            new_name='registrationNumber',
        ),
        migrations.RenameField(
            model_name='risk_factor_animal',
            old_name='reg_num',
            new_name='registrationNumber',
        ),
        migrations.RenameField(
            model_name='risk_factor_operation',
            old_name='reg_num',
            new_name='registrationNumber',
        ),
    ]
