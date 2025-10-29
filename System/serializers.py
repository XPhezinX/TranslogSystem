from System.models import usuarios, veiculos, agendamento_fix, manutencoes, alerta
from rest_framework import serializers


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'Nome', 'Email', 'Senha', 'Telefone', 'Cargo']

class VeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = veiculos
        fields = ['id', 'Marca', 'Modelo', 'Placa']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamento_fix
        fields = ['id','Motorista_ID','Mecanico_ID', 'Veiculo_ID', 
                  'Data_prevista_manutencao', 'Tipo', 'Motivo', 'Observacoes']

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = manutencoes
        fields = ['id', 'Motorista_ID', 'Mecanico_ID', 'Veiculo_ID'
                  'Agendamento_ID', 'Data_RealizacaoManu', 'Tipo',
                    'Motivo', 'Observacoes', 'Custo']


class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = alerta
        fields = ['id', 'Status', 'Veiculo_ID', 'Mensagem', ]