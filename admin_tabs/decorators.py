from django.forms.utils import pretty_name


def tab(function=None, *, label=None):
    """
    Conveniently define a tab method:

        @tab(label='Is Published?')
        def is_published(self, request, queryset):
            return obj.publish_date is not None
    """

    def decorator(func):
        func.is_tab = True
        if label is None:
            func.label = pretty_name(func.__name__)
        else:
            func.label = label
        return func

    if function is None:
        return decorator
    return decorator(function)
