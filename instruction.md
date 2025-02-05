## Use GCP Secret Manager to hide API key
Store secrets securely in GCP and access them programmatically.

1. Store the API Key in Secret Manager:
```bash
echo -n "your_api_key" | gcloud secrets create GEMINI_API_KEY --data-file=-
```

2. Grant Access to the Secret:
Assign permissions to your Cloud Run service account:
```
gcloud secrets add-iam-policy-binding GEMINI_API_KEY \
  --member="serviceAccount:[YOUR_SERVICE_ACCOUNT_EMAIL]" \
  --role="roles/secretmanager.secretAccessor"
```

3. Access the Secret in Code:
```
from google.cloud import secretmanager

def get_secret(secret_name: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/[PROJECT_ID]/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(request={"name": secret_path})
    return response.payload.data.decode("UTF-8")

api_key = get_secret("GEMINI_API_KEY")
```