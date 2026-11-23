# Practical 7: Privacy-Enhancing Technologies (PETs)

## Aim
To study Privacy-Enhancing Technologies (PETs) and understand how they help organizations process and protect data while reducing privacy risks.

## Introduction
Privacy-Enhancing Technologies (PETs) are technologies and techniques designed to protect personal information while still allowing data to be used for legitimate purposes.

PETs aim to reduce unnecessary collection, exposure, and sharing of personal information.

They are especially useful in applications involving sensitive information, analytics, authentication, healthcare, finance, and online services.

## Major Privacy-Enhancing Technologies

### 1. Encryption
Encryption converts readable data into an unreadable form using a cryptographic algorithm and key.

```
Plaintext
    ↓
Encryption + Key
    ↓
Ciphertext
```

Only an authorized party with the appropriate key can recover the protected information.

**Example:** AES and TLS
**Use:** Protecting data during transmission and storage.

### 2. Anonymization
Anonymization removes or transforms identifying information so that individuals cannot be easily identified.

**Examples:**
- Removing names and email addresses
- Generalizing age
- Masking sensitive values

**Use:** Sharing datasets for research and statistical analysis.

### 3. Pseudonymization
Pseudonymization replaces direct identifiers with artificial identifiers.

```
Name: Rahul Sharma
        ↓
User ID: User_1045
```

The original identity may still be recoverable when additional information is available.

**Use:** Data analysis and internal systems where controlled identification may be required.

### 4. Differential Privacy
Differential privacy adds carefully controlled mathematical noise to data or query results so that information about a particular individual is difficult to determine.

```
Private Dataset
      ↓
Privacy Mechanism
      ↓
Statistical Result
```

It allows useful statistical analysis while providing stronger protection for individual records.

**Use:** Large-scale data analysis and statistical reporting.

### 5. Federated Learning
Federated learning allows machine learning models to be trained across multiple devices or organizations without requiring all raw training data to be collected in one central location.

```
Device A ─┐
Device B ─┼→ Model Updates → Central Model
Device C ─┘
```

This can reduce the need to transfer raw personal data.

**Use:** Mobile applications, healthcare, and privacy-sensitive machine learning.

### 6. Homomorphic Encryption
Homomorphic encryption allows certain computations to be performed directly on encrypted data.

```
Plain Data
    ↓
Encryption
    ↓
Encrypted Data
    ↓
Computation
    ↓
Encrypted Result
    ↓
Decryption
    ↓
Result
```

This can allow a service provider to process data without directly seeing the underlying plaintext.

**Use:** Privacy-preserving cloud computing and sensitive data processing.

### 7. Zero-Knowledge Proofs
A Zero-Knowledge Proof (ZKP) allows one party to prove that a statement is true without revealing the underlying secret information. For example, a user could prove that they satisfy a particular condition without revealing unnecessary personal details.

**Use:**
- Privacy-preserving authentication
- Digital identity
- Blockchain systems
- Privacy-preserving transactions

## PETs Comparison

| Technology | Main Privacy Goal | Example Use |
|---|---|---|
| Encryption | Protect data from unauthorized access | HTTPS |
| Anonymization | Reduce identification | Research datasets |
| Pseudonymization | Hide direct identifiers | Data analysis |
| Differential Privacy | Protect individuals in statistical analysis | Data analytics |
| Federated Learning | Avoid centralizing raw training data | Machine learning |
| Homomorphic Encryption | Compute on encrypted data | Cloud computing |
| Zero-Knowledge Proofs | Prove information without revealing it | Privacy-preserving authentication |

## PETs and W3Schools
W3Schools is an online learning platform offering tutorials, exercises, certifications, paid courses, a code editor, website hosting (Spaces) and a mobile app. It collects account, payment, device and usage data and is funded by advertising for free users. PETs could be considered for different privacy-sensitive activities.

### What the Privacy Policy already shows

| PET-related Practice | What the Policy States |
|---|---|
| Encryption (payments) | Payment card data is described as encrypted, and in-app purchases are handled by Apple or Google, so W3Schools states it never sees or stores full card details. |
| Pseudonymization | For signed-in users who consent to personalized ads, the email address is converted into a coded value inside the browser before it is shared. The policy itself notes this value is still personal data because it can recognize the same person across sites. |
| Data minimization | The email address is deleted by the processor (LiveRamp) once the identifier has been created, and the identifier expires after 30 days. Paid plans and classroom accounts are excluded from advertising entirely. |
| Aggregated data | The policy mentions collecting "statistical and aggregated information" about service use, and says data is deleted or anonymized when it is no longer needed. |
| Consent controls | A consent tool allows users to refuse analytics and personalized ads and to control each advertising vendor. |
| Safe transfers | Standard Contractual Clauses and the EU-U.S. Data Privacy Framework are used for international transfers. |

### PETs that could be considered
(The policy does not say whether these are used. They are suggestions.)

| Technology | How It Could Apply to W3Schools |
|---|---|
| Encryption | Protecting user data in transit (HTTPS/TLS) and stored account and profile data at rest. |
| Pseudonymization | Using internal user IDs instead of names or emails when analyzing learning progress, quizzes and exercise results. |
| Anonymization | Removing identifying details from datasets used for statistics, research or improving tutorials. |
| Differential Privacy | Adding noise when publishing aggregate figures, such as browser statistics or tutorial usage trends, so that individual visitors cannot be identified. |
| Federated Learning | Personalizing learning recommendations or progress prediction on the user's device in the mobile app, without sending all learning activity to a central server. |
| Zero-Knowledge Proofs | Letting a user prove they meet an age requirement without revealing their exact date of birth. This could help with the under-16 age rule. |
| Homomorphic Encryption | Potentially useful for processing sensitive data on cloud infrastructure, but it is costly and rarely needed for a tutorial platform. |

The exact implementation of these technologies depends on the platform's architecture and privacy requirements.

## Benefits of PETs
PETs can provide several benefits:
- Reduce exposure of personal information.
- Minimize privacy risks during data processing.
- Support responsible data analysis.
- Reduce unnecessary collection and sharing of raw data.
- Improve user trust.
- Help organizations design privacy into their systems.

## Limitations
PETs are not a complete replacement for general security and privacy controls. Some challenges include:
- Increased system complexity
- Additional computational cost
- Difficulty in implementation
- Possible reduction in data accuracy
- Need for appropriate configuration and key management
- Different PETs provide different levels of privacy protection

A real example is the hashed email identifier used for advertising. It hides the raw email address, but it is still personal data because it can be used to recognize the same person across websites. This shows that pseudonymization is not the same as anonymization.

Therefore, PETs should be selected according to the specific use case and threat model.

## Recommendations
- Select PETs based on the type and sensitivity of the data.
- Use encryption for sensitive data in transit and at rest.
- Apply anonymization or pseudonymization where appropriate.
- Consider differential privacy when publishing statistical information.
- Use privacy-preserving machine learning techniques when raw data should remain decentralized.
- Evaluate the performance and privacy trade-offs before deployment.
- Combine PETs with access control, security monitoring, and data minimization.

## Conclusion
Privacy-Enhancing Technologies provide technical methods for reducing privacy risks while allowing useful data processing. Encryption, anonymization, pseudonymization, differential privacy, federated learning, homomorphic encryption, and zero-knowledge proofs address different privacy challenges.

Using the appropriate PET together with traditional security and privacy controls can help organizations build systems that protect personal information by design.

**Overall Importance:** High

## References
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST Privacy-Enhancing Cryptography: https://csrc.nist.gov/projects/pec
- NIST Cryptography: https://www.nist.gov/cryptography
- W3Schools Privacy Policy: https://www.w3schools.com/about/about_privacy.asp
