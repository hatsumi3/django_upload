""" route setting.
    * ''で一覧表示画面に遷移

Todo:
   TODOリストを記載
    * conf.pyの``sphinx.ext.todo`` を有効にしないと使用できない
    * conf.pyの``todo_include_todos = True``にしないと表示されない

"""

from django.urls import include, path

from . import views

app_name='ai_image'

urlpatterns = [
    path('', views.index, name="post"),
]