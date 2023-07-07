from rest_framework import permissions, response
from rest_framework.decorators import action
from .models import Product
from .permissions import IsAuthorOrAdmin, IsAuthor
from rest_framework.viewsets import ViewSet
from . import serializers


class ProductViewSet(ViewSet):
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        def get_serializer_class(self):
            if self.action == 'list':
                return serializers.ProductListSerializer
            return serializers.ProductSerializer

        def get_permissions():
            if self.action == 'destroy':
                return [IsAuthorOrAdmin]
            elif self.action in ('update', 'partial_update'):
                return [IsAuthor(), ]
            return [permissions.IsAuthenticatedOrReadOnly]





