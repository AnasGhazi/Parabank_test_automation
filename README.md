# Parabank Test Automation

This project contains automated test scripts for [Parabank](https://parabank.parasoft.com/parabank/index.htm), a demo banking application, using **Python**, **Pytest**, and **Playwright**.

## 🚀 Features

- Automated end-to-end tests for login and account actions
- Headless browser support via Playwright
- Modular test structure with clear test case organization
- Easy setup with Python virtual environment

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AnasGhazi/Parabank_test_automation.git
cd Parabank_test_automation

**2. Create a Virtual Environment (Recommended)**
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# .\venv\Scripts\activate   # Windows

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you're missing Playwright's dependencies, run:

bash
Copy
Edit
playwright install
✅ Running Tests
To execute all tests:

bash
Copy
Edit
pytest

⚠️ GitHub Push Error & Solution
Problem:
Pushing failed due to venv/ folder being over 100MB, even after adding .gitignore.

Solution That Worked:
We used git-filter-repo to remove the previously committed venv folder from the entire Git history.

Steps:
bash
Copy
Edit
brew install git-filter-repo
git clone https://github.com/AnasGhazi/Parabank_test_automation.git
cd Parabank_test_automation

git filter-repo --path venv --invert-paths
git remote add origin https://github.com/AnasGhazi/Parabank_test_automation.git
git push --set-upstream origin main --force
⚡ Important: Always commit your code in a fresh clone to avoid including unnecessary or large folders in your Git history.

📂 Folder Structure
bash
Copy
Edit
Parabank_test_automation/
├── tests/                   # Test files
├── venv/                   # (excluded from repo)
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
├── .gitignore
└── README.md

