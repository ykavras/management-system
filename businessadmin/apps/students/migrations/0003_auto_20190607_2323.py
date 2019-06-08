# Generated by Django 2.2.1 on 2019-06-07 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='members.Member', verbose_name='Kullanıcı'),
        ),
    ]