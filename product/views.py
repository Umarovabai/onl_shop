import rest_framework.pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Product, Category, Comment
from .permissions import IsAdmin, IsAuthor
from .serializers import ProductSerializer, ProductsListSerializer, CategorySerializer
from rest_framework.decorators import api_view, action

# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many = True)
#
#     return Response(serializer.data)
#
# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

# CRUD (Create, Retrieve(получение), Update, Delete)

# class ProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer
#
# class ProductDetailsView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class UpdateProductView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class DeleteProductView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
from .filters import ProductFilter
from .serializers import CommentSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#
# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdmin]
    # pagination_class = rest_framework.pagination.PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    # api/v1/products/id/comments/
    @action(['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    # def get_permissions(self):
    #     if self.action == 'comment':
    #         return []
    #     return [IsAdmin()]



    # api1/v1/products/1/comment
    # @action(['POST'], detail=True)
    # def comment(self, request, pk):
    #     product = self.get_object()
    #     data = {'product': product.id}
    #     data.update(request.data)
    #     serializer = CommentSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Комментарий успешно создан', status=201)




class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]



# class CreateCommentView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class UpdateCommentView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor]
#
# class DeleteCommentView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor | IsAdmin]

class CommentViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]




# TODO: Комментарии к продуктам
# TODO: Фильтрация продуктов
# TODO: Поиск по продуктам
# TODO: Пагинация
# TODO: Заказы
# TODO: Тесты
# TODO: GIT
# TODO: Документация

# API (Application Programming Interface) - интерфейс для взаимодествия программ

# RESTful API - API, отвечающий стилю Rest (архитектурный стиль, набор каких то правил для построения приложения)
# Правила
# 1. отсутствие момтояния клиента( на сервере не хранятся данные о том, залогинен пользователь или нет)