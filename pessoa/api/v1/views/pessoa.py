from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from pessoa.api.v1.serializers.pessoa import PessoaSerializer
from pessoa.models import Pessoa


class PessoaViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()
    # filter_class = PessoaFilter
    # pagination_class = DefaultPaginationResults

    # def create(self, request, *args, **kwargs):
    #     return super(PessoaViewSet, self).create(request, *args, **kwargs)
    #
    # def list(self, request, *args, **kwargs):
    #     return super(PessoaViewSet, self).list(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     return super(PessoaViewSet, self).update(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     return super(PessoaViewSet, self).retrieve(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super(PessoaViewSet, self).destroy(request, *args, **kwargs)


class Pessoa2ViewSet(viewsets.ModelViewSet):
    pass
