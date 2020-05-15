from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    permutar = 'PERMUTAR'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def permutar(cls, i,j):
        return cls(AcoesJogador.permutar, (i,j))