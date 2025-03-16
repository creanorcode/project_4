# Import necessary modules from Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Define a custom UserAdmin class with additional actions
class CustomUserAdmin(UserAdmin):
    # Add actions for locking and unlocking user account
    actions = ['lock_users', 'unlock_users']

    def lock_users(self, request, queryset):
        """
        Lock selected user account by setting is_active to False.
        """
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} users have been locked.")
    lock_users.short_description = "Lock selected user account"

    def unlock_users(self, request, queryset):
        """
        Unlock selected user accounts by setting is_active to True.
        """
        def unlock_users(self, request, queryset):
            updated = queryset.update(is_active=True)
            self.message_user(request, f"{updated} users have been unlocked.")
        unlock_users.short_description = "Unlock selected user accounts."


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register the custom UserAdmin so that our actions take effect
admin.site.register(User, CustomUserAdmin)
