from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    Organizador: int = Field(default=123, validate_default=True)
    Ano_Mes: str = Field(default=123, validate_default=True)
    Dia_da_Semana: str = Field(default=123, validate_default=True)
    Tipo_Dia: str = Field(default=123, validate_default=True)
    Objetivo: str = Field(default=123, validate_default=True)
    Date: str = Field(default=123, validate_default=True)
    AdSet_name: Optional[str] = Field(default=123, validate_default=True)
    Amount_spent: float = Field(default=123, validate_default=True)
    Link_clicks: Optional[int] = Field(default=123, validate_default=True)
    Impressions: int = Field(default=123, validate_default=True)
    Conversions: Optional[int] = Field(default=123, validate_default=True)
    Segmentação: Optional[str] = Field(default=123, validate_default=True)
    Tipo_de_Anúncio: str = Field(default=123, validate_default=True)
    Fase: str = Field(default=123, validate_default=True)
