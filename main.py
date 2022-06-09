from fastapi import FastAPI

app = FastAPI()

@app.get('/main')
async def test_route():
    return "Hi to the sky"

