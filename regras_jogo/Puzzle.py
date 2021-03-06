from regras_jogo.regras_abstratas import AbstractRegrasJogo
from regras_jogo.personagens import Personagens
from random import randint
class Puzzle(AbstractRegrasJogo):
    
    def __init__(self):
        
        #self.elementos = [randint(0, 8) for _ in range(8)]
        
        
        
        self.elementos = []
        while len(self.elementos) < 9:
            aux = randint(0,8)
            if aux not in self.elementos:
                self.elementos.append(aux)
        
        self.pontuacao = 0
        #print('tamanho'+str(len(self.elementos)))

    def registrarAgentePersonagem(self, personagem=Personagens.O_JOGADOR):
        """ Só há um agente, o jogador, então não preciso de lógica.
        """
        return 1
    
    def isFim(self):
        """ Se a lista estiver ordenada, fim de jogo.
        """
        
        return all(self.elementos[i] <= self.elementos[i+1]
            for i, _ in enumerate(self.elementos[:-1]))

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        from percepcoes import PercepcoesJogador
        return PercepcoesJogador(tuple(self.elementos))

        #return elementos

    def registrarProximaAcao(self, id_agente, acao):
        """ Como só há um agente atuando no mundo, o próprio jogador, não é
        necessário nenhum mecanismo para guardar ações associadas por agentes
        distintos.
        """
        self.acao_jogador = acao
    
    def atualizarEstado(self, diferencial_tempo):
        """ Não preciso me preocupar com a passagem do tempo, pois só uma
        jogada é feita por vez, e o jogo não muda seu estado sem jogadas.

        Verifico a ação última registrada e atualizado o estado do jogo
        computando-a.
        """
        from acoes import AcoesJogador
        if self.acao_jogador.tipo == AcoesJogador.PERMUTAR:
            i, j = self.acao_jogador.parametros
            self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]
        else:
            raise TypeError

        self.pontuacao += 1
    
    def terminarJogo(self):
        print(f'Fim de jogo! Sua pontuação foi de {self.pontuacao}.')
