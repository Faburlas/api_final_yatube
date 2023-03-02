from rest_framework import mixins, viewsets


class CreateRetriveListViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    pass
