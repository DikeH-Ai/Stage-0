from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # fastapi instance

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# setup root endpoint


@app.get("/")
async def root():
    # return basic information
    return {
        "email": "onyekachi.okomba@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        "github_url": "https://github.com/DikeH-Ai/Stage-0"
    }
