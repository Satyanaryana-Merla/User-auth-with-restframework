# Generated by Django 4.1.7 on 2023-04-20 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('company_address', models.CharField(max_length=100, null=True)),
                ('company_about', models.CharField(max_length=100, null=True)),
                ('company_number', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=20, null=True)),
                ('Employee_Email', models.EmailField(max_length=254, null=True)),
                ('Employee_id', models.CharField(max_length=8, null=True)),
                ('Role', models.CharField(max_length=20, null=True)),
                ('Date_of_birth', models.DateField(null=True)),
                ('Activate', models.BooleanField(default=True, null=True)),
                ('Created', models.DateField(auto_now=True, null=True)),
                ('Updated', models.DateField(auto_now=True, null=True)),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employeee', to='app.company')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
