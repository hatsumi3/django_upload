import pytest
from django.test import SimpleTestCase
from django.template import Context, Template
from django.template.base import VariableDoesNotExist

from ai_image.templatetags import ai_image_extras

def test_auto_br():
    context = Context({'title': 'my_titlemy_titlemy_titlemy_title'})
    template_to_render = Template(
        '{% load ai_image_extras %}'
        '{{ title|auto_br:10 }}'
    )
    rendered_template = template_to_render.render(context)
    
    assert rendered_template == 'my_titlemy<br>_titlemy_t<br>itlemy_tit<br>le'

def test_auto_br_ValueError():
    context = Context({'title': 'my_titlemy_titlemy_titlemy_title'})
    template_to_render = Template(
        '{% load ai_image_extras %}'
        '{{ title|auto_br:"qqqqq" }}'
    )
    
    rendered_template = template_to_render.render(context)

    assert rendered_template == 'my_titlemy<br>_titlemy_t<br>itlemy_tit<br>le'


@pytest.mark.skip(reason='html rendering error')
def test_auto_br_VariableDoesNotExist():
    context = Context({'title': 'my_titlemy_titlemy_titlemy_title'})
    template_to_render = Template(
        '{% load ai_image_extras %}'
        '{{ title|auto_br:qqqqq }}'
    )
    
    with pytest.raises(VariableDoesNotExist) as excinfo:
        rendered_template = template_to_render.render(context)
        assert rendered_template == 'my_titlemy<br>_titlemy_t<br>itlemy_tit<br>le'
