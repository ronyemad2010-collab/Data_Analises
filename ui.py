import streamlit as st
import numpy as np
from collections import Counter
import math

st.set_page_config(page_title="Data Analyzer", layout="wide")

# ====== CSS لتقريب الشكل ======
st.markdown("""
<style>

body {
    background-color: #0a0f2c;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.title {
    text-align: center;
    color: #4da3ff;
    font-size: 40px;
    font-weight: bold;
}

.card {
    background-color: #111a33;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 0 10px rgba(0,140,255,0.2);
    text-align: center;
    color: white;
    margin: 5px;
}

</style>
""", unsafe_allow_html=True)

# ====== TITLE ======
st.markdown('<div class="title">📊 Data Analyzer Dashboard</div>', unsafe_allow_html=True)

# ====== INPUT ======
numbers_input = st.text_input("Enter numbers separated by space")

def median(arr):
    arr = sorted(arr)
    n = len(arr)
    if n == 0:
        return 0
    if n % 2 == 1:
        return arr[n // 2]
    return (arr[n//2 - 1] + arr[n//2]) / 2

if numbers_input:

    try:
        numbers = list(map(float, numbers_input.split()))
        n = len(numbers)

        mean = sum(numbers) / n
        med = median(numbers)

        variance = sum((x - mean) ** 2 for x in numbers) / n
        std = math.sqrt(variance)

        freq = Counter(numbers)
        mode = [k for k, v in freq.items() if v == max(freq.values())]

        mn = min(numbers)
        mx = max(numbers)
        data_range = mx - mn

        sorted_nums = sorted(numbers)
        mid = n // 2

        if n % 2 == 0:
            lower = sorted_nums[:mid]
            upper = sorted_nums[mid:]
        else:
            lower = sorted_nums[:mid]
            upper = sorted_nums[mid+1:]

        q1 = median(lower)
        q3 = median(upper)
        iqr = q3 - q1

        outliers = [x for x in numbers if x < q1 - 1.5*iqr or x > q3 + 1.5*iqr]

        # ====== CARDS LAYOUT ======
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f'<div class="card">Mean: {mean:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">Median: {med:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">Variance: {variance:.2f}</div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<div class="card">Std: {std:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">Mode: {mode}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">Min: {mn}</div>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<div class="card">Max: {mx}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">Range: {data_range:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">IQR: {iqr:.2f}</div>', unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(f"""
        <div class="card">
            Q1: {q1:.2f} | Q3: {q3:.2f}<br><br>
            Outliers: {outliers}
        </div>
        """, unsafe_allow_html=True)

    except:
        st.error("Invalid input! Please enter numbers separated by spaces.")