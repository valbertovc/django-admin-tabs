from admin_tabs.checks import TabFilterAdminChecks
from admin_tabs.views import TabChangeList

__all__ = [
    "TabFilterAdmin",
]


class TabFilterAdmin:
    change_list_template = "admin_tabs/admin/change_list.html"
    tab_filter = None
    checks_class = TabFilterAdminChecks

    def get_changelist(self, request, **kwargs):  # pylint: disable=unused-argument
        return TabChangeList

    def get_tab_filter(self, request, **kwargs):  # pylint: disable=unused-argument
        return self.tab_filter
