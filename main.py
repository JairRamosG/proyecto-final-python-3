from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class  Valores(BaseModel):
    region: str
    generacion: float
    demanda: float
    diferencia : float
    fecha: str    

@app.get("/")
async def index():
    return {"messaje" : "Hello World!"}

@app.get("/leer_registros/")
async def leer_registros():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT region, generacion, demanda, diferencia, fecha FROM info_dia")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"Región ": resultado[0], "Generación MW ": resultado[1], "Demanda MW ": resultado[2], "Diferencia MW ": resultado[3], "Fecha ": resultado[4]} for resultado in resultados]
    else:
        return {"Mensaje" : "No hay registros en la base"}

@app.get("/leer_registro/{id}/")
async def leer_registro(id: int):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT region, generacion, demanda, diferencia, fecha FROM info_dia WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return {"Región ": resultado[0], "Generación MW ": resultado[1], "Demanda MW ": resultado[2], "Diferencia MW ": resultado[3], "Fecha ": resultado[4]}
    else:
        return {"Mensaje": "Registro no encontrado en la base"}
    
@app.get("/regiones/{region}/")
async def leer_registro(region: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT generacion, demanda, diferencia, fecha FROM info_dia WHERE region = ?", (region,))
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"Generación MW ": resultado[0], "Demanda MW ": resultado[1], "Diferencia MW ": resultado[2], "Fecha ": resultado[3]} for resultado in resultados]
    else:
        return {"Mensaje": "El nombre de la región no es válido"}