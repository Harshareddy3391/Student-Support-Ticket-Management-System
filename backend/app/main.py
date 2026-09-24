from fastapi import FastAPI

app = FastAPI(
    title="Student Support & Ticket Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Student Support Ticket Management API is running"
    }