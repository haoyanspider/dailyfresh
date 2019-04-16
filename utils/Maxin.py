from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类as_view方法
        view = super().as_view(**initkwargs)
        return login_required(view)