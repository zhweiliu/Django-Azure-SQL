from django.contrib import admin

from price.models import Popularinfo
from price.models import Searchinfo
from price.models import Userinfo

# Register your models here.

admin.site.register(Userinfo)
admin.site.register(Searchinfo)
admin.site.register(Popularinfo)