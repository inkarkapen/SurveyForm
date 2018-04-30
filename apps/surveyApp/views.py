from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'surveyApp/index.html')
def process(request):
    if request.session['times'] == None:
        request.session['times'] = 1
    else:
        if request.method == "POST":
            request.session['times'] += 1
            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comment'] = request.POST['comment']
    return redirect("/result", request)
def result(request):
    return render(request, "surveyApp/result.html")