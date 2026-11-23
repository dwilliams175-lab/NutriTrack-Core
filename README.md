# NutriTrack-Core 🥗📱

**AI-Driven OCR Nutrition Label & Receipt Scanner Extension**

* **Author:** D. Williams
* **Course:** ITCS 2080 – Fundamentals of Software Engineering (Fall 2026, CRN 11132)
* **Institution:** Lakeland Community College
* **Instructor:** Dr. Jo-Michele Rymarczyk

---

## 📋 Project Overview
**NutriTrack-Core** is a software engineering systems architecture and prototype module designed to extend a standard mobile calorie-tracking platform. To address early user drop-off caused by tedious manual food logging, this extension introduces automated Optical Character Recognition (OCR) label scanning, offline request queuing for low-bandwidth environments, and secure cloud synchronization.

---

## ✨ Key Features & Architecture
* **Automated OCR Label Parsing (`ocr_scanner.py`):** Validates image metadata (format and payload limits) and extracts core macronutrients (calories, protein, carbohydrates, and fats) into structured JSON payloads.
* **Offline-First Resilience:** Queues scanned meal entries locally (`QUEUED_FOR_SYNC`) for users in rural or low-connectivity regions, automatically syncing when network access is restored.
* **Serverless Cloud Scalability:** Architected around an event-driven microservice model (AWS Lambda + DynamoDB) to handle peak mealtime traffic without idle server overhead.
* **Security & Privacy by Design:** Enforces strict alphanumeric input validation, parameterized ORM database queries to prevent SQL injection, and Argon2id/JWT authentication safeguards.

---

## 📂 Repository Structure
```text
NutriTrack-Core/
├── README.md                       # Project documentation and setup overview
├── ocr_scanner.py                  # Core Python OCR nutrition label parser module
└── dWilliams_unit09Report.pdf      # Systems engineering & architecture report
```

---

## 🚀 Quick Start (Local Execution)
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd NutriTrack-Core
   ```
2. **Run the OCR Parser Demo (Python 3.10+):**
   ```bash
   python ocr_scanner.py
   ```
3. **Expected Output:**
   The script validates a sample image payload and outputs structured nutritional JSON ready for database ingestion.

---

## 🛠️ Software Engineering Practices Demonstrated
* **Version Control & Branching:** Trunk-based workflow using `main`, `feature/ocr-scanner`, and `docs/project-report`.
* **Code Review & Integration:** Changes integrated via documented Pull Requests (PRs).
* **Issue Tracking:** Feature milestones and security tasks managed via GitHub Issues.
* **Documentation & Governance:** Full SRS, JAD elicitation summaries, architectural trade-off matrix, and ACM/IEEE ethical analysis included in the project report.

---

## ⚠️ Disclaimer
*This software prototype and its accompanying documentation were developed for academic purposes in ITCS 2080. Nutritional parsing outputs are for informational demonstration only and do not constitute medical or dietary advice.*
