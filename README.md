# Daraz.pk Functional Automation Framework

A professional, maintainable, and highly reliable web automation framework built for **Daraz.pk** utilizing **Python**, **Selenium WebDriver**, and the **Page Object Model (POM)** design pattern. This architecture decouples test scripts from page layout structures, ensuring robustness and ease of maintenance.

---

## 🚀 Key Framework Architectural Features
* **Page Object Model (POM):** Separates core application UI interaction mechanics (locators, actions) from executable unit validation suites.
* **Weak Connection Optimization:** Built-in dynamic 30-second multi-stage explicitly waiting mechanisms to support seamless execution over lagging networks.
* **Automated Bot-Evasion Stealth Tuning:** Advanced initialization hooks to strip standard Selenium automation markers, allowing automated scripts to safely navigate heavy anti-bot security shields.
* **Query String Injection Routing:** Direct deep-link variable query parameters applied directly via URL string to bypass fragile, dynamic client-side filtering menus over stuttering bandwidth.

---

## 📁 Repository Directory Structure

```text
daraz_automation/
│
├── pages/                    # Encapsulated UI Components & Element Locators
│   ├── __init__.py
│   ├── base_page.py          # Master interaction, synchronization, and wrapper APIs
│   ├── home_page.py          # Navigation hooks and global text search interfaces
│   ├── search_page.py        # Grid extraction matrix and direct parameter filter wrappers
│   └── product_page.py       # Details inspector, document context switches & dynamic asset evaluation
│
├── tests/                    # Executable Verification Environments
│   ├── __init__.py
│   └── test_daraz.py         # Main operational workflow test runner orchestration
│
├── .gitignore                # Rules engine protecting deployment payloads (excludes venv/ directories)
└── README.md                 # Complete framework operations manual
