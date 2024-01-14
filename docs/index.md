# Welcome to django-admin-tabs documentation

![PyPI - License](https://img.shields.io/pypi/l/django-admin-tabs)
![Pypi Version](https://img.shields.io/pypi/v/django-admin-tabs.svg)
[![Codecov](https://codecov.io/github/valbertovc/django-admin-tabs/branch/main/graph/badge.svg?token=2R5S5GTS0X)](https://codecov.io/github/valbertovc/django-admin-tabs)
![Building](https://img.shields.io/github/actions/workflow/status/valbertovc/django-admin-tabs/release.yml)
![Python Versions](https://img.shields.io/pypi/pyversions/django-admin-tabs.svg)
![Django Versions](https://img.shields.io/pypi/frameworkversions/django/django-admin-tabs)

This site contains the project documentation for the
`django-admin-tabs` project that is a django reusable app used in the
Django projects.

## Table of contents

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference.md)
4. [Explanation](explanation.md)

# Introduction

It generates a filter and display it as a set of tabs in you admin changelist page.

## Get started
Install the django-admin-tabs in your virtual environment:
```bash
$ pip install django-admin-tabs
```
Import it in your admin.py file and add it as a tab_filter argument in any admin class. 
```python
from admin_tabs import TabFilterAdmin, TabFilter, tab
from django.contrib import admin

# my_app/filters.py
class UserTabfilter(TabFilter):
    @tab()
    def with_email(self, request, queryset):
        return queryset.exclude(email="")

# my_app/admin.py    
class MyModelAdmin(TabFilterAdmin, admin.ModelAdmin):
    tab_filter = UserTabfilter
```


## Useful links

1. [Documentation](https://valbertovc.github.io/django-admin-tabs/)
2. [Changelog](https://github.com/valbertovc/django-admin-tabs/releases)
3. [PyPi Page](https://pypi.org/project/django-admin-tabs/)
4. [Repository](https://github.com/valbertovc/django-admin-tabs)
5. [Bug Tracker](https://github.com/valbertovc/django-admin-tabs/issues)