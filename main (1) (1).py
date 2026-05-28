data = []

while True:
    num = input("ادخل رقم للتحليل أو اكتب exit للخروج: ")

    if num == "exit":
        break

    data.append(float(num))   # تحويل الرقم لـ float

print(data)

# mean
mean = sum(data) / len(data)
print("Mean =", mean)

# median
data = sorted(data)

n = len(data)

if n % 2 == 1:
    median = data[n // 2]
else:
    mid1 = data[n // 2 - 1]
    mid2 = data[n // 2]
    median = (mid1 + mid2) / 2

print("Median =", median)

# variance

mean = sum(data) / len(data)
variance = 0

for x in data:
    n = (x - mean) ** 2
    variance += n

variance = variance / len(data)

print("Variance =",variance)
