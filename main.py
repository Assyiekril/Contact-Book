from fastapi import FastAPI
from database import engine, Base

# Import model dulu agar tabel terbuat
from models.user import User
from models.contact import Contact

from routers import auth, contacts

# Buat semua tabel
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Buku Kontak API",
    description="Microservice RESTful API untuk manajemen buku kontak pribadi",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(contacts.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Selamat datang di Buku Kontak API!", "docs": "/docs"}