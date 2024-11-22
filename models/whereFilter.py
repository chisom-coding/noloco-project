from pydantic import BaseModel
from typing import Dict, Any

class WhereFilter(BaseModel):
    where: Dict[str,Dict[str, Any]]