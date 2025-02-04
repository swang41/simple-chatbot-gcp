from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
from google.cloud import aiplatform  

app = FastAPI()  
aiplatform.init(project="[PROJECT_ID]", location="us-central1")  

class ChatRequest(BaseModel):  
    prompt: str  

@app.post("/chat")  
async def generate_response(request: ChatRequest):  
    try:  
        endpoint = aiplatform.Endpoint(endpoint_name="projects/[PROJECT_ID]/locations/us-central1/endpoints/[ENDPOINT_ID]")  
        response = endpoint.predict(instances=[{"prompt": request.prompt}])  
        return {"response": response.predictions[0]["content"]}  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
