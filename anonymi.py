"""
Practical 5: Anonymization Techniques
Applies data masking, generalization (k-anonymity) and differential privacy
to a sample (fictional) patient dataset.
Requires: pip install pandas numpy
"""
import numpy as np
import pandas as pd

np.random.seed(42)  # fixed seed so output is repeatable

# ---------------------------------------------------------------
# SAMPLE DATASET (fictional data)
# Direct identifiers : Name, Phone, Email
# Quasi-identifiers  : Age, ZIP, Gender
# Sensitive attribute: Disease
# ---------------------------------------------------------------
data = {
    "Name":    ["Aarav Singh", "Priya Sharma", "Rohan Verma", "Sneha Gupta", "Karan Mehta",
                "Anjali Rao", "Vikram Joshi", "Neha Kapoor", "Rahul Nair", "Pooja Iyer",
                "Amit Yadav", "Simran Kaur"],
    "Phone":   ["9810011223", "9899123456", "9711234567", "9958765432", "9876501234",
                "9810098765", "9911223344", "9650123456", "9999887766", "9818123456",
                "9873456789", "9717654321"],
    "Email":   ["aarav@mail.com", "priya@mail.com", "rohan@mail.com", "sneha@mail.com",
                "karan@mail.com", "anjali@mail.com", "vikram@mail.com", "neha@mail.com",
                "rahul@mail.com", "pooja@mail.com", "amit@mail.com", "simran@mail.com"],
    "Age":     [23, 27, 24, 34, 38, 36, 52, 55, 58, 25, 37, 54],
    "ZIP":     ["110091", "110092", "110091", "201001", "201002", "201001",
                "110092", "110091", "110092", "201002", "201001", "110091"],
    "Gender":  ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Disease": ["Flu", "Diabetes", "Flu", "Asthma", "Diabetes", "Flu",
                "Heart Disease", "Asthma", "Diabetes", "Flu", "Asthma", "Heart Disease"],
}
df = pd.DataFrame(data)

print("=" * 70)
print("ORIGINAL DATASET")
print("=" * 70)
print(df.to_string(index=False))

# ---------------------------------------------------------------
# 1. DATA MASKING - hide direct identifiers
# ---------------------------------------------------------------
def mask_name(name):
    return name[0] + "*" * (len(name) - 1)

def mask_phone(phone):
    return "XXXXXX" + phone[-4:]

def mask_email(email):
    user, domain = email.split("@")
    return user[0] + "***@" + domain

masked = df.copy()
masked["Name"] = masked["Name"].apply(mask_name)
masked["Phone"] = masked["Phone"].apply(mask_phone)
masked["Email"] = masked["Email"].apply(mask_email)

print("\n" + "=" * 70)
print("1. DATA MASKING (direct identifiers hidden)")
print("=" * 70)
print(masked.to_string(index=False))

# ---------------------------------------------------------------
# 2. K-ANONYMITY - check, then fix by generalization
# ---------------------------------------------------------------
quasi_ids = ["Age", "ZIP", "Gender"]

def k_anonymity(frame, qi):
    """k = size of the smallest group sharing the same quasi-identifier values."""
    return frame.groupby(qi).size().min()

print("\n" + "=" * 70)
print("2. K-ANONYMITY")
print("=" * 70)
print("k BEFORE generalization (original quasi-identifiers):",
      k_anonymity(df, quasi_ids))

anon = df.drop(columns=["Name", "Phone", "Email"]).copy()   # remove direct identifiers

def age_band(age):
    low = (age // 20) * 20
    return f"{low}-{low + 19}"

anon["Age"] = anon["Age"].apply(age_band)          # generalize Age to 20-year bands
anon["ZIP"] = anon["ZIP"].str[:3] + "***"          # generalize ZIP to first 3 digits
anon = anon.drop(columns=["Gender"])               # suppress Gender

anon_qi = ["Age", "ZIP"]
print("k AFTER  generalization (20-year Age bands, ZIP prefix, Gender suppressed):",
      k_anonymity(anon, anon_qi))
print()
print(anon.sort_values(anon_qi).to_string(index=False))

# l-diversity check: does each group contain varied sensitive values?
l_div = anon.groupby(anon_qi)["Disease"].nunique().min()
print("\nl-diversity (min distinct diseases in any group):", l_div)

# ---------------------------------------------------------------
# 3. DIFFERENTIAL PRIVACY - Laplace mechanism on a count query
# ---------------------------------------------------------------
print("\n" + "=" * 70)
print("3. DIFFERENTIAL PRIVACY (Laplace mechanism)")
print("=" * 70)

true_count = int((df["Disease"] == "Diabetes").sum())
sensitivity = 1  # adding/removing one person changes a count by at most 1

def dp_count(true_value, epsilon):
    noise = np.random.laplace(loc=0, scale=sensitivity / epsilon)
    return true_value + noise

print("Query: How many patients have Diabetes?")
print("True count:", true_count)
for eps in [0.1, 0.5, 1.0, 5.0]:
    noisy = [dp_count(true_count, eps) for _ in range(5)]
    print(f"epsilon = {eps:<4} -> 5 noisy answers:",
          [round(x, 2) for x in noisy])

print("\nSmaller epsilon = more noise = stronger privacy, lower accuracy.")
print("Larger  epsilon = less noise = weaker privacy, higher accuracy.")

# Accuracy vs. privacy over many runs
print("\nAverage absolute error over 1000 queries:")
for eps in [0.1, 0.5, 1.0, 5.0]:
    err = np.mean([abs(dp_count(true_count, eps) - true_count) for _ in range(1000)])
    print(f"epsilon = {eps:<4} -> average error = {err:.2f}")

print("\nPractical completed.")
