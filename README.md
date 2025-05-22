# 🧪 Hybrid Python Automation Framework for nopCommerce

This is a robust, scalable, and maintainable **Hybrid Test Automation Framework** built using **Python** for automating the web application **nopCommerce**. It combines the best features of **Keyword-driven**, **Data-driven**, and **Page Object Model (POM)** approaches.

---

## 🚀 Tech Stack

- **Language**: Python
- **Test Runner**: Pytest
- **Web Automation**: Selenium WebDriver
- **Reporting**: HTML Reports (pytest-html)
- **Data Handling**: Excel (openpyxl)
- **Logging**: Python Logging Module
- **Design Pattern**: Page Object Model (POM)
- **Framework Type**: Hybrid (Data-Driven + POM + Modular)

---

## 📁 Project Structure

nopcommerceApp/
│
├── Configurations/ # Configuration files
│ └── config.ini
│
├── Logs/ # Log files directory
│
├── pageObjects/ # Page Object classes
│ ├── init.py
│ └── Loginpage.py
│
├── Reports/ # HTML reports generated after test execution
│
├── Screenshots/ # Screenshots of failed test cases
│
├── testCases/ # Test scripts
│ ├── init.py
│ ├── conftest.py # Pytest fixtures and setup
│ ├── test_login.py
│ └── test_login_ddt.py # Data-driven login test
│
├── TestData/ # External test data (Excel)
│ └── LoginTest.xlsx
│
├── utilities/ # Utility modules
│ ├── init.py
│ ├── customLogger.py # For logging
│ ├── readProperties.py # Read config.ini
│ └── XLUtils.py # Excel utilities
│
├── .gitignore
└── README.md




---

## 🚀 Features

- ✅ **Hybrid framework**: POM + Data-driven + Modular
- ✅ **Selenium WebDriver** with **Pytest** for automation
- ✅ **Excel-based test data** using `openpyxl`
- ✅ **Custom logging** via Python's `logging` module
- ✅ **Automatic screenshot capture** on test failure
- ✅ **HTML test reports** generation
- ✅ **INI-based config management** (URL, browser, credentials, etc.)
- ✅ Organized structure for **reusability** and **scalability**

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nopcommerceApp.git
   cd nopcommerceApp

