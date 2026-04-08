# 🚕 FareCalc: Travel Fare Optimizer

A backend fare calculation script developed for the "CityCab" ride-sharing platform. This tool dynamically calculates travel costs based on distance, vehicle selection, and peak-hour surge pricing logic.

---

## ⚙️ Core Logic
The application uses the following parameters to determine the final estimate:
1.  **Vehicle Rates**:
    - **Economy**: $10/km
    - **Premium**: $18/km
    - **SUV**: $25/km
2.  **Surge Pricing**: Automatically applies a **1.5x Multiplier** if the ride occurs during peak hours (5:00 PM - 8:00 PM).
3.  **Validation**: Includes robust checks to ensure requested services are currently available in the fleet.

---

## 🛠️ Technical Implementation
- **Data Collections**: Uses Python Dictionaries for fast vehicle-rate mapping.
- **Functional Programming**: Centrally managed by the `calculate_fare()` function.
- **Dynamic Logic**: Implements time-based conditional branching.
- **Error Handling**: Gracefully manages invalid vehicle inputs without crashing the session.

---

## 📂 Deliverables
- [fare_calc.py](file:///d:/Virtusa-Training/Virtusa-PreOnboarding-Training/Problem%20Statements%20by%20Virtusa/Python/FareCalc%20Optimizer/fare_calc.py): The main calculation engine and interactive CLI.

---

## 🏃 How to Run
1. Open your terminal in this directory.
2. Run the script:
   ```bash
   python fare_calc.py
   ```
3. Enter the distance, vehicle type, and current hour when prompted.
