from django import template

register = template.Library()


@register.inclusion_tag(
    "apiview/templatetags/book_table_index.html"
)
def book_table_index(
    table_data_json
) -> dict:
    return {
        "self": table_data_json
    }
