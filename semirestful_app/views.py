from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def shows(request):

    print(Show.objects.all())
    context = {
        "theshows" : Show.objects.all()
    }
    return render(request, "allshows.html", context)

def addshow(request):
    return render(request, 'addshow.html')

def createshow(request):
    print(request.POST)
    newShow = Show.objects.create(title=request.POST['title'], network=request.POST['net'], description= request.POST['desc'], release_date=request.POST['release'])
    return redirect(f'/shows/{newShow.id}')

def showpage(request, x):
    currentShow = Show.objects.get(id = x)
    context = {
        'number': currentShow.id,
        'showtitle': currentShow.title,
        'shownetwork': currentShow.network,
        'showreleasedate': currentShow.release_date,
        'showdescription': currentShow.description,
        'showLastUpdated': currentShow.updated_at,
    }
    return render(request, 'tvshow.html', context)

def editShow(request, x):
    showToEdit = Show.objects.get(id = x)
    context = {
        'currShow': showToEdit
    }
    return render(request, 'editshow.html', context)

def updateShow(request, x):
    showToUpdate = Show.objects.get(id = x)
    showToUpdate.title = request.POST['title']
    showToUpdate.network = request.POST['net']
    showToUpdate.description = request.POST['desc']
    showToUpdate.release_date = request.POST['release']
    showToUpdate.save()
    print(request.POST)
    return redirect(f'/shows/{x}')

def destroy(request, x):
    showtodelete = Show.objects.get(id = x)
    showtodelete.delete()
    return redirect('/shows')
