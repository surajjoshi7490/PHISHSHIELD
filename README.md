# 🛡️ PHISHSHIELD

Welcome to **PHISHSHIELD**!

PHISHSHIELD is a simple web application that checks a website URL and predicts whether it looks **Safe** or **Not Safe**.

You enter a URL, PHISHSHIELD looks at different parts of the URL and website, and then uses a machine-learning model to make a prediction.

> 🎓 This project was developed as a final-year academic project at MLV Textile & Engineering College.

---

## 🤔 Why PHISHSHIELD?

Phishing websites often look very similar to real websites.

They can be created to trick people into sharing:

- Passwords
- Banking details
- Personal information
- Login credentials

Sometimes, small changes in a URL can be difficult to notice.

The idea behind PHISHSHIELD is simple:

**Give users a quick way to check a URL before interacting with it.**

---

## ✨ What Can PHISHSHIELD Do?

- 🔗 Scan a website URL.
- 🔍 Look at different URL and website characteristics.
- 🤖 Use a trained Gradient Boosting machine-learning model.
- ⚡ Give a quick prediction.
- 🚫 Detect known URL shorteners using an additional rule.
- ✅ Show the final result as **Safe** or **Not Safe**.
- 🌐 Provide an easy-to-use Flask web interface.

---

## 🔄 How It Works

The process is simple:

```text
Enter a URL
     ↓
PHISHSHIELD examines the URL
     ↓
Website features are extracted
     ↓
The machine-learning model checks the features
     ↓
An additional URL-shortener rule is applied
     ↓
Safe / Not Safe
```

PHISHSHIELD uses multiple signals, including:

- URL length
- IP address usage
- URL shortening
- `@` symbol
- Redirects
- Subdomains
- HTTPS usage
- Non-standard ports
- Suspicious forms
- Popups
- Iframes
- Links and scripts
- Other website characteristics

---

## 📁 Project Structure

```text
PHISHSHIELD/
│
├── app.py
├── feature.py
├── convert.py
├── newmodel.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── know_more.html
│
└── screenshots/
    ├── home-page.png
    └── about-page.png
```

### What are the main files?

**`app.py`**  
Handles the Flask website and connects the different parts of the project.

**`feature.py`**  
Looks at the submitted URL and extracts the features needed by the model.

**`convert.py`**  
Handles the final decision logic, including the URL-shortener rule.

**`newmodel.pkl`**  
Contains the pre-trained Gradient Boosting model used for prediction.

---

## 🚀 Installation

Follow these steps.

### ✅ 1. Clone the project

```bash
git clone <your-repository-url>
```

### ✅ 2. Open the project folder

```bash
cd PHISHSHIELD
```

### ✅ 3. Create a virtual environment

```bash
python -m venv venv
```

### ✅ 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### ✅ 5. Install the required packages

```bash
pip install -r requirements.txt
```

That's it! 🎉

---

## ▶️ How to Use

### 1. Start the application

Run:

```bash
python app.py
```

### 2. Open PHISHSHIELD

Open the local address provided by Flask in your browser.

### 3. Enter a URL

For example:

```text
https://example.com
```

### 4. Click **Scan URL**

PHISHSHIELD will process the URL and show the prediction.

---

## 🧠 About the Machine Learning Model

PHISHSHIELD uses a **pre-trained Gradient Boosting classifier**.

The application creates a 30-value feature vector and sends it to the model for prediction.

The project website reports **95% accuracy** for the model.

The current project contains the prediction application and trained model. Detailed training metrics and the complete model-training process are not documented here.

---

## 📸 Project Screenshots

### Home Page
<img width="1104" height="839" alt="image" src="https://github.com/user-attachments/assets/454356b1-93c0-4b07-8e2c-9203ae9fa167" />



### About Page

<img width="1145" height="501" alt="image" src="https://github.com/user-attachments/assets/6d1622bf-43f4-4b61-ac29-e7d8d488fb96" />


---

## ⚠️ A Small Note About Safety

PHISHSHIELD is an academic project.

A **Safe** result does not guarantee that a website is completely trustworthy.

The project should not be used as the only security check for important or sensitive activities.

For a real-world deployment, additional security protections would also be needed.

---

## 🔮 Future Improvements

Some things that could make PHISHSHIELD even better:

- Improve URL validation.
- Add more phishing-related features.
- Improve URL-shortener detection.
- Add clearer explanations for each prediction.
- Add automated tests.
- Add more detailed model evaluation.
- Improve protection against unsafe external requests.
- Prepare the application for secure production deployment.

---

## 🤝 Contributing

Want to help improve PHISHSHIELD? You're welcome!

You can contribute by:

1. Forking the project.
2. Creating a new branch.
3. Making your changes.
4. Testing your changes.
5. Creating a pull request.

Even small improvements are useful.

If you find a bug or have an idea, feel free to open an issue and explain what you found.

---

## 👨‍💻 Project Developers

- **Suraj Joshi**
- **Yash Jain**

---

## 📄 License

No open-source license has been specified for this project yet.

If you plan to publish and allow others to freely use, modify, and share the project, add a license such as the **MIT License** and include the corresponding `LICENSE` file in the repository.
