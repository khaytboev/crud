import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import FirstForm
from .models import FirstModel
from django.shortcuts import render


def view1(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    # return HttpResponse(html)

    return render(request, "grut/knopka.html")


def view2(request):
    context = {}

    form = FirstForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "grut/brain.html", context)


def list_view(request):
    context = {}

    context["dataset"] = FirstModel.objects.all()

    return render(request, "grut/list.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = FirstModel.objects.get(id=id)

    return render(request, "grut/detail_view.html", context)


def update_view(request, id):

    context = {}

    obj = get_object_or_404(FirstModel, id=id)

    form = FirstForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, "grut/update_view.html", context)


def delete_view(request, id):

    context = {}

    obj = get_object_or_404(FirstModel, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "grut/delete_view.html", context)

