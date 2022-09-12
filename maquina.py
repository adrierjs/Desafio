class Estados:
    def __init__(self, estado = None, transicao = None):
        self.transicao = transicao
        if not estado:
            self.estado = "acordado"
        else:
            self.estado = estado

    def verificarTransicao(self):
        if self.estado == "acordado":
            print("08:00")
        elif self.estado == "trabalhando":
            print("12:00 / 18:00")
        elif self.estado == "descansando":
            print("13:00 / 22:00")
        elif self.estado == "dormindo":
            print("não há transições disponíveis")
        else:
            print("não há transições disponíveis")

    def alterarTransicao(self, transicao):
        if transicao == "08:00" and self.estado == "acordado":
            self.transicao = transicao
            self.estado = "trabalhando"
        elif transicao == "12:00" and self.estado =="trabalhando" or transicao == "18:00" and self.estado=="trabalhando":
            self.transicao = transicao
            self.estado = "descansando"
        elif transicao == "13:00" and self.estado == "descansando":
            self.transicao = transicao
            self.estado = "trabalhando"
        elif transicao == "22:00" and self.estado == "descansando":
            self.transicao = transicao
            self.estado = "dormindo"
        else:
            raise IndexError("Transição não disponível")
        self.imprimeStatus()

    def imprimeStatus(self):
        print("Estado: ", self.estado,"\nTransição:", self.transicao)

