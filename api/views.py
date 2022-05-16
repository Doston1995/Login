from rest_framework.generics import ListAPIView
from main.models import Blog
from .serializers import BlogSerializer


class BlogApiListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

