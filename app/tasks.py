import time
import celery
import os

# CELERY_BROKER = os.getenv("CELERY_BROKER")
# CELERY_BACKEND = os.getenv("CELERY_BACKEND")

app = celery.Celery(broker="redis://127.0.0.1:6379/1", backend='redis://127.0.0.1:6379/2')

@app.task
def cpu_bound(a, b):

    time.sleep(1)
    return a + b