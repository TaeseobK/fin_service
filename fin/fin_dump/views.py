from prometheus_client import generate_latest, REGISTRY
from django.http import HttpResponse

# Endpoint untuk expose metrics ke Prometheus
def metrics_view(request):
    return HttpResponse(generate_latest(REGISTRY), content_type="text/plain; charset=utf-8")