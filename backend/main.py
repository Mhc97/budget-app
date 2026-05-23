from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Budget API fonctionne 🎉"}

@app.get("/expenses")
def get_expenses():
    return [
        {"id": 1, "title": "Courses", "amount": 45, "category": "food"},
        {"id": 2, "title": "Cinéma", "amount": 12, "category": "leisure"}
    ]
