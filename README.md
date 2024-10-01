# In Browser Proctoring System

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1.1-green?style=for-the-badge&logo=django&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.1-orange?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10.0-red?style=for-the-badge&logo=opencv&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-19.24.6-brightgreen?style=for-the-badge&logo=linux&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4-blue?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.9.2-yellow?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-cyan?style=for-the-badge&logo=seaborn&logoColor=white)


An advanced web-based proctoring system for secure online examinations, integrating object detection, face recognition, head pose estimation, and background audio monitoring.

<img width="1469" alt="Screenshot 2024-10-02 at 1 14 19 AM" src="https://github.com/user-attachments/assets/0544f4f7-5a1e-49f9-83a4-0f9f5c050b53">
<img width="1471" alt="Screenshot 2024-10-02 at 1 15 24 AM" src="https://github.com/user-attachments/assets/88527c8c-835a-4990-b21d-dbe83166575b">



## 🚀 Features

- 👤 Face recognition login
- 📷 Real-time object detection
- 🧑‍💻 Head pose estimation
- 🎤 Background audio monitoring
- 📊 Comprehensive exam activity logging
- 📈 Detailed cheating detection reports
- 🏫 Institution-specific exam creation

## 🛠️ Technology Stack

- Python 3.12
- Django 5.1.1
- PyTorch 2.4.1
- OpenCV 4.10.0
- dlib 19.24.6
- NumPy 1.26.4
- Matplotlib 3.9.2
- Seaborn 0.13.2


## 📁 Project Structure

```
inbrowserproctoring/
├── .myenv/
├── logs/
├── media/
│   ├── cvs/
│   ├── photos/
│── object_detection_model/
│── proctoring_systems/
├── proctorings/
│   ├── __pycache__/
│   ├── management/
│   ├── migrations/
│   ├── ml_models/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── google_sheets.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── shape_predictor_model/
├── check.py
├── db.sqlite3
├── manage.py
├── report.html
├── requirements.txt
└── yolov8n.pt
```

## 🚀 Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/shishirrijal/in-browser-proctoring-system.git
   ```

2. Set up a virtual environment and activate it:
   ```
   python -m venv .myenv
   source .myenv/bin/activate  # On Windows, use `.myenv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## 📝 Usage

1. Institutions can create exams through the admin interface.
2. Users register and log in using facial recognition.
3. During the exam, the system monitors for:
   - Multiple persons in frame
   - Use of phones or other devices
   - Unusual background sounds
   - Suspicious head movements
4. A detailed log of exam activities is maintained.
5. Organizations can view comprehensive reports on exam integrity.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/in-browser-proctoring-system/issues).
