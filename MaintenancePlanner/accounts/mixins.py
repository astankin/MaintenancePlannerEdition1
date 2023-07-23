from django.shortcuts import redirect


class AllowedUsersMixin:
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role in self.allowed_roles:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('home-page')