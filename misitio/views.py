from django.http import HttpResponse
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    html = " <html><body>It is now %s .</body></html> " % ahora
    
    return HttpResponse(html)