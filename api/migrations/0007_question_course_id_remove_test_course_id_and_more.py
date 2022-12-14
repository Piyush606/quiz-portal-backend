# Generated by Django 4.1 on 2022-08-28 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_test_chapter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.course'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='test',
            name='course_id',
        ),
        migrations.AddField(
            model_name='test',
            name='course_id',
            field=models.ManyToManyField(to='api.course'),
        ),
    ]
