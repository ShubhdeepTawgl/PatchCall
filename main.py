import requests
import json

# Constants
INTERVIEW_SERVICE_URL = "https://interview-api.interviewintelligence.in"
END_POINT = "/api/v1/interviews/{}/recordingDetails"
INTERVIEW_ID = "5145"  # Replace with the actual interview ID
TOKEN = "V4KtNQPCoQpJZrUlJLQ5QuJv8AiV34X2b4cLUe5SNrESrJp5qFlp"  # Replace with your actual token
TENANT_ID = "9I7PFYlRu15XIhInDRpg9NBbI"  # Replace with your actual tenant ID

# Load JSON data from a file
def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        return None

# Make the PATCH request
def update_database(json_data, token, tenant_id, interview_id):
    url = f"{INTERVIEW_SERVICE_URL}{END_POINT.format(interview_id)}"
    
    headers = {
        "Content-Type": "application/json",
        "X-TAWGL-USER": token,
        "X-TAWGL-CLIENT": tenant_id
    }
    
    try:
        response = requests.patch(url, json=json_data, headers=headers)
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
    except requests.RequestException as e:
        print("Error occurred during the request:", e)

# Main execution
if __name__ == "__main__":
    # Path to your JSON file
    json_file_path = "MP4_dev_6d017d8a-537a-4663-b6aa-2a982b70c832.json"  # Replace with the path to your JSON file
    json_data = load_json(json_file_path)
    
    if json_data:
        update_database(json_data, TOKEN, TENANT_ID, INTERVIEW_ID)
