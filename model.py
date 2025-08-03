from pydantic import BaseModel, HttpUrl


class MeshInspectRequest(BaseModel):
    mesh_url: HttpUrl
    model_config = {
        "json_schema_extra": {
            "example": {
                "mesh_url": "https://raw.githubusercontent.com/zhachu16/wdg_mesh_inspector_api/main/big_sphere_exmaple.stl"
            }
        }
    }


class MeshInspectResponse(BaseModel):
    is_printable: bool
    info: dict
    model_config = {
        "json_schema_extra": {
            "example": {
                "is_printable": True,
                "info": {
                    "Printable": "No obvious fault detected, mesh is likely printable"
                }
            }
        }
    }


class MeshInfoRequest(BaseModel):
    mesh_url: HttpUrl
    model_config = {
        "json_schema_extra": {
            "example": {
                "mesh_url": "https://raw.githubusercontent.com/zhachu16/wdg_mesh_inspector_api/main/small_sphere_example.stl"
            }
        }
    }


class MeshInfoResponse(BaseModel):
    x_dim: float
    y_dim: float
    z_dim: float
    weight: float
    estimated_price: float
    model_config = {
        "json_schema_extra": {
            "example": {
                "x_dim": 120.0,
                "y_dim": 85.0,
                "z_dim": 60.0,
                "weight": 0.153,
                "estimated_price": 42.75
            }
        }
    }
