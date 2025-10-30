from django.db import models
from django.core.exceptions import ValidationError

# ==========================================
# 			      usuários
# ==========================================
class usuarios(models.Model):
    Nome = models.CharField(max_length=100, null=False)
    Email = models.EmailField(max_length=100, null=False, unique=True)
    Senha = models.CharField(max_length=255, null=False)
    Telefone = models.CharField(max_length=20, null=False, unique=True)
    class cargos(models.TextChoices):
        MECANICO = 'mecanico', 'Mecânico'
        MOTORISTA = 'motorista', 'Motorista'
        ADMINISTRADOR = 'administrador', 'Administrador'
    Cargo = models.CharField(max_length=14, choices=cargos.choices, null=False)

    class Meta:
        db_table = 'Usuarios'

# ==========================================
# 			      veículos
# ==========================================
def validar_placa(value):
    placa = value.upper().replace(' ', '').replace('-', '')
    if len(placa) == 7 and placa[:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5].isnumeric() and placa[6].isnumeric():
        return    
    else:
        raise ValidationError("Essa placa não está dentro dos padrões necesários")

class veiculos(models.Model):
    Marca = models.CharField(max_length= 50, null= False)
    Modelo = models.CharField(max_length= 50, null= False)
    Placa = models.CharField(max_length=7, null=False, validators=[validar_placa], unique=True)
    Km_Atual = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'Veiculos'

# ==========================================
#        agendamento de manutenções
# ==========================================

class agendamento_fix(models.Model):
    Motorista_ID = models.ForeignKey('Usuarios', on_delete=models.SET_NULL, null=True, related_name='agendamentos_como_motorista') 
    Mecanico_ID = models.ForeignKey('Usuarios', on_delete=models.SET_NULL, null=True, related_name='agendamentos_como_mecanico')
    Veiculo_ID = models.ForeignKey('Veiculos', on_delete=models.CASCADE, related_name='agendamentos')
    Data_prevista_manutencao = models.DateField(null=False)
    class tipos(models.TextChoices):
        PREVENTIVA = 'preventiva', 'Preventiva'
        CORRETIVA = 'corretiva', 'Corretiva'
    Tipo = models.CharField(max_length=11, choices=tipos.choices, null=False)
    Motivo = models.CharField(max_length=255)
    Observacoes = models.TextField()
    class Meta:
        db_table = 'Agendamentos'

# ==========================================
#        histórico de manutenções
# ==========================================

class manutencoes(models.Model):
    Motorista_ID = models.ForeignKey('Usuarios', on_delete=models.SET_NULL, null=True, related_name='manutencoes_como_motorista')
    Mecanico_ID = models.ForeignKey('Usuarios', on_delete=models.SET_NULL, null=True, related_name='manutencoes_como_mecanico')
    Veiculo_ID = models.ForeignKey('Veiculos', on_delete=models.CASCADE, related_name='veiculo_consertado')
    Agendamento_ID = models.ForeignKey("Agendamento_fix", on_delete=models.SET_NULL, null=True, related_name='agendamento_fix')
    Km_Manutencao = models.BigIntegerField(null=False, default=0) 
    Km_Proxima_Revisao = models.BigIntegerField(null=True, blank=True)
    Data_RealizacaoManu = models.DateField(null=False)
    class tipos(models.TextChoices):
        PREVENTIVA = 'preventiva', 'Preventiva'
        CORRETIVA = 'corretiva', 'Corretiva'
    Tipo = models.CharField(max_length=11, choices=tipos.choices, null=False)
    Motivo = models.CharField(max_length=255)
    Observacoes = models.TextField()
    Custo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    class Meta:
        db_table = 'Manutencoes'

# ==========================================
#               quilometragem
# ==========================================

class registro_km(models.Model):
    Veiculo_ID = models.ForeignKey('Veiculos', on_delete=models.CASCADE, related_name='registros_km')
    Km_Leitura = models.BigIntegerField(null=False) 
    Motorista_ID = models.ForeignKey('Usuarios', on_delete=models.SET_NULL, null=True)
    Data_Hora_Registro = models.DateTimeField(auto_now_add=True) 
    class fontes(models.TextChoices):
        ABASTECIMENTO = 'abastecimento', 'Abastecimento'
        INICIO_TURNO = 'inicio_turno', 'Início de Turno'
        MECANICO = 'mecanico', 'Mecânico (Check-in)'
    Fonte_Registro = models.CharField(max_length=15, choices=fontes.choices, null=False)

    class Meta:
        db_table = 'RegistrosKM'

# ==========================================
#                 alertas
# ==========================================

class alerta(models.Model):
    class stts(models.TextChoices):
        ATIVO = 'ativo','Ativo'
        RESOLVIDO = 'resolvido','Resolvido'
    Status = models.CharField(max_length=10,choices=stts, null=False)
    Veiculo_ID = models.ForeignKey("Veiculos", on_delete=models.CASCADE, null=False, related_name='alerta_do_veiculo')
    Mensagem = models.TextField()
    class Meta:
        db_table = 'Alerta'

