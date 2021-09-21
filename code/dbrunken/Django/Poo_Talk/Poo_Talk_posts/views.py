from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Author

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)
    
class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    
    def form_valid(self, form):
       return super().form_valid(form)