from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/who")
def who():
    return "Thomas RIPOLL"

@app.get("/api/data")
def get_data():
    return {"data": ["item1", "item2"]}

if __name__ == "__main__":
    import uvicorn
    # Le port attribué reste 8001
    uvicorn.run(app, host="0.0.0.0", port=8023)