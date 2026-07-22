from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes.auth_routes import auth_router
from app.routes.user_routes import user_router
from app.routes.stats_routes import stats_router
from app.routes.seed_routes import seed_router
from app.routes.contact_routes import contact_router

# Import all models to ensure they are registered with SQLAlchemy
from app.models.users import *  # noqa: F401
from app.models.contacts import *  # noqa: F401
from app.models.notes import *  # noqa: F401
from app.models.interactions import *  # noqa: F401

app = FastAPI()

# CORS (required for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health endpoint (required for deployment health checks)
@app.get("/health")
def health():
    return {"status": "ok"}

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(stats_router)
app.include_router(seed_router)
app.include_router(contact_router)