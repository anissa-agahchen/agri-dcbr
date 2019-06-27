# Generated by Django 2.2 on 2019-06-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190614_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='association_membership',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='association_membership',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='inspection',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='inspection',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='risk_factor_animal',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='risk_factor_animal',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='risk_factor_operation',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='risk_factor_operation',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.RemoveField(
            model_name='risk_factor_operation',
            name='animal_type',
        ),
        migrations.AddField(
            model_name='operator',
            name='animal_type',
            field=models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat'), ('DOG & CAT', 'dog & cat')], default='DOG & CAT', max_length=10),
        ),
    ]