import json

import requests
from flask import Flask, jsonify, request
from lorax import Client

app = Flask(__name__)

# Configuration
LORAX_ENDPOINT = "http://127.0.0.1:8080"  # Replace with your LoRAX server endpoint
CALLBACK_URL = (
    "http://localhost:5001/uploadresponse/"  # Replace with your callback endpoint
)

# Initialize the LoRAX client
lorax_client = Client(LORAX_ENDPOINT)


@app.route("/lorax/upload", methods=["POST"])
def upload_batch():
    """
    Handles batch upload requests.

    Args:
        None

    Returns:
        JSONResponse: A JSON response indicating success or failure.
    """
    try:
        # Parse the request body
        data = request.get_json()
        batch_id = data.get("batchId")
        prompts = data.get("data")

        if not batch_id or not prompts:
            return jsonify({"message": "Missing batchId or data"}), 400

        # Send the batch to LoRAX
        responses = []
        for prompt_data in prompts:
            response = lorax_client.generate(
                prompt_data["prompt"],
                adapter_id=prompt_data.get("adapter_id"),
                max_new_tokens=prompt_data.get("max_new_tokens"),
                # ... other parameters
            )
            responses.append(response.model_dump())

        # Trigger the callback
        callback_data = {"batchId": batch_id, "response": responses}
        requests.post(CALLBACK_URL, json=callback_data)

        return jsonify({"message": "Batch processed successfully"}), 200

    except Exception as e:
        print(f"Error processing batch: {e}")
        return jsonify({"message": "Error processing batch"}), 500


@app.route("/uploadresponse/", methods=["POST"])
def uploadresponse():
    """
    Handles the callback response from LoRAX.

    Args:
        None

    Returns:
        JSONResponse: A JSON response indicating success or failure.
    """
    try:
        # Parse the request body
        data = request.get_json()
        batch_id = data.get("batchId")
        responses = data.get("response")

        print(f"Callback received for batch {batch_id}")
        print(f"Responses: {responses}")
        # Here you would typically store the responses or trigger further actions.

        return jsonify({"message": "Callback received"}), 200

    except Exception as e:
        print(f"Error processing callback: {e}")
        return jsonify({"message": "Error processing callback"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
