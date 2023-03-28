from fastapi import FastAPI

app = FastAPI()

@app.get('/main')
async def test_route():
    return "SALUDOS!! LLEGAMOS AQUI Y AHORA QUE?"

