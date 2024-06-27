import random
import string

# Estimate pi by computing the ratio of the volume of a sphere to the volume of
# a cube

x = 50

p1 = 0
p2 = 0

for i in range(x):
    for j in range(x):
        for k in range(x):
            x1 = float(
                random.choices(["+", "-"])[0]
                + "0."
                + "".join(random.choices(string.digits, k=7 + i))
            )
            x2 = float(
                random.choices(["+", "-"])[0]
                + "0."
                + "".join(random.choices(string.digits, k=7 + j))
            )
            x3 = float(
                random.choices(["+", "-"])[0]
                + "0."
                + "".join(random.choices(string.digits, k=7 + k))
            )

            d = x1**2 + x2**2 + x3**2

            if d <= 1:
                p1 += 1

            p2 += 1

r = 6 * p1 / p2

print(f"Final Estimation of Pi = {r}")
