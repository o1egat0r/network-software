from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()
profiles_db: Dict[str, dict] = {}

def next_state(state: str, event: str) -> str:
    if "FAIL" in event or event == "CANCEL":
        return "CANCELLED"
    
    transitions = {
        ("NEW", "PAY_OK"): "PAID",
        ("PAID", "RESERVE_OK"): "DONE",
    }

    return transitions.get((state, event), state)

class ProfileCreate(BaseModel):
    name: str
    phone: str

@app.post("/api/profiles/saga")
async def start_saga(data: ProfileCreate):
    profile_id = str(uuid.uuid4())
    current_state = "NEW"
    
    if "666" in data.phone:
        current_state = next_state(current_state, "PAY_FAIL")
    else:
        current_state = next_state(current_state, "PAY_OK")

        current_state = next_state(current_state, "RESERVE_OK")

    profiles_db[profile_id] = {
        "id": profile_id,
        "name": data.name,
        "phone": data.phone,
        "status": current_state
    }
    
    return profiles_db[profile_id]

@app.get("/api/profiles/{profile_id}")
async def get_profile(profile_id: str):
    if profile_id not in profiles_db:
        raise HTTPException(status_code=404, detail="Not found")
    return profiles_db[profile_id]

@app.get("/health")
async def health():
    return {"status": "ok", "project": "profiles-s05"}