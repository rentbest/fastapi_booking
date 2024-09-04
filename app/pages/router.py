from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels, get_hotel_by_id
import app.hotels.exceptions as exc


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
        name="hotels.html", context={"request": request, "hotels": hotels}
    )


@router.get("/hotels/{hotel_id}")
async def get_hotel_detail_page(
    request: Request,
    hotel_id: int,
    hotel=Depends(get_hotel_by_id),
):
    if not hotel:
        raise exc.HotelNotFound
    return templates.TemplateResponse(
        name="hotel_detail.html", context={"request": request, "hotel": hotel}
    )
