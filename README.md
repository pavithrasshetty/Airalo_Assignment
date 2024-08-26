# Airalo Assignment

## Airalo Website Test Automation

This project automates the Airalo WebApp using PyCharm as the IDE. It includes 4 test cases written using Selenium.

### Prerequisites
- PyCharm IDE
- Python 3.9
- Appium
- Selenium Libraries

### Setup

1. Clone the project from the GitHub repository:
git clone https://github.com/pavithrasshetty/Airalo_Assignment.git

2. Install the required dependencies:
pip install -r requirements.txt

3. Install Appium and start the Appium server:
- Install Appium via npm:

  npm install -g appium

- Start the Appium server:

  appium

4. Run the test cases.

### Test Cases

1. **Open Airalo's Website:**
- Launch a browser and navigate to Airalo's website.

2. **Search for Japan:**
- In the search field on the home page, type "Japan" and select the "Japan" destination from the "Local" section in the autocomplete options.

3. **Select an eSIM Package:**
- On the next page, choose the first eSIM package.
- Click on "Buy Now."

4. **Verify Package Details:**
- In the popup that appears, ensure the following details are accurate:
  - Title: Moshi Moshi
  - Coverage: Japan
  - Data: 1 GB
  - Validity: 7 days
  - Price: $4.50

**Author**
Pavithra Shetty
