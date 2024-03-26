from rest_framework.permissions import BasePermission


class IsAdmin(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.user and request.user.is_authenticated:
            return request.user.is_superuser
        return False


class HasDeletePermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'demo.delete_book'
            )
        return False


class HasUpdatePermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'demo.change_book'
            )
        return False


class HasViewPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'demo.view_book'
            )
        elif request.user and request.user.is_superuser:
            return True
        return False
