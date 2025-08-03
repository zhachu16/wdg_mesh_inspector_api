from pydantic import BaseModel, HttpUrl

class MeshInspectRequest(BaseModel):
    mesh_url: HttpUrl

class MeshInspectResponse(BaseModel):
    is_printable: str
    info: dict

class MeshInfoRequest(BaseModel):
    mesh_url: HttpUrl

class MeshInfoResponse(BaseModel):
    x_dim: float
    y_dim: float
    z_dim: float
    weight: float
    estimated_price: float
