from django.contrib.admin import checks

from admin_tabs.filters import TabFilter


# pylint: disable=too-few-public-methods
class TabFilterAdminChecks(checks.ModelAdminChecks):
    def check(self, admin_obj, **kwargs):
        default_checks = super().check(admin_obj, **kwargs)
        return [*default_checks, *self._check_tab_filter(admin_obj)]

    def _check_tab_filter(self, obj):
        """Check tab_filter is a TabFilter."""

        if obj.tab_filter is None:
            return checks.must_be(
                "defined", option="tab_filter", obj=obj, id="admin_tab_filter.E001"
            )
        if not issubclass(obj.tab_filter, TabFilter):
            return checks.must_inherit_from(
                parent="TabFilter",
                option="tab_filter",
                obj=obj,
                id="admin_tab_filter.E002",
            )
        return []
