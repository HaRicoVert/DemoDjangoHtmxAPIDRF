from django import template

register = template.Library()


@register.inclusion_tag(
    'customdsfr/custom_input.html'
)
def custom_input(
    input_type,
    input_name="default_name",
    label="default_label",
    input_extra_attributes=None,
    input_extra_classes=None,
    input_placeholder=None
):
    allowed_input_type = {'text', 'date', 'datetime-local', 'email', 'month', 'number', 'password', 'search', 'tel',
                          'time', 'url', 'week'}

    return {
        'input_type': input_type,
        'input_name': input_name,
        'allowed_input_type': allowed_input_type,
        'label': label,
        'input_placeholder': input_placeholder,
        'input_extra_attributes': input_extra_attributes,
        'input_extra_classes': input_extra_classes
    }
