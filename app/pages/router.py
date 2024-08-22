from fastapi import APIRouter, Request, Depends 
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],  
)


templates = Jinja2Templates(directory="app/templates")


@router.get("/hotels")
async def get_hotels_page(
    request: Request,
    hotels=Depends(get_hotels),
):
    return templates.TemplateResponse(
        name="hotels.html",
        context={"request": request, "hotels": hotels}
    )