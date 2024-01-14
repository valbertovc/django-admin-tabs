from django.contrib.auth import get_user_model
from django.test import TestCase

from admin_tabs import TabFilterAdmin
from admin_tabs.views import TabChangeList

User = get_user_model()


class TabFilterAdminTestCase(TestCase):
    admin_class = TabFilterAdmin

    def test_get_changelist(self):
        changelist = self.admin_class().get_changelist(None)
        self.assertIs(changelist, TabChangeList)

    def test_get_tab_filter(self):
        tab_filter = self.admin_class().get_tab_filter(None)
        self.assertIsNone(tab_filter)
