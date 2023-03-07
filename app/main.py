from fastapi import FastAPI,Request
from starlette.middleware.cors import CORSMiddleware
from fastapi_responses import custom_openapi
# from py_common_utils.src.common_utils import log_utils
from app.api.v1.routers import api_router
from app.core.config import settings


# log = log_utils.create_log(__name__)
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.openapi = custom_openapi(app)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)