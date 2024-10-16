from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "watch_data_system",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.tasks.scraping_tasks", "app.tasks.update_vectorstore_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
