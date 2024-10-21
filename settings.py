from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8"
  )
  ID: str = "0000000"
  PASSWORD: str = "your_password"
  HOURLY_RATE: int
  ROUND_TRIP_COST: int
  LOGIN_URL: str
  SCRAPE_URL: str
