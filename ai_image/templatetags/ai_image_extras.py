from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.safestring import SafeString

register = template.Library()

@register.filter(name='auto_br')
@stringfilter
def auto_br(value, limits) -> SafeString:
    """指定した文字数毎に<br>タグを挿入するDjango template tag
    元の文字列の<br>タグが含まれていた場合はその場所でも改行する。
    
    Args:
        value ([type]): 元の文字列
        limits ([type]): <br>を挿入する文字数

    Returns:
        [type]: [description]
    """
    
    # エラー時は10文字で改行
    try:
        limits = int(limits)
    except ValueError as e:
        limits = 10

    split_value = value.split('<br>')
        
    split_again = []
    for pease in split_value:
        split_again.extend([pease[i: i+limits] for i in range(0, len(pease), limits)])

    value = '<br>'.join(split_again)
    return mark_safe(value)
