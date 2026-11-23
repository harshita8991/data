# Practical 2: Privacy Impact Assessment (PIA) of the W3Schools Adventure App

## Aim
To conduct a Privacy Impact Assessment of the W3Schools Adventure mobile app (iOS and Android) to identify potential privacy risks and suggest strategies to reduce them.

## System Selected
- **Organization:** W3Schools
- **System:** W3Schools Adventure app (bite-sized coding lessons and challenges), used with a W3Schools account
- **Privacy Policy:** [W3Schools Privacy Policy](https://www.w3schools.com/about/about_privacy.asp)
- **Basis of assessment:** Published Privacy Policy (last updated 16 September 2026)

## Requirements
- Internet connection
- Web browser
- W3Schools Privacy Policy and Cookie Policy

## Procedure
1. Describe the system and its purpose.
2. Identify the personal data collected by the app.
3. Map how the data flows between the user, W3Schools and third parties.
4. Identify privacy risks.
5. Rate each risk by likelihood and impact.
6. Identify existing safeguards and suggest additional measures.
7. Record the residual risk.

## Step 1: System Description
The W3Schools Adventure app lets users learn coding through short lessons and challenges on their phones. The Privacy Policy states that it also applies to the mobile apps. Users can create a W3Schools account, track progress and buy subscriptions inside the app.

## Step 2: Personal Data Inventory

| Data Category | Examples | Purpose |
|---|---|---|
| Account Information | Email address, full name, phone number | Create and manage the account |
| Usage Information | Pages or screens viewed, clicks, searches, errors, time spent | Operate and improve the service |
| Device Information | Device type, operating system, language, unique device identifiers, push notification tokens | Delivery, performance and notifications |
| Subscription Data | User ID, transaction ID, subscription status | Manage in-app subscriptions |
| Payment Data | Card details (handled by Apple App Store or Google Play) | Process purchases |
| Support Data | Messages, attachments | Provide customer support |

## Step 3: Data Flow

| Stage | Description |
|---|---|
| Collection | Data is provided by the user or collected automatically from the app and device |
| Processing | W3Schools uses the data to run and improve the service, provide support and security, and for marketing |
| Storage | Cloud infrastructure (Amazon), in the USA or Europe |
| Sharing | Sub-processors such as RevenueCat (subscriptions), Google (analytics), Zendesk (support) and Brevo (marketing emails) |
| Payments | Apple App Store or Google Play handle in-app payments, and W3Schools states it never sees full card details |
| Deletion | Account and related data are stated to be deleted within 30 days of account deletion, subject to exceptions |

## Step 4: Privacy Risk Assessment

| ID | Privacy Risk | Likelihood | Impact | Risk Level |
|---|---|---|---|---|
| R1 | Device identifiers and push tokens could be used to track a user across sessions | Medium | Medium | Medium |
| R2 | Usage data may be combined with data from other sources to build a detailed profile | Medium | Medium | Medium |
| R3 | Subscription data is shared with a US-based sub-processor (RevenueCat) | Low | Medium | Low |
| R4 | Data may be processed outside the user's country where protection may differ | Medium | Medium | Medium |
| R5 | Children may use the app, although the service is generally not intended for users under 16 | Medium | High | High |
| R6 | Retention periods are not clearly defined ("minimum period necessary") | Medium | Medium | Medium |
| R7 | Data may be used for marketing emails and promotions | Low | Low | Low |
| R8 | Unauthorized access to an account or a data breach could expose personal data | Low | High | Medium |
| R9 | W3Schools is not responsible for sub-processors' handling of data beyond what it shares with them | Medium | Medium | Medium |

## Step 5: Existing Safeguards
- Separate consent through a consent tool for analytics and personalized advertising, which can be withdrawn at any time.
- Payments are handled by Apple or Google, so full card details are not seen by W3Schools.
- Administrative, technical and physical security safeguards, and contractual obligations on sub-processors.
- A clear account deletion process with a 30-day deletion timeline.
- Standard Contractual Clauses and EU-U.S. Data Privacy Framework compliance for international transfers.
- User rights such as access, correction, deletion and objection.

## Step 6: Recommended Mitigation Measures

| Risk | Recommended Measure |
|---|---|
| R1, R2 | Limit collection to what the app needs and keep device identifiers separate from account data where possible |
| R3, R9 | Review sub-processor agreements regularly and publish clear information about the data each one receives |
| R4 | Keep using legal transfer safeguards and publish where each category of data is stored |
| R5 | Add stronger age verification and parental consent steps |
| R6 | Publish specific retention periods for each data category |
| R7 | Keep marketing opt-in clear and unsubscribe options easy to use |
| R8 | Offer two-factor authentication, use encryption, and run regular security reviews |

## Step 7: Residual Risk

| Risk | Before Mitigation | After Mitigation |
|---|---|---|
| R1 | Medium | Low |
| R2 | Medium | Low |
| R3 | Low | Low |
| R4 | Medium | Low |
| R5 | High | Medium |
| R6 | Medium | Low |
| R7 | Low | Low |
| R8 | Medium | Low |
| R9 | Medium | Medium |

## Result
The Privacy Impact Assessment of the W3Schools Adventure app was successfully performed. The assessment identified the personal data collected, mapped its flow, rated nine privacy risks and suggested mitigation measures.

## Conclusion
The W3Schools Adventure app has a reasonable set of existing safeguards, including consent controls, third-party payment handling and a clear deletion process. The highest risk is children's use of the app, and the main remaining concerns are unclear retention periods, cross-border transfers and reliance on third-party sub-processors. Adding stronger age checks, defined retention periods and clearer sub-processor information would reduce these risks further.
