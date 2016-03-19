from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.views.generic import FormView

from .forms import FlagCreateForm
from .models import Flag


class FlagCreateView(FormView):
    form_class = FlagCreateForm
    template_name = 'flags/flag_form.html'
    success_url = '/'

    def get_form_kwargs(self):
        try:
            app_label = self.kwargs.pop('app_label')
            model_name = self.kwargs.pop('model_name')
            pk = self.kwargs.pop('pk')

            cls = apps.get_model(app_label=app_label, model_name=model_name)
            self.obj = cls.objects.get(pk=pk)
        except (KeyError, LookupError, ObjectDoesNotExist):
            raise Http404

        return super(FlagCreateView, self).get_form_kwargs()

    def form_valid(self, form):
        Flag.objects.create(content_object=self.obj, creator=self.request.user)
        return super(FlagCreateView, self).form_valid(form)
