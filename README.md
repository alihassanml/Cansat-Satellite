##CanSat Satellite Monitoring System##

---

Welcome to our CanSat Satellite Monitoring System! This project aims to develop a CanSat satellite equipped with sensors to collect and transmit data such as pressure, temperature, longitude, and more. This README provides an overview of the project and instructions for setting up and running the Django full project with the backend.

### Features:

- **Real-time Monitoring**: Receive live updates of sensor data from the CanSat satellite.
- **Data Visualization**: Visualize collected data through interactive charts and graphs.
- **Backend Integration**: Utilizes Django framework for robust backend management.
- **User Authentication**: Secure access with user authentication and authorization.

### Technologies Used:

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **HTML/CSS/JavaScript**: Frontend technologies for creating an intuitive user interface.
- **SQLite/PostgreSQL**: Database management systems for storing sensor data.
- **Django REST Framework**: Facilitates building Web APIs in Django for seamless data exchange.
- **Chart.js**: JavaScript library for creating responsive and interactive charts.

### Installation:

1. Clone the repository:
   ```
   git clone https://github.com/alihassanml/Cansat-Satellite.git
   ```

2. Navigate to the project directory:
   ```
   cd cansat-monitoring-system
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - **Windows**:
     ```
     venv\Scripts\activate
     ```
   - **Unix/macOS**:
     ```
     source venv/bin/activate
     ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Apply database migrations:
   ```
   python manage.py migrate
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://127.0.0.1:8000/`.

### Usage:

1. Sign up for a new account or log in if you already have one.
2. Connect to the CanSat satellite.
3. View real-time sensor data on the dashboard.
4. Explore historical data through interactive charts and graphs.
5. Manage user accounts and permissions through the admin interface.

### Contribution:

We welcome contributions from the community to enhance this project further. If you have any suggestions, bug fixes, or new features to propose, please open an issue or submit a pull request on GitHub.

### License:

This project is licensed under the [[MIT License](https://github.com/alihassanml/Cansat-Satellite.git)](LICENSE).

---

**Start Monitoring Your CanSat Satellite Today!**

For any questions or support, feel free to reach out to us via GitHub issues or email. Thank you for your interest in our CanSat Satellite Monitoring System!

---
