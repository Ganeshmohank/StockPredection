from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.portfolio_routes import router as portfolio_router

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Route registration
app.include_router(portfolio_router, prefix="/api/portfolio")
