from django import template

# create a object of Library class
register = template.Library()


# create a custom template tag
@register.filter(takes_context=True)
def cart_item_count(context):
    request = context['request']
    count = request.session.get('cart', None)
    print(count, 'items')
    return count