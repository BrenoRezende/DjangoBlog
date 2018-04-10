from rest_framework.response import Response
from rest_framework.decorators import api_view
from artigos.models import Artigo
from artigos.serializers import ArtigoSerializer

@api_view(['GET'])
def artigos_api(request):
    artigos = ArtigoSerializer(Artigo.objects.all(), many=True)
    return Response(artigos.data)
