from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print("yessss")
        print(request.user)
        print("inside permission")

        if request.user.user_type == 'EMPLOYEE':
            print('Is AUTHENTICATED')
            return True
        return False