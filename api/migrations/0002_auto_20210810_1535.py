# Generated by Django 3.2.5 on 2021-08-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host_username',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('session_key', models.CharField(max_length=50, unique=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.room')),
            ],
        ),
    ]