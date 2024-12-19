# Payment Failure Analysis Dashboard

This project is a Payment Failure Analysis Dashboard that visualizes payment failures using a Python Django backend, MongoDB database, and a React.js frontend. The application is deployed on Railway.

---

## Features

1. **Interactive Dashboard**:
   - View payment failure statistics by reason, payment method, and time.
   - Filter data by date range.
   - Visualize data with bar charts and other graphs.

2. **REST API Backend**:
   - APIs built with Django to fetch analytics data from MongoDB.

3. **Database**:
   - MongoDB stores payment transaction data.

4. **Deployment**:
   - Hosted on Railway.

---

## Technologies Used

### Backend
- Python (Django)
- MongoDB

### Frontend
- React.js
- Chart.js

### Deployment
- Railway

---

## Setup Instructions

### Prerequisites
1. Python 3.10 or later
2. Node.js and npm
3. MongoDB instance (local or hosted, e.g., MongoDB Atlas)
4. Railway account

---

### Backend Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abharaut/payment_failure.git
   cd payment-failure-dashboard/backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB**:
   - Update `settings.py` in the Django project:
```python

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Dashboard',
        'CLIENT': {
           'host': 'mongodb+srv://abhaintern:BzlCMiNOsJ536N6G@cluster0.wyqg4.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority',
        }
    }
}
```
5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

---

### Frontend Setup

1. **Navigate to Frontend Directory**:
   ```bash
   cd ../frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Start the Development Server**:
   ```bash
   npm start
   ```
   - The React application will run at `http://localhost:3000`.

---


4. **Access the Application**:
   - Use the URLs provided by Cloud Run to access the backend and frontend.

---

## Usage

1. Open the frontend in your browser.
2. Use the filters to select a date range and view payment failure statistics.
3. Analyze the data using the provided graphs and export options.

---

## Future Enhancements

1. Add real-time updates with WebSockets.
2. Implement user authentication for secure access.
3. Add more detailed filters and data visualizations.
4. Integrate with external payment gateways for real-time monitoring.

---


