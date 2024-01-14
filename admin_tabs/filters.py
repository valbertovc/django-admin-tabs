import inspect

from django.contrib import admin

from .exceptions import TabNotFound

__all__ = ["TabFilter"]


class TabFilter(admin.SimpleListFilter):
    """
    Tab filter for Django admin.

    - is_tab: attribute is for control which filter is the tab filter,
       because it is used together other list_filters from Admin class.
    - tabs: must be a list of strings representing the tabs you want
       to show. You may override get_tabs method and put your logic
       to build a dynamic list of tabs. If you keep it empty (None),
       all declared tab methods will be shown.
    """

    title = "Tabs"
    parameter_name = "tab"
    is_tab = True
    template = "admin_tabs/admin/tab_filter.html"
    tabs = None

    def __init__(self, request, params, model, model_admin):
        self._tab_mapping = self._generate_tab_mapping()
        super().__init__(request, params, model, model_admin)

    def _generate_tab_mapping(self):
        members = inspect.getmembers(self, predicate=inspect.ismethod)
        return {
            name: method.label
            for name, method in members
            if getattr(method, "is_tab", False)
        }

    def get_tabs(self, request, model_admin):  # pylint: disable=unused-argument
        if self.tabs is None:
            self.tabs = self._tab_mapping.keys()
        return self.tabs

    def lookups(self, request, model_admin):
        tabs = self.get_tabs(request, model_admin) or []
        return ((value, getattr(self, value).label) for value in tabs)

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            try:
                tab_method = getattr(self, value)
            except KeyError as error:
                raise TabNotFound(f"Tab {value} not found") from error
            queryset = tab_method(request, queryset)
        return queryset
