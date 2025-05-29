# aquariux-khoa-tran
Technical test for Senior Automation QA Engineer

## Installation

1. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

### Page Object Model (POM)
- `pages/`: Contains page object classes
  - `base/`: Base classes for elements and pages
  - `login_page.py`: Login page interactions
  - `home_page.py`: Home page interactions

### Utils
- `utils/`: Utility modules
  - `logger.py`: Logging setup and configuration
  - `driver/`: WebDriver initialization and management, including WebDriverWait control for centralize purpose
  - `common_imports.py`: Shared imports across the project

### Tests
- `tests/`: Test cases and suites
  - `conftest.py`: PyTest configuration and fixtures
  - `test_login.py`: Login functionality tests

### Reports
- `reports/`: Test execution reports
  - Allure reports generation
  - HTML test results

### Logging
- `logs/`: Application logs
  - Rotating log files
  - Separate test run sections
  - Debug and error information

### Configuration
- `config/`: Environment configurations
  - `config.py`: Environment-specific settings
  - Test data and parameters
  - Browser configurations

