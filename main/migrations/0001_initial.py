# Generated by Django 4.0.6 on 2024-04-01 14:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255, verbose_name='Name of User')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname of User')),
                ('role', models.PositiveIntegerField(choices=[(1, 'admin'), (2, 'client'), (3, 'coach'), (4, 'gym')], default=2, verbose_name='Role')),
                ('gender', models.PositiveIntegerField(choices=[(0, 'none'), (1, 'male'), (2, 'female'), (3, 'other')], default=0, verbose_name='Gender')),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=10, verbose_name='Phone number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Coach')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname of Coach')),
                ('date_of_birth', models.DateField()),
                ('gender', models.PositiveIntegerField(choices=[(0, 'none'), (1, 'male'), (2, 'female'), (3, 'other')], default=0, verbose_name='Gender')),
                ('salary', models.FloatField()),
                ('date_of_start_working', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Coach',
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Gym')),
                ('address', models.CharField(max_length=255, verbose_name='Address of Gym')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=255, verbose_name='Email of Gym')),
            ],
            options={
                'verbose_name_plural': 'Gym',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('day_of_week', models.CharField(max_length=255, verbose_name='Day of week')),
                ('time_of_work', models.TimeField(verbose_name='Time of work')),
                ('Coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_coach', to='main.coach', verbose_name='Coach')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('status', models.CharField(max_length=255, verbose_name='Status')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_coach', to='main.coach', verbose_name='Coach')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gym', to='main.gym', verbose_name='Gym')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_records', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='coach',
            name='gym',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='main.gym', verbose_name='Gym'),
        ),
    ]
