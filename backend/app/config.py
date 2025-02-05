import os
from google.cloud import secretmanager
from google.api_core.exceptions import NotFound

def get_secret(secret_name: str, project_id: str = None) -> str:
    """Fetches secrets from GCP Secret Manager or .env."""
    # Check if running in production (Cloud Run)
    if os.getenv("K_SERVICE"):
        client = secretmanager.SecretManagerServiceClient()
        secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": secret_path})
        return response.payload.data.decode("UTF-8")
    
    # Local development: Use .env or environment variables
    return os.getenv(secret_name)