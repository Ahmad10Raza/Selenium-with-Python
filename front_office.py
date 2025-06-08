import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pathfinder.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")

# Wait for page to load
time.sleep(3)

driver.implicitly_wait(15)


# Read data from CSV file
with open("customer-onboarding-challenge.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Fill form fields
        driver.find_element(By.ID, "CompanyName").clear()
        driver.find_element(By.ID, "CompanyName").send_keys(row["Company Name"])

        driver.find_element(By.ID, "CustomerID").clear()
        driver.find_element(By.ID, "CustomerID").send_keys(row["Customer ID"])

        driver.find_element(By.ID, "PrimaryContact").clear()
        driver.find_element(By.ID, "PrimaryContact").send_keys(row["Primary Contact"])

        driver.find_element(By.ID, "StreetAddress").clear()
        driver.find_element(By.ID, "StreetAddress").send_keys(row["Street Address"])

        driver.find_element(By.ID, "City").clear()
        driver.find_element(By.ID, "City").send_keys(row["City"])

        # Select State from dropdown
        Select(driver.find_element(By.ID, "State")).select_by_visible_text(row["State"])

        driver.find_element(By.ID, "Zip").clear()
        driver.find_element(By.ID, "Zip").send_keys(row["Zip"])

        driver.find_element(By.ID, "Email").clear()
        driver.find_element(By.ID, "Email").send_keys(row["Email Address"])

        # Select Radio Buttons
        # Offers Discounts: radioDiscountYes or radioDiscountNo
        if row["Offers Discounts"].strip().upper() == "YES":
            driver.find_element(By.ID, "radioDiscountYes").click()
        else:
            driver.find_element(By.ID, "radioDiscountNo").click()

        # Non-Disclosure On File: radioNdaYes or radioNdaNo
        if row["Non-Disclosure On File"].strip().upper() == "YES":
            driver.find_element(By.ID, "radioNdaYes").click()
        else:
            driver.find_element(By.ID, "radioNdaNo").click()

        # Submit the form
        driver.find_element(By.ID, "submitButton").click()
        time.sleep(2)

        # Optionally take a screenshot or log success
        print(f"Submitted: {row['Company Name']}")
        
        # Click "Reset Form" to load next entry
        driver.find_element(By.ID, "resetButton").click()
        time.sleep(1)

# Cleanup
driver.quit()
