from django.contrib import admin
from member.models import *
# Register your models here.
admin.site.register(MemberProfile)
admin.site.register(BookBorrwed)
admin.site.register(ReturnBook)
