from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import random

load_dotenv()

TEMPERATURE_SCALE = os.environ.get('TEMPERATURE_SCALE')
SPEED_SCALE = os.environ.get('SPEED_SCALE')

app = FastAPI()

# Configurazione CORS per permettere tutte le origini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permetti tutte le origini
    allow_credentials=True,
    allow_methods=["GET"],  # Permetti tutti i metodi (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permetti tutti gli header
)


@app.get("/")
def sanity() -> int:
    return 1

@app.get("/getSpeed")
def getSpeed() -> dict:
    scale : str

    if SPEED_SCALE == "KILOMETER":
        scale = "km/h"
    else:
        scale = "m/h"

    return {"Speed": random.randrange(10, 130), "Scale": scale}

@app.get("/getTemperature")
def getTemperature() -> dict:
    scale : str

    if TEMPERATURE_SCALE == "CELSIUS":
        scale = "°"
    else:
        scale = "f"

    return {"Temp": random.randrange(-10, 46), "Scale": scale}