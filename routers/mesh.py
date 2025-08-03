from fastapi import APIRouter, HTTPException
from model import MeshInspectRequest, MeshInspectResponse, MeshInfoRequest, MeshInfoResponse
from core import inspect_mesh, get_mesh_info

router = APIRouter()

@router.post("/get_mesh_inspection_api", response_model=MeshInspectResponse)
def get_mesh_inspection_api(req: MeshInspectRequest):
    try:
        result = inspect_mesh(req.mesh_url)
        return MeshInspectResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/get_mesh_info_api", response_model=MeshInfoResponse)
def get_mesh_info_api(req: MeshInfoRequest):
    try:
        result = get_mesh_info(req.mesh_url)
        return MeshInfoResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
