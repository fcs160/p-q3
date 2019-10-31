from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "%s - %s" % (self.nome, self.telefone)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ("nome",)


class ItemTema(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField("descrição")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"
        ordering = ("nome",)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=70)
    numero = models.IntegerField("número")
    complemento = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    cidade = models.CharField(max_length=20)
    UF_CHOICES = [("AC", "AC"),
                  ("AL", "AL"),
                  ("AM", "AM"),
                  ("AP", "AP"),
                  ("BA", "BA"),
                  ("CE", "CE"),
                  ("DF", "DF"),
                  ("ES", "GO"),
                  ("MA", "MA"),
                  ("MG", "MG"),
                  ("MS", "MS"),
                  ("MT", "MT"),
                  ("PA", "PA"),
                  ("PB", "PB"),
                  ("PE", "PE"),
                  ("PI", "PI"),
                  ("PR", "PR"),
                  ("RJ", "RJ"),
                  ("RN", "RN"),
                  ("RO", "RO"),
                  ("RR", "RR"),
                  ("RS", "RS"),
                  ("SC", "SC"),
                  ("SE", "SE"),
                  ("SP", "SP"),
                  ("TO", "TO")
                  ]
    uf = models.CharField("UF", max_length=2, choices=UF_CHOICES)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.cep

    class Meta:
        verbose_name = "endereço"
        verbose_name_plural = "endereços"
        ordering = ("bairro", "cidade", "uf")


class Tema(models.Model):
    nome = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField("Valor do aluguel", max_digits=7, decimal_places=2)
    cor_toalha = models.CharField(max_length=20)
    item = models.ManyToManyField(ItemTema)

    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"
        ordering = ("nome", "valor_aluguel")

    def __str__(self):
        return "%s - R$%.2f " % (self.nome, self.valor_aluguel)


class Aluguel(models.Model):
    data_festa = models.DateField("Data da festa")
    hora_inicio = models.TimeField("Horário do ínicio")
    hora_termino = models.TimeField("Horário do término")
    valor_cobrado = models.DecimalField(max_digits=7, decimal_places=2)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.OneToOneField("Endereco", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"

    def __str__(self):
        return "%s - R$%.2f" % (self.data_festa.strftime("%d/%m/%Y"), self.valor_cobrado)
