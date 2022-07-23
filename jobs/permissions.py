from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print('>>>>>>>',request.user.user_type)
        print("inside permission")

        if request.user.user_type == 'COMPANY':
            print('Is AUTHENTICATED')
            return True
        return False