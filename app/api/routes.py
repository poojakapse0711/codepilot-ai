from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/", tags=["Application"])
async def root():
    """Root endpoint."""
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


@router.get("/health", tags=["Application"])
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
    }