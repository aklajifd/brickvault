import httpx
from app.core.config import settings

REBRICKABLE_BASE_URL = "https://rebrickable.com/api/v3/lego"

async def fetch_set_from_rebrickable(set_number: str) -> dict | None:
    set_num = set_number if "-" in set_number else f"{set_number}-1"
    
    url = f"{REBRICKABLE_BASE_URL}/sets/{set_num}/"
    headers = {"Authorization": f"key {settings.rebrickable_api_key}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == 404:
        return None
    
    response.raise_for_status()
    data = response.json()
    
    return {
        "set_number": set_number,
        "name": data["name"],
        "year": data["year"],
        "piece_count": data["num_parts"],
        "image_url": data.get("set_img_url"),
        "rebrickable_theme_id": data.get("theme_id"),
    }
    
async def fetch_theme_from_rebrickable(theme_id: int) -> dict | None:
    url = f"{REBRICKABLE_BASE_URL}/themes/{theme_id}/"
    headers = {"Authorization": f"key {settings.rebrickable_api_key}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == 404:
        return None
    
    response.raise_for_status()
    data = response.json()
    
    return {
        "name": data["name"],
        "rebrickable_id": data["id"],
    }