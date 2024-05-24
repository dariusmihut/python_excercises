import requests
import warnings
warnings.filterwarnings("ignore", module="urllib3")

url = 'https://dummy.restapiexample.com/api/v1/employees'

employees_response = requests.get(url, headers={"User-Agent": "my python"})

print(employees_response)
employees_response_data = employees_response.json()

print(employees_response_data.get('status'))

employees = employees_response_data.get('data')

for employee in employees:
    print(employee)
