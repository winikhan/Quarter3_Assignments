import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Length": {
            "meters": 1,
            "kilometers": 0.001,
            "miles": 0.000621371,
            "feet": 3.28084
        },
        "Weight": {
            "grams": 1,
            "kilograms": 0.001,
            "pounds": 0.00220462,
            "ounces": 0.035274
        },
        "Temperature": {
            "Celsius": lambda c: c,
            "Fahrenheit": lambda c: (c * 9/5) + 32,
            "Kelvin": lambda c: c + 273.15
        }
    }
    
    if from_unit in conversion_factors["Temperature"]:
        return conversion_factors["Temperature"][to_unit](value)
    
    base_value = value / conversion_factors["Length"].get(from_unit, 1)
    return base_value * conversion_factors["Length"].get(to_unit, 1)

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])
    
    units = list(convert_units(1, category, category).keys())
    
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
