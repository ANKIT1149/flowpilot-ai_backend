from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/login")
def login(name: str, email: str):
    if name == "":
        return {"message": "Please fill all detals"}

    return {
        "message": f"Welcome {name} to the flow pilot ai confirm this is your email {email}"
    }
