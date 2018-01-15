from django.contrib.auth.mixins import AccessMixin


class OwnerRequiredMixin(AccessMixin):
    """
    Mixin which checks if:
    - User is logged in
    - If object's user is equal to current user
    - If current user is superuser, allow in
    """
    def is_owner(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        obj = self.get_object()
        return obj.user == user

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.is_owner(request, *args, **kwargs)
        if not user_test_result:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
