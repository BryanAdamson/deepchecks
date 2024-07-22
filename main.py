from fastapi import FastAPI

from app.controllers import alert_controller, interaction_controller
from infrastructure.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(interaction_controller.router, prefix="/api/interactions")
app.include_router(alert_controller.router, prefix="/api/alerts")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
