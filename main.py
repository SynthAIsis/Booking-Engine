import requests
import json

def book_villa_in_crete(api_key, check_in_date, check_out_date, guests, location="Crete, Greece", villa_type="villa"):
    """
    Function to book a villa in Crete Island using a real vacation rental API.
    """
    
    # Example base URL (replace with the actual API URL)
    base_url = "https://admin.booking.com/hotel/hoteladmin/ical.html?t=61a946b5-2762-4b0d-bb29-8ae61b53db1c"  # Replace with the real API base URL
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "location": location,
        "check_in": check_in_date,
        "check_out": check_out_date,
        "guests": guests,
        "property_type": villa_type
    }
    
    try:
        response = requests.post(base_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Villa booked successfully!")
            return response.json()
        else:
            return {"error": f"Booking failed with status code {response.status_code}", "details": response.text}
    
    except Exception as e:
        return {"error": "An unexpected error occurred", "details": str(e)}


# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    CHECK_IN_DATE = "2025-06-15"
    CHECK_OUT_DATE = "2025-06-22"
    GUESTS = 4
    
    booking_result = book_villa_in_crete(API_KEY, CHECK_IN_DATE, CHECK_OUT_DATE, GUESTS)
    print(json.dumps(booking_result, indent=4))
