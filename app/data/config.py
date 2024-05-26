from typing import Any, Optional

from pydantic import Field, field_validator, PostgresDsn, RedisDsn, ValidationInfo
from pydantic_settings import BaseSettings
from yarl import URL


class DefaultSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_prefix = "BOT_"
        env_file_encoding = "utf-8"

    VERSION: str = "1.0.0"

    DEBUG: bool = Field(default=False)
    LOGGING_LEVEL: int = Field(
        default=20
    )  # read here - https://docs.python.org/3/library/logging.html#levels

    @field_validator("LOGGING_LEVEL", mode="before")
    def set_logging_level(cls, v: Optional[int], info: ValidationInfo):
        if info.data.get("DEBUG"):
            return 10

        if isinstance(v, int):
            return v

    USE_WEBHOOK: bool = Field(default=False)

    MAIN_WEBHOOK_ADDRESS: Optional[str] = Field(default=None)
    MAIN_WEBHOOK_SECRET_TOKEN: Optional[str] = Field(default=None)

    MAIN_WEBHOOK_LISTENING_HOST: Optional[str] = Field(default=None)
    MAIN_WEBHOOK_LISTENING_PORT: Optional[int] = Field(default=None)

    MAX_UPDATES_IN_QUEUE: Optional[int] = Field(default=None)

    TOKEN: str = Field(default="need_token")

    REDIS_BASE: str = ""
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = Field(default=6379)
    REDIS_PASSWORD: Optional[str] = None
    REDIS_USER: Optional[str] = None

    REDIS_CACHE_DB: int = Field(default=5)
    REDIS_STORAGE_DB: int = Field(default=3)

    MONGODB_HOST: str = "localhost"
    MONGODB_PORT: int = Field(default=27017)
    MONGODB_DATABASE: str = Field(default="sampleDB")

    @property
    def REDIS_URI(self) -> URL:
        """
        Assemble REDIS URL from settings.

        :return: redis URL.
        """
        path = ""
        if self.REDIS_BASE is not None:
            path = f"/{self.REDIS_BASE}"
        return URL.build(
            scheme="redis",
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            user=self.REDIS_USER,
            password=self.REDIS_PASSWORD,
            path=path,
        )

    @property
    def MONGODB_URI(self) -> URL:
        return URL.build(
            scheme="mongodb",
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
        )
