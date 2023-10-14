from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/index.html')

def test_page(request):
    context = {
        'test' : [1,2,3,4,5,6],
    }
    return render(request, 'main/test.html',context=context)