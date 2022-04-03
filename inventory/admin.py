# https://realpython.com/manage-users-in-django-admin/#model-permissions
# https://ofstack.com/python/31843/django-guardian-is-used-to-implement-row-level-permission-control-of-django-admin.html

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import Product
from guardian.shortcuts import assign_perm
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm, get_users_with_perms, get_groups_with_perms

# Unregister the provided model admin

# admin.site.register(User)
# admin.site.register(Group)

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ('name',)

    # app This function determines whether to display on the main page 
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objs(request).exists()

    #  This function controls which data is displayed and which is not displayed when displaying a list of data 
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        data = self.get_model_objs(request)
        return data
        
    #  Internally used to get rows of data that a user has permission to access 
    def get_model_objs(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view', 'change', 'delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions],
                    klass=klass, any_perm=True)

    #  Use to determine whether a user has permission for a data row 
    def has_perm(self, request, obj, action):
        opts = self.opts
        codename = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{codename}', obj)
        else:
            return self.get_model_objs(request, action).exists()

    #  Whether you have permission to view a data row 
    def has_view_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'view')

    #  Whether you have permission to modify a data row 
    def has_change_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'change')

    #  Whether you have permission to delete a data row 
    def has_delete_permission(self, request, obj=None):
        return self.has_perm(request, obj, 'delete')

    # #  The user should have all permissions for his new data rows 
    # def save_model(self, request, obj, form, change):
    #     result = super().save_model(request, obj, form, change)
    #     if not request.user.is_superuser and not change:
    #         opts = self.opts
    #         actions = ['view', 'add', 'change', 'delete']
    #         [assign_perm(f'{opts.app_label}.{action}_{opts.model_name}', request.user, obj) for action in actions]
    #         return result


    # def queryset(self, request):
    #     if request.user.is_superuser:
    #         return super(ProductAdmin, self).queryset(request)
    #     return get_objects_for_user(user=request.user, perms=['view_product', 'change_product', 'delete_product'], klass=Product)
        
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
    # def get_queryset(self, request):
    #     qs = super(UserAdmin, self).get_queryset(request)
    #     staff = User.objects.get(username='staff')
    #     return staff
    # def get_queryset(self, request):
    #     qs = super(UserAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs

    #     return get_objects_for_user(qs, 'auth.view_user')



# Register out own model admin, based on the default UserAdmin
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser

#         if not is_superuser:
#             form.base_fields['username'].disabled = True
#             form.base_fields['is_superuser'].disabled = True
#             form.base_fields['user_permissions'].disabled = True
#             form.base_fields['groups'].disabled = True

#         return form

    # def has_change_permission(self, request, obj=None):
    #     return False


# class ReadOnlyAdminMixin:
#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     # def has_view_permission(self, request, obj=None):
#     #     return False

# @admin.register(Product)
# class RandomModelAdmin(BaseReadOnlyAdminMixin, admin.ModelAdmin):
#     list_display = ("name", )