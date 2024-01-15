# How-to guides

This part of the project documentation focuses on a
**problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code
provided in this project.

## Ready-to-use classes

Consider the scenario below:

```python
from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_filter = ("is_staff", "is_superuser")

```

If you want to organize better the changelist page you
can add a set of tabs that applies filter and changes
the list of data showed, like you do in a django's list_filter
feature.

### Prepare your filter and admin classes

1. Your filter classes could be placed in `admin_filters.py` or just `filters.py` module.

```python
from admin_tabs import TabFilter, tab


class UserTabFilter(TabFilter):
    @tab()
    def is_staff(self, request, queryset):
        return queryset.filter(is_staff=True)
   
    @tab(label="Super-users")
    def is_superuser(self, request, queryset):
        return queryset.filter(is_superuser=True)
```

2. Now you must declare you tab filter class in you admin class

```python
from admin_tabs import TabFilterAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin
from . import filters
User = get_user_model()


@admin.register(User)
class MyUserAdmin(TabFilterAdmin, admin.ModelAdmin):
    tab_filter = filters.UserTabFilter
    list_filter = ("is_staff", "is_superuser")
```

3. Done! When you access your admin changelist page you will see the 
new filter on top of page.
