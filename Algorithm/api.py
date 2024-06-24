from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from main import main
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the origins that should be allowed
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define the request model
class EstimationRequest(BaseModel):
    salary: int
    productivity: int
    min_loc: int
    max_loc: int
    coding_language: str
    project_type: str
    min_fp: int
    max_fp: int
    external_inputs: int
    external_outputs: int
    inquiries: int
    external_files: int
    internal_files: int
    min_test_cases: int
    max_test_cases: int
    min_success_rate: float
    max_success_rate: float
    min_internal_cost: int
    max_internal_cost: int
    external_resources: Optional[bool] = False
    min_external_cost: Optional[int] = 0
    max_external_cost: Optional[int] = 0
    num_simulations: Optional[int] = 1000

# Define the response model
class EstimationResponse(BaseModel):
    loc_array: List[List[float]]
    loc_mean: float
    time_array: List[List[float]]
    time_mean: float
    complexity_array: List[List[float]]
    complexity_mean: float
    num_people_array: List[List[float]]
    num_people_mean: float
    cost_array: List[List[float]]
    cost_mean: float
    code_coverage_array: List[List[float]]
    code_coverage_mean: float
    risk_array: List[List[float]]
    risk_mean: float

@app.post("/estimate", response_model=EstimationResponse)
async def estimate(request: Request):
    try:
        request_data = await request.json()
        logger.info("Incoming request data: %s", request_data)
        estimation_request = EstimationRequest(**request_data)
    except ValidationError as e:
        logger.error("Validation error: %s", e.json())
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        logger.error("Error parsing request: %s", e)
        raise HTTPException(status_code=400, detail="Invalid request data")

    try:
        result = main(
            salary=estimation_request.salary,
            productivity=estimation_request.productivity,
            min_loc=estimation_request.min_loc,
            max_loc=estimation_request.max_loc,
            coding_language=estimation_request.coding_language,
            project_type=estimation_request.project_type,
            min_fp=estimation_request.min_fp,
            max_fp=estimation_request.max_fp,
            external_inputs=estimation_request.external_inputs,
            external_outputs=estimation_request.external_outputs,
            inquiries=estimation_request.inquiries,
            external_files=estimation_request.external_files,
            internal_files=estimation_request.internal_files,
            min_test_cases=estimation_request.min_test_cases,
            max_test_cases=estimation_request.max_test_cases,
            min_success_rate=estimation_request.min_success_rate,
            max_success_rate=estimation_request.max_success_rate,
            min_internal_cost=estimation_request.min_internal_cost,
            max_internal_cost=estimation_request.max_internal_cost,
            external_resources=estimation_request.external_resources,
            min_external_cost=estimation_request.min_external_cost,
            max_external_cost=estimation_request.max_external_cost,
            num_simulations=estimation_request.num_simulations
        )
    except Exception as e:
        logger.error("Error during estimation: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error")

    return EstimationResponse(
        loc_array=result[0],
        loc_mean=result[1],
        time_array=result[2],
        time_mean=result[3],
        complexity_array=result[4],
        complexity_mean=result[5],
        num_people_array=result[6],
        num_people_mean=result[7],
        cost_array=result[8],
        cost_mean=result[9],
        code_coverage_array=result[10],
        code_coverage_mean=result[11],
        risk_array=result[12],
        risk_mean=result[13]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
