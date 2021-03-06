# Generated by Django 2.0.2 on 2018-06-03 08:20

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 6, 3, 8, 20, 8, 513319, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
