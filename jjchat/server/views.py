from rest_framework import viewsets

from .models import Server


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        if category:
            queryset = self.queryset.filter(category=category)
