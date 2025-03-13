from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MODEL_ID: str

    class Config:
        env_file = ".env"

    def __init__(self, **data):
        # Strip whitespace from string values
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        super().__init__(**data)

settings = Settings()