# Generated by Django 5.0.3 on 2024-04-28 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danhmucgia',
            fields=[
                ('madanhmucgia', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('tendanhmucgia', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Danhmucphong',
            new_name='Danhmucquan',
        ),
        migrations.RenameField(
            model_name='danhmucquan',
            old_name='madanhmuc',
            new_name='madanhmucquan',
        ),
        migrations.RenameField(
            model_name='danhmucquan',
            old_name='tendanhmuc',
            new_name='tendanhmucquan',
        ),
        migrations.RemoveField(
            model_name='phong',
            name='danhmuc',
        ),
        migrations.AddField(
            model_name='phong',
            name='danhmucquan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='danh_muc_quan', to='app.danhmucquan'),
        ),
        migrations.AddField(
            model_name='phong',
            name='danhmucgia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='danh_muc_giaca', to='app.danhmucgia'),
        ),
    ]