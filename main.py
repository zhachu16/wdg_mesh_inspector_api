from fastapi import FastAPI
from routers import mesh
import uvicorn

app = FastAPI(
    title="Mesh Inspection API",
    description="API to inspect 3D meshes for printability, dimensions, weight and estimated cost",
    version="1.0.0"
)

app.include_router(mesh.router, prefix="/mesh", tags=["Mesh Operations"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)