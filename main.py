from fastapi import FastAPI
from database import engine, Base
from routers import auth, contacts

# Buat semua tabel otomatis saat aplikasi start
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Buku Kontak API",
    description="Microservice RESTful API untuk manajemen buku kontak pribadi",
    version="1.0.0"
)

# Daftarkan semua router
app.include_router(auth.router)
app.include_router(contacts.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Selamat datang di Buku Kontak API!", "docs": "/docs"}