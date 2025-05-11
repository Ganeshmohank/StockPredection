from pydantic import BaseModel
from typing import List, Dict

class StrategyWeight(BaseModel):
    name: str
    weight: float

class StockDetail(BaseModel):
    ticker: str
    price: float
    shares: float
    value: float
    sector: str
    description: str
    type: str
    strategy: str
    trend: List[float]

class PortfolioResponse(BaseModel):
    portfolio: List[StockDetail]
    total_value: float
    history: List[float]
    sector_allocations: Dict[str, float]

class PortfolioRequest(BaseModel):
    amount: float
    strategies: List[StrategyWeight]
