from rest_framework import permissions


class YourProfile(permissions.BasePermission):
    ''' Allow for editing of profile by the owner of that profile'''

    def has_object_permission(self, request, view, obj):
        # read-only request are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed by the owner of the profile    
        return obj.user == request.user