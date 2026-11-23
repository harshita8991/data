# Practical 5: Anonymization Techniques

## Aim
To learn data anonymization techniques such as k-anonymity, differential privacy and data masking, and apply them to a real-world style dataset.

## Requirements
- Python 3.8 or above
- Libraries: `pip install pandas numpy`

## Dataset
A fictional patient dataset of 12 records (no real people).

| Type | Columns | Meaning |
|---|---|---|
| Direct identifiers | Name, Phone, Email | Identify a person on their own |
| Quasi-identifiers | Age, ZIP, Gender | Can identify a person when combined or linked with other data |
| Sensitive attribute | Disease | The private information to protect |

## Techniques Applied

| Technique | What it does | Applied to |
|---|---|---|
| Data Masking | Hides part of a value | Name, phone number, email |
| K-Anonymity | Makes each record identical to at least k-1 others on quasi-identifiers | Age, ZIP, Gender |
| Generalization | Replaces exact values with ranges or prefixes | Age into 20-year bands, ZIP into first 3 digits |
| Suppression | Removes a column entirely | Gender |
| l-Diversity | Checks each group has varied sensitive values | Disease |
| Differential Privacy | Adds random (Laplace) noise to query answers | Count of diabetes patients |

## Procedure
1. Install libraries: `pip install pandas numpy`
2. Save the program as `anonymization_practical.py`
3. Run it: `python anonymization_practical.py`
4. Observe the output of each technique.

## Output Summary

**1. Data Masking**
```
Name: Aarav Singh   -> A**********
Phone: 9810011223   -> XXXXXX1223
Email: aarav@mail.com -> a***@mail.com
```

**2. K-Anonymity**
```
k BEFORE generalization : 1   (every person is unique, so easy to re-identify)
k AFTER  generalization : 3   (every person looks like at least 2 others)
l-diversity             : 2   (every group has at least 2 different diseases)
```

Anonymized table (after generalization):
```
  Age    ZIP       Disease
20-39 110***           Flu
20-39 110***      Diabetes
20-39 110***           Flu
20-39 201***        Asthma
20-39 201***      Diabetes
20-39 201***           Flu
20-39 201***           Flu
20-39 201***        Asthma
40-59 110*** Heart Disease
40-59 110***        Asthma
40-59 110***      Diabetes
40-59 110*** Heart Disease
```

**3. Differential Privacy** (true count of Diabetes patients = 3)
```
epsilon   Average error (1000 queries)
0.1       10.07
0.5        2.04
1.0        1.02
5.0        0.20
```
(Noisy answers vary on each run unless the random seed is fixed, as in the code.)

## Observations
- Masking alone is not enough. The remaining Age, ZIP and Gender can still identify someone through linking with other datasets.
- Before generalization k = 1, meaning every record was unique and could be re-identified. After generalization k = 3, so an attacker cannot tell which of at least 3 records belongs to a person.
- Generalization and suppression reduce privacy risk but also reduce detail (accuracy of the data).
- k-anonymity can still leak information if everyone in a group has the same disease. That is why l-diversity is checked; here every group has at least 2 different diseases.
- In differential privacy, a smaller epsilon means more noise, stronger privacy and lower accuracy. A larger epsilon means less noise, weaker privacy and higher accuracy.
- With very small epsilon the noisy answer can even be negative or far from the true value, so epsilon must be chosen as a balance between privacy and usefulness.

## Relevance to Data Privacy
- Anonymized data is generally outside the scope of personal data laws such as the DPDP Act 2023 and GDPR, but only if people truly cannot be re-identified. Masked or pseudonymized data is still personal data.
- Organizations like platforms and hospitals can use these techniques to analyze or share data without exposing individuals.

## Result
Data masking, k-anonymity (with generalization, suppression and l-diversity) and differential privacy were successfully applied to a sample dataset.

## Conclusion
No single technique gives complete privacy. Masking protects direct identifiers, k-anonymity protects against linking attacks on quasi-identifiers, l-diversity protects the sensitive attribute, and differential privacy protects individuals in statistical results. Using them together, and balancing privacy against data usefulness, gives the best protection.
