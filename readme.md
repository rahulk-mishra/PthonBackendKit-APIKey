# 💳 Juspay Flask Integration Kit

This project is a Python-based backend using **Flask** that demonstrates how to integrate **Juspay's Payment Gateway** using **API Key-based authentication**. It allows merchants to initiate a payment session, handle payment responses, check order status, and process refunds.

---

## 📦 Features

- Initiate Juspay session and redirect users to hosted payment page
- Handle return URL and show order status
- Fetch order status using order ID
- Process refund requests
- Logs for debugging and tracking


---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Others**: Ngrok (for public tunneling), Logging

---

## 📁 Project Structure
project-root/
├── index.py # Main Flask application
├── payment_handler.py # Juspay API integration logic
├── config.json # Merchant configuration
├── templates/
│ └── initatePaymentDataForm.html # to create order and initiate payment display page.
| └── initateRefundDataForm.html  # to initate refund for given order.
| └── client.py # contains all the basic auth and checks.
| └── exception.py # contains exception class for API exception.
| └── request.py # contains Request class contains all important parameter.
| └── simpleLogger.py # contains logger class to create .log files and all
├── requirements.txt # Python dependencies
└── README.md # Project documentation
