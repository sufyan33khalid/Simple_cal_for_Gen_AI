import streamlit as st

# Streamlit Calculator App
def main():
    st.title("Simple Calculator")

    # Select operation
    operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0, format="%f")
    num2 = st.number_input("Enter second number", value=0.0, format="%f")

    result = None

    # Perform calculation based on the selected operation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2

    # Display result
    if result is not None:
        st.success(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()
