from System.models import usuarios, veiculos, agendamento_fix, manutencoes, registro_km, alerta
from rest_framework import serializers
from django.contrib.auth.hashers import make_password 



class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'Nome', 'Email', 'Senha', 'Telefone', 'Cargo']
        extra_kwargs = {'Senha': {'write_only': True}} 

    def create(self, validated_data):
        validated_data['Senha'] = make_password(validated_data.get('Senha'))
        return super().create(validated_data)

class VeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = veiculos
        fields = ['id', 'Marca', 'Modelo', 'Placa', 'Km_Atual']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamento_fix
        fields = ['id','Motorista_ID','Mecanico_ID', 'Veiculo_ID', 
                  'Data_prevista_manutencao', 'Tipo', 'Motivo', 'Observacoes']

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = manutencoes
        fields = ['id', 'Motorista_ID', 'Mecanico_ID', 'Veiculo_ID',
                  'Agendamento_ID', 'Km_Manutencao', 'Km_Proxima_Revisao',
                  'Data_RealizacaoManu', 'Tipo', 'Motivo',
                  'Observacoes', 'Custo']

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = registro_km
        fields = ['id', 'Veiculo_ID', 'Km_Leitura', 'Motorista_Id',
                  'Data_Hora_Registro', 'Fonte_Registro']

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = alerta
        fields = ['id', 'Status', 'Veiculo_ID', 'Mensagem', ]