from flask import Flask, render_template, request

app = Flask(__name__)


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

    # mean
    mean = sum(data) / len(data)

    # median
    med = median(data)

    # variance
    variance = sum((x - mean) ** 2 for x in data) / len(data)

    # std
    std = variance ** 0.5

    # mode
    mode = max(set(data), key=data.count)

    # min max range
    min_v = min(data)
    max_v = max(data)
    range_v = max_v - min_v

    # Q1 Q3
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

    # IQR
    IQR = Q3 - Q1

    # outliers
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


# ========== FLASK ROUTES ==========

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        numbers = request.form["numbers"]

        data = [float(x) for x in numbers.split()]
        result = analyze(data)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)