from django.template import Context, loader
from django.http import HttpResponse
from models import Notes

def notes_list(request):
  note_list = Notes.objects.all()
  t = loader.get_template('notes/list.html')
  c = Context({'note_list': note_list})
  return HttpResponse(t.render(c))

def notes_detail(request, id):
  note = Notes.objects.get(pk=id)
  t = loader.get_template('notes/detail.html')
  c = Context({'note': note})
  return HttpResponse(t.render(c))
