# Delhi High Court Case Status Scraper

## 📌 Project Overview
This project is a **web scraper** built with **Python, Flask, and Playwright** to fetch case details from the [Delhi High Court website](https://delhihighcourt.nic.in/).

It allows users to:
- Select **Case Type**
- Enter **Case Number**
- Select **Case Year**
- Solve CAPTCHA manually
- Retrieve and display the case details in a clean, tabular format.

---

## 🚀 Features
- **Flask Web Interface** for easy case search
- Dropdown for **Delhi High Court official case types**
- **Manual CAPTCHA handling** (due to automation restrictions)
- **Playwright automation** for form submission and data extraction
- Results displayed in a **formatted HTML table**

---

## 🛠️ Technologies Used
- **Python 3**
- **Flask** (Backend web server)
- **Playwright** (Browser automation)
- **HTML/CSS** (Frontend form & styling)

---

## 📂 Project Structure


## ❌ Current Limitations
⚠️ **Important Note:**  
The project is **not fully functional** due to issues with:
- **Search button click in Playwright** — On the Delhi High Court official site, the "Search" button is **not clickable via automation** because it’s hidden/disabled until CAPTCHA is verified.
- **CAPTCHA handling** — Currently requires **manual solving**. The scraper waits for the user to solve CAPTCHA in the opened browser before continuing.
- Sometimes, after solving CAPTCHA, the site **redirects to another page** instead of showing results directly, which needs additional handling in the code.

🔹 You can still:
- Open the official site in a Playwright browser
- Fill the case type, number, and year
- Solve CAPTCHA manually
- (Partial) Extract results **if the table appears**


