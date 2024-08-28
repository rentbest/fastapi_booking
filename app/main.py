from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as bookings_router
from app.users.router import router as users_router
from app.hotels.router import router as hotels_router
from app.rooms.router import router as rooms_router

from app.pages.router import router as pages_router
from app.images.router import router as images_router

from app.cache import lifespan

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(users_router)
app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(pages_router)
app.include_router(images_router)