from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from main import main
app = FastAPI()

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
def estimate(request: EstimationRequest):
    result = main(
        salary=request.salary,
        productivity=request.productivity,
        min_loc=request.min_loc,
        max_loc=request.max_loc,
        coding_language=request.coding_language,
        project_type=request.project_type,
        min_fp=request.min_fp,
        max_fp=request.max_fp,
        external_inputs=request.external_inputs,
        external_outputs=request.external_outputs,
        inquiries=request.inquiries,
        external_files=request.external_files,
        internal_files=request.internal_files,
        min_test_cases=request.min_test_cases,
        max_test_cases=request.max_test_cases,
        min_success_rate=request.min_success_rate,
        max_success_rate=request.max_success_rate,
        min_internal_cost=request.min_internal_cost,
        max_internal_cost=request.max_internal_cost,
        external_resources=request.external_resources,
        min_external_cost=request.min_external_cost,
        max_external_cost=request.max_external_cost,
        num_simulations=request.num_simulations
    )
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



#! API POST request body at URL : http://127.0.0.1:8000/estimate

# {
#     "salary": 50000,
#     "productivity": 100,
#     "min_loc": 10000,
#     "max_loc": 20000,
#     "coding_language": "python",
#     "project_type": "Embedded",
#     "min_fp": 100,
#     "max_fp": 200,
#     "external_inputs": 10,
#     "external_outputs": 10,
#     "inquiries": 5,
#     "external_files": 3,
#     "internal_files": 5,
#     "min_test_cases": 500,
#     "max_test_cases": 1000,
#     "min_success_rate": 0.8,
#     "max_success_rate": 0.9,
#     "min_internal_cost": 100000,
#     "max_internal_cost": 200000,
#     "external_resources": false,
#     "min_external_cost": 20000,
#     "max_external_cost": 50000,
#     "num_simulations": 1000
# }


