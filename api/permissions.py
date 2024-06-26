from rest_framework.permissions import BasePermission


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
                'book.view_book'
            )
        return False


class HasViewHachettePermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_hachette_book'
            )
        return False


class HasViewFlammarionPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_flammarion_book'
            )
        return False


class HasViewAlbinMichelPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_albin_michel_book'
            )
        return False


class HasViewGallimardPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_gallimard_book'
            )
        return False


class HasViewLeLivreDePochePermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_le_livre_de_poche_book'
            )
        return False


class HasViewRobertLaffontPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_robert_laffont_book'
            )
        return False


class HasViewJaiLuPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_j_ai_lu_book'
            )
        return False


class HasViewFayardPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_fayard_book'
            )
        return False


class HasCreateIndicatorPermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'POST' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'gain.add_indicator'
            )
        return False
