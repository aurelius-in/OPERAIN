from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	baywalk_base_url: str = Field(..., alias="BAYWALK_BASE_URL")
	perceptionlab_base_url: str = Field(..., alias="PERCEPTIONLAB_BASE_URL")
	edgesight_base_url: str = Field(..., alias="EDGESIGHT_BASE_URL")
	rainlane_base_url: str = Field(..., alias="RAINLANE_BASE_URL")
	drifthawk_base_url: str = Field(..., alias="DRIFTHAWK_BASE_URL")
	webhook_secret: str = Field(..., alias="WEBHOOK_SECRET")

	postgres_host: str = Field("localhost", alias="POSTGRES_HOST")
	postgres_port: int = Field(5432, alias="POSTGRES_PORT")
	postgres_db: str = Field("operain", alias="POSTGRES_DB")
	postgres_user: str = Field("operain", alias="POSTGRES_USER")
	postgres_password: str = Field("operain", alias="POSTGRES_PASSWORD")

	redis_host: str = Field("localhost", alias="REDIS_HOST")
	redis_port: int = Field(6379, alias="REDIS_PORT")
	use_redis: bool = Field(False, alias="USE_REDIS")

	jwt_secret: str = Field(..., alias="JWT_SECRET")
	oauth_issuer_url: Optional[str] = Field(None, alias="OAUTH_ISSUER_URL")
	oauth_client_id: Optional[str] = Field(None, alias="OAUTH_CLIENT_ID")
	oauth_client_secret: Optional[str] = Field(None, alias="OAUTH_CLIENT_SECRET")
	allow_local_login: bool = Field(True, alias="ALLOW_LOCAL_LOGIN")

	locker_bucket_path: str = Field("./_locker_dev", alias="LOCKER_BUCKET_PATH")

	class Config:
		env_file = ".env"
		env_file_encoding = "utf-8"

	@property
	def database_url(self) -> str:
		return (
			f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
			f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
		)


settings = Settings()
