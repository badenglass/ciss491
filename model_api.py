from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# regression coefficients
INTERCEPT = 4554.019897
B_RATING = -4.661275474
B_EVENTS = -3970.769561
B_INTERACTION = 4.203271496


class PlayerInput(BaseModel):
    rating: float
    events_played: float


@app.post("/predict")
def predict(data: PlayerInput):

    interaction = data.rating * data.events_played

    predicted_points = (
        INTERCEPT
        + B_RATING * data.rating
        + B_EVENTS * data.events_played
        + B_INTERACTION * interaction
    )

    return {
        "rating": data.rating,
        "events_played": data.events_played,
        "predicted_points": round(predicted_points, 2)
    }
