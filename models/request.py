from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class GamedataModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    criancaUUID: str =  Field(...)
    especialistaId: str =  Field(...)
    jogoId: int =  Field(...)
    numeroFase: int =  Field(...)
    dificuldadeFase: int =  Field(...)
    numeroAcertos: int =  Field(...)
    numeroErros: int =  Field(...)
    tempoSessao: int =  Field(...)
    tempoSessaoF: float =  Field(...)
    habilidadeTrabalhada: str =  Field(...)
    plataforma: str =  Field(...)
    condicoesAdequadas: str =  Field(...)

class PlayerdataModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nomeCrianca: str =  Field(...)
    nomeResponsavel1: str =  Field(...)
    nomeResponsavel2: str =  Field(...)
    especialistaId: str =  Field(...)
    terapeutaId: str =  Field(...)
    escolaridade: str =  Field(...)
    idade: int =  Field(...)
    cidade: str =  Field(...)
    nivelEstudos: int =  Field(...)