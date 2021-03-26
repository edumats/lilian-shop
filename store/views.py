from rest_framework import viewsets, permissions, renderers

from .models import Hantem
from .serializers import HantemSerializer
from shop.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hantems': reverse('hantem-list', request=request, format=format),
    })


class HantemViewSet(viewsets.ModelViewSet):
    queryset = Hantem.objects.all()
    serializer_class = HantemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
