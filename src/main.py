from fastapi import FastAPI
from routers import items

app = FastAPI()

# Include the router from items.py
app.include_router(items.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
