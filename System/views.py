from System.models import usuarios, veiculos, agendamento_fix, manutencoes, registro_km, alerta
from System.serializers import UsuariosSerializer, VeiculosSerializer, AgendamentoSerializer, ManutencaoSerializer, RegistroSerializer, AlertaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def casdastro_pessoas(request):
    cadastros = usuarios.objects.all()
    serializer = UsuariosSerializer(cadastros, many=True)
    return Response(serializer.data)