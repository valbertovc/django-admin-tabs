from django.test import TestCase

import admin_tabs


def func_mock():
    pass


class TabDecoratorTestCase(TestCase):
    def test_should_create_label_from_djang_pretty_name(self):
        decorated = admin_tabs.decorators.tab(func_mock)
        self.assertEqual("Func mock", decorated.label)

    def test_should_create_user_defined_label(self):
        decorated = admin_tabs.decorators.tab(func_mock, label="User label")
        self.assertEqual("User label", decorated.label)
