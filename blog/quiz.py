from django.shortcuts import render_to_response

def test1(request):
    return render_to_response('test1.html')
