from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Suspect
from .forms import SuspectForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView



def Suspect_list(request):
    suspects = Suspect.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/suspect_list.html', {'suspects': suspects})

def Suspect_detail(request, pk):
    suspect = get_object_or_404(Suspect, pk=pk)
    return render(request, 'main/suspect_detail.html', {'suspect': suspect})

# class Suspect_new(FormView):
#     form_class = SuspectForm
#     template_name = 'main/suspect_edit.html'
#     #success_url =reverse_lazy('suspect_detail')
#
#     def form_valid(self, form):
#
#         form.author = self.request.user
#         form.published_date = timezone.now()
#         form.save()
#         return redirect('suspect_detail', pk=form.pk)
def Suspect_new(request):
    if request.method == "POST":
        form = SuspectForm(request.POST, request.FILES)
        if form.is_valid():
            suspect = form.save(commit=False)
            suspect.author = request.user
            suspect.published_date = timezone.now()
            suspect.save()
            return redirect('suspect_detail', pk=suspect.pk)
    else:
        form = SuspectForm()
    return render(request, 'main/suspect_edit.html', {'form': form})






# def post_edit(request, pk):
#   post = get_object_or_404(Post, pk=pk)
#   if request.method == "POST":
#        form = SuspectForm(request.POST, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#   else:
#        form = SuspectForm(instance=post)
#        return render(request, 'blog/post_edit.html', {'form': form})
#

