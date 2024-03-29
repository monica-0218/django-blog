# Generated by Django 3.0.7 on 2020-06-20 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(help_text='正方形の画像にしてください', upload_to='author-icon/', verbose_name='アイコン')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=255, verbose_name='自己紹介')),
                ('TwitterID', models.CharField(help_text='@はいりません', max_length=15)),
            ],
            options={
                'verbose_name_plural': '著者',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'タグ',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='images/', verbose_name='サムネ')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('description', models.CharField(max_length=255, verbose_name='headタグでの説明')),
                ('content', models.TextField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='公開日')),
                ('is_public', models.BooleanField(default=False, verbose_name='公開する')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
            options={
                'verbose_name_plural': '投稿記事',
                'ordering': ['-created_at'],
            },
        ),
    ]
