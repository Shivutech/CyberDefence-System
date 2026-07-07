# 🛡️ AI Cyber Defence System

An AI-powered Cyber Defence System that captures live network traffic, extracts packet information, analyzes network behavior using Machine Learning, detects suspicious activities, and provides real-time monitoring through an interactive dashboard.

---

# 📖 Project Overview

Cyber attacks such as DDoS, Port Scanning, and network intrusions are increasing every day. Traditional monitoring tools require manual analysis, which is time-consuming.

This project provides an automated solution that continuously monitors network traffic, captures packets in real time, extracts important network features, and uses a Machine Learning model to identify suspicious traffic. All captured data is visualized on a dashboard, making it easier to monitor network activity.

---

# 🎯 Objectives

- Monitor live network traffic.
- Capture and analyze packets.
- Detect suspicious activities using AI/ML.
- Visualize network traffic.
- Store packet information for future analysis.
- Generate alerts for suspicious packets.

---

# 🚀 Features

- Live Packet Capture
- Network Traffic Monitoring
- Machine Learning Based Attack Detection
- Real-time Dashboard
- Packet Logging
- CSV Data Storage
- Protocol Analysis
- Source & Destination IP Tracking
- Packet Size Monitoring
- Easy-to-use Interface

---

# ⚙️ How It Works

1. The system captures live network packets using Scapy.
2. Important packet features such as Source IP, Destination IP, Protocol, and Packet Size are extracted.
3. The extracted data is stored in a CSV file.
4. A trained Machine Learning model analyzes the packet features.
5. If suspicious traffic is detected, the system generates an alert.
6. The dashboard displays real-time packet information and network statistics.

---

# 🛠️ Technologies Used

- Python
- Scapy
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib
- CSV

---

# 📂 Project Structure

```
CyberDefence-System
│
├── analysis
├── capture
├── data
├── models
├── images
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 📷 Dashboard Screenshots

## Dashboard Home

![Dashboard Home](images/screenshot(32).png)

## Live Packet Monitoring

![Live Packet Monitoring](images/screenshot(33).png)

## Traffic Analysis

![Traffic Analysis](images/dashboard3.png)

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/CyberDefence-System.git
```

Go to project folder

```bash
cd CyberDefence-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Train the Machine Learning model

```bash
python analysis/train_model.py
```

Start Packet Capture

```bash
python main.py
```

Run Dashboard

```bash
streamlit run dashboard.py
```

---

# 📊 Output

- Live Network Monitoring
- Packet Capture
- Attack Detection
- Protocol Statistics
- Network Visualization
- Packet History

---

# 🔮 Future Improvements

- Deep Learning Based Detection
- Real-time Email Alerts
- Telegram Notifications
- IP Reputation Checking
- Threat Intelligence Integration
- Firewall Automation
- Database Support
- Cloud Deployment

---

# 👨‍💻 Author

**Shivakant Prajapati**

B.Tech (Computer Science & Engineering - AI & ML)

Cyber Security Enthusiast | Machine Learning | Python Developer

---

# ⭐ Support

If you found this project useful, don't forget to **Star ⭐ this repository**.