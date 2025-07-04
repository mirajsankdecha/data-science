from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr'],
        'data1': [10, 20, 30, 25],
        'data2': [5, 15, 10, 20],
    })
