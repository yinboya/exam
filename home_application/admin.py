# -*- coding: utf-8 -*-

# import from apps here


# import from lib
# ===============================================================================
# from django.contrib import admin
# from apps.__.models import aaaa
#
# admin.site.register(aaaa)
# ===============================================================================

from django.contrib import admin
import models
from django.contrib import admin

admin.site.register(models.Script)
