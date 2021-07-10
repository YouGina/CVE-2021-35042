from django.http import HttpResponse
from .models import User
import datetime

def loadexampledata(request):
    html=""
    u=User(name="Admin")
    u.save()
    u=User(name="Moderator")
    u.save()
    u=User(name="Helpdesk")
    u.save()
    return HttpResponse(html)

def users(request):
    now = datetime.datetime.now()
    users = User.objects.order_by(request.GET.get('order_by', 'name'))
    rows = ""
    for user in users:
        rows += "<tr><td>%s</td></tr>" % user.name
    table = "<table><thead><tr><th>Name</th></tr></thead><tbody>%s</tbody></table>" %rows
    html = "<html><body>%s</body></html>" % table
    return HttpResponse(html)
