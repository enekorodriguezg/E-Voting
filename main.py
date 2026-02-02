from fastapi import FastAPI

# --- ESTA ES LA LÍNEA CLAVE ---
# La variable TIENE que llamarse 'app' porque así lo pusiste en el Dockerfile
app = FastAPI() 
# ------------------------------

@app.get("/")
def read_root():
    return {"mensaje": "Hola, soy tu Sistema de Votación funcionando en Docker"}