'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys

driver = webdriver.Chorme()
driver.get("https://example.com/login")

driver.find_element(By.ID, "username").send_keys("Test_user")
driver.find_element(By.ID, "password").send_keys("user")
driver.find_element(By.ID, "loginBtn").click()

assert "Dashboard" in driver.title
driver.quit()


#Dynamic Element
element= webdriver(driver, 10).unitl(
    lambda d: d.find_element(By.XPATH, "//button[contain(text(), 'Submit')]")

)

#Handle dropdown in seleniums
from selenium.webdriver.support.ui import Select
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown = select_by_visible_text("India")

#write sql query to fetch. customers with transaction above 10000Rs
SELECT customer_id, SUM(amount) AS total_amount
FROM transactions
GROUP BY customer_id
HAVING sum(amount) > 10000;


#SQL query to find duplicates records in a table.
SELECT account_number, COUNT(*)
FROM customers
GROUP BY account_number
HAVING COUNT(*) > 1;


#POM Ex
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "username"
        self.password = "password"
        self.loginBtn = "loginBtn"

    def login(self, user, pwd):
        self.driver.find_element(By.ID, self.username).send_keys(user)
        self.driver.find_element(By.ID, self.password).send_keys(pwd)
        self.driver.find_element(By.ID, self.loginBtn).click()

#how do you perform API testing in Python?
import requests
response = requests.post(
    "https://api.bank.com/login"
    json={"username": "user1", "password": pass123"}
)
assert response.status_code == 200
assert "token" in response.json()

#How do you parameterize test case in Pytest:
import pytest
@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ])

def test_login(username, password):
    assert username != " " and password != " "
'''
def print_pattern(n: int):
    if n < 2:
        print("n must be >= 2")
        return
    
    # Top part: n rows of "@"
    for _ in range(n):
        print("@")
    
    # Middle: diagonal with stars
    print("@" + "*" * n)             # first star line with @ at start
    print(" " * (n) + "*" * n + "@") # shifted line with @ at end
    
    # Bottom part: n rows of "@" (shifted to the right)
    for _ in range(n):
        print(" " * (n*2) + "@")

# Example run
print_pattern(4)
