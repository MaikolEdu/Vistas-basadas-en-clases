from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Entry


class EntryCreateView(CreateView):
	model= Entry


class EntryDetailView(DetailView):
	model = Entry


class EntryListView(ListView):
	model = Entry

class EntryUpdateView(UpdateView):
	model = Entry

class EntryDeleteView(DeleteView):
	model = Entry