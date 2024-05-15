from pydantic import BaseModel

class GamedataRequest(BaseModel):
    criancaUUID: str
    especialistaId: str
    jogoId: int
    numeroFase: int
    dificuldadeFase: int
    numeroAcertos: int
    numeroErros: int
    tempoSessao: int
    tempoSessaoF: float
    habilidadeTrabalhada: str
    plataforma: str
    condicoesAdequadas: str