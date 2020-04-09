from django.shortcuts import render, get_object_or_404, redirect
from .models import Mysearchface
from .forms import MysearchfaceForm
from .searchface import predict
import os
import os.path
import os
from project_DjangoFace.settings import MEDIA_ROOT
from main.models import Suspect
# Create your views here.



def Mysearchfaceviews(request):
    if request.method == "POST":
        form = MysearchfaceForm(request.POST, request.FILES)
        if form.is_valid():
            face = form.save(commit=False)
            face.author = request.user
            face.save()
            return redirect('searchface_sent', pk=face.pk)
    else:
        form = MysearchfaceForm()
    return render(request, 'searchface/searchface_form.html', {'form': form})


def Mysearchfaceviews_sent(request, pk):
    sentface = get_object_or_404(Mysearchface, pk=pk)
    print(sentface.name)




    # here I want the /static/image.jpg file then
    #image_file = os.path.join(MEDIA_ROOT, 'main/test/admin.png')
    name_image = os.path.basename(sentface.image.name)
    image_file = os.path.join(MEDIA_ROOT, 'main/test/'+name_image)
    knn_file = os.path.join(MEDIA_ROOT, 'main/trained_knn_model.clf')


    print("Поиск лиц в {}".format(image_file))

    # Найти всех людей на изображении, используя обученную модель классификатора
    # Примечание: вы можете передать либо имя файла классификатора, либо экземпляр модели классификатора
    predictions = predict(image_file, model_path=knn_file)

    # Вывести результаты на консоль
    if predictions == []:
        print("# # # # # # Некорректно изображено лицо на фотографии {}".format(image_file))
    for name, (top, right, bottom, left) in predictions:
        if name=='unknown':
            print('Херня')
            return render(request, 'searchface/searchface_sent.html', {'sentface': sentface})
        else:
            sentface.passport = name
            people = Suspect.objects.filter(passport=sentface.passport)

            suspect = get_object_or_404(Suspect, passport=sentface.passport)
            print("- Найдено {} в {}".format(name, image_file))
            return render(request, 'searchface/searchface_sent.html', {'sentface': sentface, 'suspect': suspect})



#<img src="..." class="img-fluid" alt="Адаптивные изображения">