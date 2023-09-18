# Generated by Django 2.2.28 on 2023-09-18 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0007_auto_20230917_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('age', models.PositiveIntegerField(verbose_name='年龄')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=10, verbose_name='性别')),
                ('contact', models.CharField(max_length=20, verbose_name='联系方式')),
                ('job_status', models.CharField(choices=[('actively_looking', '积极找工作'), ('not_looking', '暂不找工作')], max_length=20, verbose_name='求职状态')),
                ('job_expectation', models.TextField(verbose_name='求职期望')),
                ('work_experience', models.TextField(verbose_name='工作/实习经历')),
                ('project_experience', models.TextField(verbose_name='项目经历')),
                ('education', models.CharField(max_length=100, verbose_name='教育程度')),
                ('skills', models.TextField(verbose_name='专业技能')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '求职者简历',
                'verbose_name_plural': '求职者简历',
            },
        ),
    ]
