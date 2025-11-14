from datetime import date

class Tarefa:
    def __init__(self, titulo: str, descricao: str, prazo: date, prioridade: int):
        self.titulo = titulo               
        self.descricao = descricao         
        self.data_da_criacao = date.today()
        self._prazo = prazo                
        self._status = False
        self._prioridade = prioridade              

    @property
    def prazo(self):
        return self._prazo
    @prazo.setter
    def prazo(self, novo_prazo: date):
        if novo_prazo < self.data_da_criacao:
            raise ValueError("O prazo não pode ser antes da data de criação.")
        self._prazo = novo_prazo

    @property
    def status(self):
        return self._status

    def concluir(self):
        self._status = True

    def __repr__(self):
        status = "Concluída" if self._status else "Pendente"
    
        prioridades = {
            0: "Urgente",
            1: "Alta",
            2: "Média",
            3: "Baixa"
        }
        prioridade_texto = prioridades.get(self._prioridade, "Desconhecida")

        return (
            f"Tarefa(titulo='{self.titulo}', "
            f"status='{status}', "
            f"prioridade='{prioridade_texto}', "
            f"prazo={self._prazo}, "
            f"criada_em={self.data_da_criacao})"
        )


    @property
    def prioridade(self):
        return self._prioridade
    @prioridade.setter
    def prioridade(self, nova_prioridade):
        if type(nova_prioridade) != int:
            raise ValueError('A prioridade deve ser um número inteiro')
        elif nova_prioridade > 3 or nova_prioridade < 0:
            raise ValueError('A prioridade deve ser <= 3 e >= 0')
        else:
            self._prioridade = nova_prioridade
        
            

        

    


        
