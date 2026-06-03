import streamlit as st

st.set_page_config(page_title="Data Analyzer", layout="wide")


# ========== FUNCTIONS ==========

def median(arr):
    m = len(arr)
    if m == 0:
        return 0
    arr = sorted(arr)

    if m % 2 == 1:
        return arr[m // 2]
    else:
        return (arr[m // 2 - 1] + arr[m // 2]) / 2


def analyze(data):
    data = sorted(data)

    mean = sum(data) / len(data)
    med = median(data)

    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = variance ** 0.5

    mode = max(set(data), key=data.count)

    min_v = min(data)
    max_v = max(data)
    range_v = max_v - min_v

    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid+1:]

    Q1 = median(lower_half)
    Q3 = median(upper_half)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = []
    for x in data:
        if x < lower_bound or x > upper_bound:
            outliers.append(x)

    return {
        "mean": mean,
        "median": med,
        "variance": variance,
        "std": std,
        "mode": mode,
        "min": min_v,
        "max": max_v,
        "range": range_v,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "outliers": outliers
    }


# ========== UI ==========

st.title("📊 Data Analyzer Dashboard")

numbers = st.text_input("Enter numbers separated by space")

if numbers:

    data = [float(x) for x in numbers.split()]
    result = analyze(data)

    st.write("### Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Mean:", result["mean"])
        st.write("Median:", result["median"])
        st.write("Variance:", result["variance"])

    with col2:
        st.write("Std:", result["std"])
        st.write("Mode:", result["mode"])
        st.write("Min:", result["min"])

    with col3:
        st.write("Max:", result["max"])
        st.write("Range:", result["range"])
        st.write("IQR:", result["IQR"])

    st.write("### Extra")
    st.write("Q1:", result["Q1"], " | Q3:", result["Q3"])
    st.write("Outliers:", result["outliers"])