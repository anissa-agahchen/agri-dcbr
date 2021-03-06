# Generated by Django 2.2 on 2019-06-14 22:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=14)),
                ('op_first_name', models.CharField(max_length=32)),
                ('op_middle_name', models.CharField(max_length=50)),
                ('op_last_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('soc_1', models.BooleanField(default=False)),
                ('soc_2', models.BooleanField(default=False)),
                ('soc_3', models.BooleanField(default=False)),
                ('soc_4', models.BooleanField(default=False)),
                ('soc_5', models.BooleanField(default=False)),
                ('soc_6', models.BooleanField(default=False)),
                ('soc_7', models.BooleanField(default=False)),
                ('soc_8', models.BooleanField(default=False)),
                ('soc_9', models.BooleanField(default=False)),
                ('soc_10', models.BooleanField(default=False)),
                ('soc_11', models.BooleanField(default=False)),
                ('soc_1_comment', models.TextField(blank=True, default='')),
                ('soc_2_comment', models.TextField(blank=True, default='')),
                ('soc_3_comment', models.TextField(blank=True, default='')),
                ('soc_4_comment', models.TextField(blank=True, default='')),
                ('soc_5_comment', models.TextField(blank=True, default='')),
                ('soc_6_comment', models.TextField(blank=True, default='')),
                ('soc_7_comment', models.TextField(blank=True, default='')),
                ('soc_8_comment', models.TextField(blank=True, default='')),
                ('soc_9_comment', models.TextField(blank=True, default='')),
                ('soc_10_comment', models.TextField(blank=True, default='')),
                ('soc_11_comment', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Inspections',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=14)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(blank=True, default='', max_length=50)),
                ('email_address', models.CharField(blank=True, default='', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comm_pref', models.CharField(choices=[('Email', 'email'), ('Mail', 'mail')], default='Email', max_length=10)),
                ('operator_type', models.CharField(choices=[('BREEDER', 'breeder'), ('SELLER', 'seller'), ('BREEDER&SELLER', 'breeder & seller')], default='BREEDER', max_length=20)),
                ('operation_name', models.CharField(blank=True, default='', max_length=50)),
                ('operation_URL', models.TextField(blank=True, default='', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Operators',
            },
        ),
        migrations.CreateModel(
            name='Risk_Factor_Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accidental_breeding', models.BooleanField(default=False)),
                ('num_workers', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_breeds_dogs', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_breeds_cats', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('has_vet', models.BooleanField(default=False)),
                ('has_perm_id', models.BooleanField(default=False)),
                ('perm_id_type', models.CharField(choices=[('TATTOO', 'tattoo'), ('MICROCHIP', 'microchip'), ('OTHER', 'other')], default='TATTOO', max_length=10)),
                ('perm_id_other', models.CharField(blank=True, default='', max_length=10)),
                ('operation_type', models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat'), ('DOG&CAT', 'dog & cat')], default='DOG&CAT', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_factor_operations', related_query_name='risk_factor_operations', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'RiskFactorOperations',
            },
        ),
        migrations.CreateModel(
            name='Risk_Factor_Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_dogs_intact', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_litter_whelped', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_cats_intact', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_litter_queened', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_sold', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_transferred', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_traded', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_leased', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_factor_animals', related_query_name='risk_factor_animals', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'RiskFactorAnimals',
            },
        ),
        migrations.CreateModel(
            name='Association_Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assoc_name', models.CharField(blank=True, default='', max_length=50)),
                ('membership_num', models.CharField(blank=True, default='', max_length=10)),
                ('assoc_URL', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associations', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'Associations',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRI', 'Primary'), ('OPN', 'Operation'), ('VET', 'Veterinary')], default='PRI', max_length=3)),
                ('street_num', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('suite', models.CharField(blank=True, default='', max_length=32)),
                ('street_name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('postal_code', models.CharField(max_length=7)),
                ('province', models.CharField(default='BC', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', related_query_name='addresses', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
