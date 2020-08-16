import pytest

from django.urls import resolve, reverse, Resolver404

pytestmark = pytest.mark.django_db


# def test_admin():
#     assert reverse("users:update") == "/admin"
#     assert resolve("/admin").view_name == "users:update"

def test_post():
    assert reverse("ai_image:post") == "/"
    assert resolve("/").view_name == "ai_image:post"

def test_not_existed():
    with pytest.raises(Resolver404):
        resolve('/not/existed')