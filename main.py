from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Base de datos de la memoria
tareas = []

# Modelo de la tarea
class  Tarea(BaseModel):
    id: int
    titulo: str
    completada: bool = False

@app.get("/")
def inicio():
    return {"mensaje:": "Pasele a la API huerco!"}

@app.get("/tareas", response_model = List[Tarea])
def obtener_tareas():
    return tareas

@app.post("/tareas", response_model = Tarea)
def agregar_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

@app.put("/tareas/{id}", response_model = Tarea)
def completar_tarea (id : int):
    for tarea in tareas:
        if tarea.id == id:
            tarea.completada = True
            return tarea
    return {"error": "Tarea no encontrada"}

@app.delete("/tareas/{id}")
def eliminar_tarea(id: int):
    for i, tarea in enumerate(tareas):
        if tarea.id == id:
            tareas.pop(i)
            return{"mensaje": "Tarea eliminada"}
    return{"error": "Tarea no encontrada"}
