from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, tasks

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A full-featured Task Manager REST API with authentication. Built with FastAPI + SQLite.",
    version="1.0.0"
)

# Allow frontend apps to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Task Manager API 🚀",
        "docs": "/docs",
        "version": "1.0.0"
    }
