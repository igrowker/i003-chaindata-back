# application runner
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from database.session import engine
from routers.user import userRouter
from models import user
from const import OPEN_API_TITLE, OPEN_API_DESCRIPTION, VERSION

user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=VERSION,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(userRouter)

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")
