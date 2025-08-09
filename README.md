# FastAPI ML Prediction Demo

A demonstration project showcasing how to deploy a trained Machine Learning model using FastAPI. This project serves a pre-trained scikit-learn model through a REST API, enabling real-time predictions via HTTP requests.

## 🚀 Features

- **FastAPI Web Framework**: High-performance, modern web framework for building APIs
- **Pre-trained ML Model**: Uses a pickled scikit-learn model for predictions
- **Pydantic Data Validation**: Automatic request/response validation
- **RESTful API**: Clean, intuitive API endpoints
- **Lightweight**: Minimal dependencies and simple setup

## 📋 Requirements

- Python 3.12.6+
- Dependencies listed in `requirements.txt`

## 🛠️ Project Structure

```
FastAPI-MLprediction-Demo/
├── app.py              # Main FastAPI application
├── model.pkl           # Pre-trained ML model (768 bytes)
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 📦 Dependencies

- **FastAPI (0.115.6)**: Modern web framework for APIs
- **scikit-learn (1.5.2)**: Machine learning library
- **uvicorn**: ASGI server for FastAPI
- **pydantic**: Data validation using Python type annotations

## 🔧 Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/mehul16/FastAPI-MLprediction-Demo.git
   cd FastAPI-MLprediction-Demo
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

The application will be available at **http://localhost:8000**

## 🌐 API Endpoints

### GET `/`
Returns a welcome message confirming the service is running.

**Response:**
```json
{
  "message": "FastAPI ML prediction service is running!"
}
```

### POST `/predict/`
Makes predictions using the trained ML model.

**Request Body:**
```json
{
  "col1": 0.0,
  "col2": 0.0,
  "col3": 0.0,
  "col4": 0.0,
  "col5": 0.0,
  "col6": 0.0,
  "col7": 0.0,
  "col8": 0.0,
  "col9": 0.0
}
```

**Response:**
```json
{
  "PredictedValue": 123.45
}
```

**Example cURL request:**
```bash
curl -X POST "http://localhost:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{
       "col1": 1.5,
       "col2": 2.0,
       "col3": 0.5,
       "col4": 3.2,
       "col5": 1.8,
       "col6": 0.9,
       "col7": 2.7,
       "col8": 1.1,
       "col9": 4.0
     }'
```

## 🏗️ Architecture

The application follows a simple yet effective architecture:

1. **FastAPI Application** (`app.py`): Handles HTTP requests and responses
2. **ML Model** (`model.pkl`): Pre-trained scikit-learn model loaded at runtime
3. **Data Validation**: Pydantic models ensure input data integrity

## 🔍 Model Information

- **Model Type**: Scikit-learn model (pre-trained)
- **Input Features**: 9 numerical features (col1 through col9)
- **Output**: Single numerical prediction value
- **Model Size**: 768 bytes (lightweight model)

## � Deployment Options

### Local Development
- Run with `uvicorn` for development and testing
- Use virtual environments for isolation

### Production Deployment
- Deploy to cloud platforms (AWS, GCP, Azure, Heroku, etc.)
- Use process managers like `gunicorn` for production
- Set up reverse proxy with `nginx` if needed

### Production Considerations

- Configure proper logging and monitoring
- Set up health checks
- Implement authentication if needed
- Use production ASGI servers like `gunicorn` with `uvicorn` workers
- Consider using a reverse proxy (`nginx`) for production

## 🧪 Testing

Access the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [uvicorn Documentation](https://www.uvicorn.org/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)

---

**Author**: [mehul16](https://github.com/mehul16)  
**Repository**: FastAPI-MLprediction-Demo

---

## 🧪 **Local Deployment and Testing Guide**

### **Step 1: Environment Setup**
```bash
# Clone the repository
git clone https://github.com/mehul16/FastAPI-MLprediction-Demo.git
cd FastAPI-MLprediction-Demo

# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 2: Start the Application**
```bash
# Start the FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Server will start at: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

### **Step 3: Test the API Endpoints**

#### **Test Root Endpoint**
```bash
curl -X GET "http://localhost:8000/"
```
**Expected Response:**
```json
{"message": "FastAPI ML prediction service is running!"}
```

#### **Test Prediction Endpoint with Sample Data**

**Test Set 1: All Zeros**
```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"col1": 0.0, "col2": 0.0, "col3": 0.0, "col4": 0.0, "col5": 0.0, "col6": 0.0, "col7": 0.0, "col8": 0.0, "col9": 0.0}'
```
**Expected Response:** `{"PredictedValue": 0.9618817953225365}`

**Test Set 2: Small Positive Values**
```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"col1": 1.5, "col2": 2.0, "col3": 0.5, "col4": 3.2, "col5": 1.8, "col6": 0.9, "col7": 2.7, "col8": 1.1, "col9": 4.0}'
```
**Expected Response:** `{"PredictedValue": 0.673971264328095}`

**Test Set 3: Mixed Values**
```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"col1": -2.5, "col2": 3.8, "col3": -1.2, "col4": 0.7, "col5": -0.3, "col6": 2.1, "col7": -1.9, "col8": 4.5, "col9": -0.8}'
```
**Expected Response:** `{"PredictedValue": 0.6322957602756805}`

**Test Set 4: Large Values**
```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"col1": 10.0, "col2": 15.5, "col3": 8.2, "col4": 12.7, "col5": 9.3, "col6": 11.8, "col7": 14.1, "col8": 7.6, "col9": 13.9}'
```
**Expected Response:** `{"PredictedValue": -1.4187535968980438}`

**Test Set 5: Decimal Values**
```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"col1": 0.123, "col2": -0.456, "col3": 0.789, "col4": -0.321, "col5": 0.654, "col6": -0.987, "col7": 0.234, "col8": -0.567, "col9": 0.890}'
```
**Expected Response:** `{"PredictedValue": 0.8965879387985408}`

### **Step 4: Interactive Testing**
Visit the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### **Step 5: Stop the Application**
```bash
# Press Ctrl+C in the terminal where uvicorn is running
# Or kill the process:
pkill -f uvicorn
```

### **✅ Test Results Summary**
All test endpoints return HTTP 200 OK responses with accurate ML predictions:
- ✅ Root endpoint functioning
- ✅ Prediction endpoint processing all input types correctly  
- ✅ Model loading and inference working properly
- ✅ JSON serialization working correctly
- ✅ Error handling and validation active

### **🔧 Troubleshooting**
- **Port already in use**: Change port with `--port 8001`
- **Module not found**: Ensure virtual environment is activated and dependencies installed
- **Permission denied**: Check file permissions for `model.pkl`
- **Import errors**: Verify all packages in `requirements.txt` are installed
