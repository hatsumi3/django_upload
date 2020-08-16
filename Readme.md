# Django Upload

## what is this repository?

This is a sample project for learning django. It is currently under construction.

djangoを学習するためのサンプルプロジェクトです。現在は作成途中です。

## Goal

Build a web server with nginx, gunicorn, and django containers up in a docker on AWS EC2.
Set up django's static and media to allow you to check delivery from the web server (nginx).

AWS EC2上のdockerにnginx,gunicorn,djangoのコンテナを立てて、webサーバを構築します。
djangoのstatic,mediaを用いて、webサーバ(nginx)からの配信を確認できるように設定を行います。

## Task

- Add test file
- Fix Dockerfile and docker-compose.yml
  - The following commands are currently being run manualy.
    - python manage.py collectstatic
    - python manage.py makemigrations
    - python manage.py migrate

## Used Library

- python
  - [django3](https://docs.djangoproject.com/en/3.1/)
  - [Pillow](https://pypi.org/project/Pillow/)
- css,javascript
  - [Bootstrap4.5](https://getbootstrap.jp/)

## referances

- [Djangoアプリについて、pytest-djangoを使ってテストしてみた](https://thinkami.hatenablog.com/entry/2016/04/19/001651)