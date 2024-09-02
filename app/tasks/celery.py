from celery import Celery
from app.config import settings


celery = Celery(
    main="tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["app.tasks.tasks"],
)