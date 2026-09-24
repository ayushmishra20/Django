from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hi welcome !!"}

@app.get("/about")
def about():
    return {"message":"This is the about page."}