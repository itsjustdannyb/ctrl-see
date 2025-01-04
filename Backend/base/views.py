from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import TextDocumentForm
from .models import TextDocument
from django.http import HttpResponseRedirect
import pyttsx3
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

class TextListView(ListView):
    # List all the text document
    model = TextDocument
    template_name = 'textList.html'
    paginate_by = 100


class TextDetailView(DetailView, FormView):

    model = TextDocument
    form_class = TextDocumentForm
    template_name = 'textDets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TextDocumentForm()
        return context
    
    
'''class TextCreateView(CreateViewsd):
    """Text create view"""

    model = TextDocument
    form_class = TextDocumentForm
    template_name = 'textDocCreate.html'


    def get_success_url(self):
        return reverse_lazy("text-detail", kwargs={'pk':self.object.pk})


    def get_object(self, queryset = None):
        pk = self.kwargs.get('pk')
        if pk:
            try:
                return TextDocument.objects.get(pk=pk)
            except TextDocument.DoesNotExist:
                return None
            
        return None
        
    
    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        if pk:
            try:
                existing_doc = TextDocument.objects.get(pk=pk)
                form.instance = existing_doc
            except TextDocument.DoesNotExist:
                pass
            
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        pk = self.kwargs.get('pk')
        if pk:
            try: 
                textDocument = TextDocument.objects.get(pk=pk)
                context['form'] = TextDocumentForm(instance=textDocument)
            
            except TextDocument.DoesNotExist:
                pass

        return context
'''

class TextCreateView(CreateView):
    model = TextDocument
    form_class = TextDocumentForm
    template_name = 'textDocCreate.html'

    def get_success_url(self):
        return reverse_lazy("text-detail", kwargs={'pk': self.object.pk})

class TextUpdateView(UpdateView):
    model = TextDocument
    form_class = TextDocumentForm
    template_name = 'textDocCreate.html'  # Adjust template name

    def get_object(self, queryset = None):
        pk = self.kwargs.get('pk')
        return TextDocument.objects.get(pk=pk)  # Retrieve object for update
    
    def get_success_url(self):
        return reverse_lazy("text-detail", kwargs={'pk': self.object.pk})
    



class GetEditorView(TemplateView):
    template_name = "editor.html"
    extra_context = {"form": TextDocumentForm()}


@csrf_exempt
def textToSpeech(request, pk):
    
    try:
        text = TextDocument.objects.get(id=pk)
        content = text.text
    
        if not content:
            return HttpResponse('No Text available')

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('rate', 125)
        engine.setProperty('voice', voices[1].id)

        engine.say(content)
        engine.runAndWait()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', request.path))
    
    except TextDocument.DoesNotExist:
        return HttpResponse('Text Document not found', status=404)
    
    except Exception as e:
        # Log the specific exception for debugging
        print(f"An error occurred: {e}")
        return HttpResponse(f'An error occurred: {e}', status=500)