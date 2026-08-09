import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "instance" / "staffhub.db"

# SECRET_KEY should be set via the SECRET_KEY environment variable outside of
# local development or grading. The fallback below is a development-only
# default and is not suitable for a production deployment.
SECRET_KEY = os.environ.get("SECRET_KEY", "staffhub-starter-development-key")
