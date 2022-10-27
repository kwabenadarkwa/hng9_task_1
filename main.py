from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def root():
    return({
        "slackUsername":"darkwak",
        "backend":True,
        "age":22,
        "bio":"here to have fun"
    })