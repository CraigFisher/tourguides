from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import GuideProfile
from profiles.models import MemberProfile


class MemberProfileInline(admin.StackedInline):
    model = MemberProfile
    can_delete = False
    verbose_name_plural = 'member profiles'


class GuideProfileInline(admin.StackedInline):
    model = GuideProfile
    can_delete = False
    verbose_name_plural = 'tour guide profiles'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberProfileInline, GuideProfileInline)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
