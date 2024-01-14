# django-admin-tabs

![PyPI - License](https://img.shields.io/pypi/l/django-admin-tabs)
![Pypi Version](https://img.shields.io/pypi/v/django-admin-tabs.svg)
[![Codecov](https://codecov.io/github/valbertovc/django-admin-tabs/branch/main/graph/badge.svg?token=2R5S5GTS0X)](https://codecov.io/github/valbertovc/django-admin-tabs)
![Building](https://img.shields.io/github/actions/workflow/status/valbertovc/django-admin-tabs/release.yml)
![Python Versions](https://img.shields.io/pypi/pyversions/django-admin-tabs.svg)
![Django Versions](https://img.shields.io/pypi/frameworkversions/django/django-admin-tabs)

It generates dynamically a directory path and a secure file name for Django FileField.

Main options:
- Ready to use generators.
- Generate secure file name without especial characters.
- Generate file name using a uuid value.
- Dynamically generate paths from the model instance.
- Generate paths using Python datetime formats.

## Get started
Install the django-admin-tabs in your virtual environment
```bash
$ pip install django-admin-tabs
```
Import it in your models file and add it as a `upload_to` argument in the `FileField` 
```python
# my_app/models.py
from upload_to import UploadTo
from django.db import models


class MyModel(models.Model):
    attachment = models.FileField(upload_to=UploadTo("attachments"))
```
The path and file name generated will be like this:
```text
"attachments/the-file-name-uploaded.pdf"
```

## How to use the ready-to-use classes

Consider the scenario below:
```python
import upload_to
from django.db import models


class MyUser(models.Model):
    username = models.CharField(...)
    avatar = models.FileField(upload_to=<generator>)

instance = MyUser(username='user@email.com')
```
Replace the `<generator>` fragment by the generators as showed below:
#### File in root folder
```python
>>> generator = upload_to.UploadTo()
>>> generator(instance, "file.pdf")
"file.pdf"

```
#### Define a folder structure
```python
>>> generator = upload_to.UploadTo(prefix=["files", "documents"])
>>> generator(instance, "file.pdf")
"files/documents/file.pdf"
```
#### Generate a folder name using datetime formats from Python
```python
>>> generator = upload_to.UploadTo(prefix=["pictures", "%Y"])
>>> generator(instance, "file.png")
"pictures/2023/file.png"
```
#### Replace the file name by an hexadecimal uuid value
```python
# 4. replace file name by a uuid value
>>> generator = upload_to.UuidUploadTo()
>>> generator(instance, "file.pdf")
"b189dfdf25e640b2ba5c497472c20962.pdf"
```
#### Generate the folder path using the instance's attributes
```python
>>> generator = upload_to.AttrUploadTo(attrs=["username"])
>>> generator(instance, "file.pdf")
"useremailcom/file.pdf"
```
#### Generate the folder path using the app_label and the model_name from the instance's meta options
```python
>>> generator = upload_to.ModelUploadTo()
>>> generator(instance, "file.pdf")
"my_app/user/file.pdf"
```

## Customize your upload paths

```python
# my_app/models.py
import upload_to
from django.db import models


def my_upload_generator(instance, filename):
    filename = upload_to.uuid_filename(filename)
    path = upload_to.options_from_instance(instance)
    return upload_to.upload_to(path, filename)

class MyProfile(models.Model):
    user = models.OneToOneField(...)
    avatar = models.FileField(upload_to=my_upload_generator)
```

## Useful links

1. [Documentation](https://valbertovc.github.io/django-admin-tabs/)
2. [Changelog](https://github.com/valbertovc/django-admin-tabs/releases)
3. [PyPi Page](https://pypi.org/project/django-admin-tabs/)