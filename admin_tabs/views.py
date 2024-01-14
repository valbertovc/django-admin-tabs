from django.contrib.admin.views.main import ChangeList

__all__ = [
    "TabChangeList",
]


class TabChangeList(ChangeList):
    def __init__(
        self,
        request,
        model,
        list_display,
        list_display_links,
        list_filter,
        date_hierarchy,
        search_fields,
        list_select_related,
        list_per_page,
        list_max_show_all,
        list_editable,
        model_admin,
        sortable_by,
        search_help_text,
    ):  # pylint: disable=too-many-arguments
        self.tab_filter = model_admin.get_tab_filter(request)
        self.tab_filter_spec = None
        if self.tab_filter is not None:
            list_filter = (self.tab_filter,) + list_filter
        super().__init__(
            request,
            model,
            list_display,
            list_display_links,
            list_filter,
            date_hierarchy,
            search_fields,
            list_select_related,
            list_per_page,
            list_max_show_all,
            list_editable,
            model_admin,
            sortable_by,
            search_help_text,
        )

    def get_has_tab_filter(self):
        return (
            self.tab_filter
            and self.filter_specs
            and getattr(self.filter_specs[0], "is_tab", False)
            and self.filter_specs[0].has_output()
        )

    def get_queryset(self, request):  # pylint: disable=arguments-differ
        queryset = super().get_queryset(request)
        if self.get_has_tab_filter():
            self.tab_filter_spec = self.filter_specs.pop(0)
        return queryset
