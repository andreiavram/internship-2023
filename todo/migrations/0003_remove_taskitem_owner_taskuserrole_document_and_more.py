# Generated by Django 4.2.3 on 2023-07-05 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_taskitem_status_alter_taskitem_parent_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskitem',
            name='owner',
        ),
        migrations.CreateModel(
            name='TaskUserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('supervisor', 'Supervisor'), ('assignee', 'Assignee')], default='assignee', max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.taskitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='documents')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='todo.taskitem')),
            ],
        ),
        migrations.AddField(
            model_name='taskitem',
            name='users',
            field=models.ManyToManyField(through='todo.TaskUserRole', to=settings.AUTH_USER_MODEL),
        ),
    ]
