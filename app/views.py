from django.shortcuts import render

# Create your views here.
def doors(request):
    return render(request,'doors.html')
def signpage(request):
    return render(request,'signpage.html')
def universal(request):
    return render(request,'universal.html')
def rotate(request):
    return render(request,'rotate.html')
