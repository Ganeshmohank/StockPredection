from fastapi import APIRouter, HTTPException
from models.portfolio import PortfolioRequest, PortfolioResponse
from services.portfolio_service import generate_portfolio

router = APIRouter()

@router.post("/suggest", response_model=PortfolioResponse)
def suggest_portfolio(req: PortfolioRequest):
    try:
        portfolio, total_value, history, sector_allocations = generate_portfolio(
            req.amount, req.strategies
        )
        return {
            "portfolio": portfolio,
            "total_value": total_value,
            "history": history,
            "sector_allocations": sector_allocations
        }
    except Exception as e:
        print("❌ ERROR:", e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")
