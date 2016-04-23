from django.shortcuts import render
from Proxys.tables import HttpProxyTable
from Proxys.models import HttpProxy
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
def http_proxy_view(request):
    query = "SELECT t1.id, t1.nick_name, t1.hash_id, 'http://' || t1.lan_ip || ':8080' as lan_ip, t1.modified_datetime, t1.status \
             FROM Proxys_httpproxy t1 \
             JOIN (SELECT hash_id, MAX(modified_datetime) modified_datetime \
                   FROM Proxys_httpproxy \
                   GROUP BY hash_id) t2 \
             ON t1.hash_id = t2.hash_id AND t1.modified_datetime = t2.modified_datetime \
             ORDER BY t1.modified_datetime DESC;"

    http_proxy_list = HttpProxy.objects.raw(query)
    data_list = []
    for item in http_proxy_list:
        item.modified_datetime = item.modified_datetime.astimezone(timezone.get_current_timezone())
        data_list.append(item)
    http_proxy_table = HttpProxyTable(data_list)
    return render(request, "index.html", {'http_proxy_table': http_proxy_table})

def get_data_view(request):
    lan_ip = request.GET["lan_ip"]
    hash_id = request.GET["hash_id"]
    status = request.GET["status"].lower() == "true"
    HttpProxy(lan_ip = lan_ip, hash_id = hash_id, status = status).save()
    return JsonResponse({"status": "success"}) 

