from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    app_name: str = "BrickVault"
    debug: bool = False
    rebrickable_api_key: str = ""
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_jwt_secret: str = ""

    class Config:
        env_file = ".env"

settings = Settings()