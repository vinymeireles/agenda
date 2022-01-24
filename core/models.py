from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#classe que será migrada para o banco de dados como tabela
class Evento(models.Model): 
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #insere a hora atual no campo
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #usuario com atributo de chave estrangeira

    class Meta:
        db_table = 'evento' #table passara a ser chamar 'evento'

    def __str__(self):
        return self.titulo #atualizando o nome do evento object para o titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M hrs')    #formatar a data e hora evento para o padrao brasileiro (D/M/Y h:m)