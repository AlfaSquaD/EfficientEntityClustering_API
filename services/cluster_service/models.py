from pydantic import BaseModel


class ClusterIn(BaseModel):
    cluster_id: str
    cluster_name: str

class ClusterAddEntityIn(BaseModel):
    cluster_id: str
    entity_ids: list[str]


class ClusterOut(BaseModel):
    cluster_id: str
    cluster_name: str
    entity_ids: list[str]
    cluster_vector: list[float]
