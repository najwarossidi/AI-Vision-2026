"""
BMI Calculator Program
This program calculates the Body Mass Index (BMI) and classifies it.
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kg and height in meters.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value rounded to 2 decimal places
    """
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    if weight <= 0:
        raise ValueError("Weight must be greater than 0")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    """
    Classify BMI into categories.
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: Classification category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    """Main function to run the BMI calculator."""
    print("=" * 50)
    print("         BMI Calculator Program")
    print("=" * 50)
    print()
    
    try:
        # Get user input
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        classification = classify_bmi(bmi)
        
        # Display results
        print()
        print("=" * 50)
        print("               RESULTS")
        print("=" * 50)
        print(f"Weight:         {weight} kg")
        print(f"Height:         {height} m")
        print(f"BMI:            {bmi}")
        print(f"Classification: {classification}")
        print("=" * 50)
        print()
        
        # Display BMI categories for reference
        print("BMI Categories:")
        print("  Underweight:  BMI < 18.5")
        print("  Normal:       18.5 ≤ BMI < 25")
        print("  Overweight:   25 ≤ BMI < 30")
        print("  Obese:        BMI ≥ 30")
        
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        print("Please enter valid numeric values for weight and height.")
    except ZeroDivisionError:
        print("Error: Height cannot be zero.")


if __name__ == "__main__":
    main()
