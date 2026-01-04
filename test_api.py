"""
Simple test script to verify API endpoints are working correctly.
Run this after starting the Flask server.

Usage: python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:5555"


def print_response(response, test_name):
    print(f"\n{'='*60}")
    print(f"Test: {test_name}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))
    print(f"{'='*60}")


def test_endpoints():
    print("Starting API tests...")

    # Test 1: GET /heroes
    print("\n1. Testing GET /heroes")
    response = requests.get(f"{BASE_URL}/heroes")
    print_response(response, "GET All Heroes")

    # Test 2: GET /heroes/1
    print("\n2. Testing GET /heroes/1")
    response = requests.get(f"{BASE_URL}/heroes/1")
    print_response(response, "GET Hero by ID")

    # Test 3: GET /heroes/999 (not found)
    print("\n3. Testing GET /heroes/999 (should fail)")
    response = requests.get(f"{BASE_URL}/heroes/999")
    print_response(response, "GET Hero by ID - Not Found")

    # Test 4: GET /powers
    print("\n4. Testing GET /powers")
    response = requests.get(f"{BASE_URL}/powers")
    print_response(response, "GET All Powers")

    # Test 5: GET /powers/1
    print("\n5. Testing GET /powers/1")
    response = requests.get(f"{BASE_URL}/powers/1")
    print_response(response, "GET Power by ID")

    # Test 6: PATCH /powers/1 (valid)
    print("\n6. Testing PATCH /powers/1 (valid)")
    data = {"description": "This is an updated description that is at least 20 characters long"}
    response = requests.patch(f"{BASE_URL}/powers/1", json=data)
    print_response(response, "PATCH Power - Valid")

    # Test 7: PATCH /powers/1 (invalid - too short)
    print("\n7. Testing PATCH /powers/1 (invalid)")
    data = {"description": "Too short"}
    response = requests.patch(f"{BASE_URL}/powers/1", json=data)
    print_response(response, "PATCH Power - Invalid")

    # Test 8: POST /hero_powers (valid)
    print("\n8. Testing POST /hero_powers (valid)")
    data = {
        "strength": "Strong",
        "power_id": 2,
        "hero_id": 2
    }
    response = requests.post(f"{BASE_URL}/hero_powers", json=data)
    print_response(response, "POST HeroPower - Valid")

    # Test 9: POST /hero_powers (invalid strength)
    print("\n9. Testing POST /hero_powers (invalid strength)")
    data = {
        "strength": "Invalid",
        "power_id": 1,
        "hero_id": 1
    }
    response = requests.post(f"{BASE_URL}/hero_powers", json=data)
    print_response(response, "POST HeroPower - Invalid Strength")

    print("\n\nAll tests completed!")


if __name__ == "__main__":
    try:
        test_endpoints()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")
        print("Make sure the Flask server is running on http://localhost:5555")
    except Exception as e:
        print(f"Error: {e}")
