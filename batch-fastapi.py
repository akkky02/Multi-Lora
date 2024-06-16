import asyncio
import json

import aiohttp
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from lorax import AsyncClient  # Import the AsyncClient

app = FastAPI()

# Configuration
LORAX_ENDPOINT = "http://127.0.0.1:8080"  # Replace with your LoRAX server endpoint
CALLBACK_URL = (
    "http://localhost:8001/uploadresponse/"  # Replace with your callback endpoint
)

# Initialize the asynchronous LoRAX client
lorax_client = AsyncClient(LORAX_ENDPOINT)


@app.post("/lorax/upload")
async def upload_batch(request: Request):
    """
    Handles batch upload requests asynchronously.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        JSONResponse: A JSON response indicating success or failure.
    """
    try:
        # Parse the request body
        data = await request.json()
        batch_id = data.get("batchId")
        prompts = data.get("data")

        if not batch_id or not prompts:
            raise HTTPException(status_code=400, detail="Missing batchId or data")

        # Send the batch to LoRAX asynchronously
        async def process_prompt(prompt_data):
            response = await lorax_client.generate(
                prompt_data["prompt"],
                adapter_id=prompt_data.get("adapter_id"),
                max_new_tokens=prompt_data.get("max_new_tokens"),
                # ... other parameters
            )
            return response.dict()

        responses = await asyncio.gather(
            *[process_prompt(prompt_data) for prompt_data in prompts]
        )

        # Trigger the callback asynchronously
        async with aiohttp.ClientSession() as session:
            async with session.post(
                CALLBACK_URL, json={"batchId": batch_id, "response": responses}
            ) as resp:
                if resp.status != 200:
                    raise HTTPException(
                        status_code=resp.status, detail="Callback failed"
                    )

        return JSONResponse(
            content={"message": "Batch processed successfully"}, status_code=200
        )

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error processing batch: {e}")
        return JSONResponse(
            content={"message": "Error processing batch"}, status_code=500
        )


async def callback_handler(batch_id, responses):
    """
    Handles the callback response from LoRAX.

    Args:
        batch_id (str): The batch ID.
        responses (list): The list of responses from LoRAX.
    """
    print(f"Callback received for batch {batch_id}")
    print(f"Responses: {responses}")
    # Here you would typically store the responses or trigger further actions.


# This is a simple callback handler that just prints the responses.
# You can replace this with your own logic.
@app.post("/uploadresponse/")
async def uploadresponse(request: Request):
    data = await request.json()
    batch_id = data.get("batchId")
    responses = data.get("response")
    asyncio.create_task(callback_handler(batch_id, responses))
    return JSONResponse(content={"message": "Callback received"}, status_code=200)


# Run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
