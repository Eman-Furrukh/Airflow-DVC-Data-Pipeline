# Weather Data Pipeline with DVC and Airflow

This project demonstrates a complete ML pipeline for collecting, preprocessing, and modeling weather data using **DVC**, **Git**, and **Apache Airflow**.

---

## 📁 Project Structure

```
├── dags/
│   └── weather_pipeline_dags.py   # Airflow DAG
├── raw_data.csv              # Collected raw weather data
├── processed_data.csv        # Preprocessed data
├── model.pkl                 # Trained model
├── main.py                   # Data collection script
├── process_data.py           # Data preprocessing script
├── train_model.py            # Model training script
├── dvc.yaml                  # DVC pipeline definition
├── dvc.lock                  # DVC lock file
├── requirements.txt          # Python dependencies
├── docker-compose.yaml       # Airflow setup
├── .dvcignore
├── .gitignore
└── README.md                 # This file
```

---

## ✅ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your_repo_url>
cd Airflow-DVC-Data-Pipeline
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Linux/macOS
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up DVC
```bash
dvc init
dvc remote add -d myremote <remote_url>
```

If you use Google Drive:
```bash
pip install dvc[gdrive]
```

### 5. Setup and Launch Airflow
```bash
pip install apache-airflow
```

#### Recommended (Dockerized Airflow Setup)
```bash
docker-compose up airflow-init
docker-compose up
```

Access Airflow UI at: [http://localhost:8081](http://localhost:8081)

---

## 🔁 Pipeline Breakdown with DVC

### Add DVC Stages
```bash
# Data Collection
dvc stage add -n collect_data -o raw_data.csv python main.py

# Data Preprocessing
dvc stage add -n preprocess_data -d raw_data.csv -d process_data.py -o processed_data.csv python process_data.py

# Model Training
dvc stage add -n train_model -d processed_data.csv -d train_model.py -o model.pkl python train_model.py
```

### Run Full Pipeline
```bash
dvc repro
```

### Track and Push Artifacts
```bash
git add dvc.yaml dvc.lock .gitignore

git commit -m "Add DVC pipeline"

dvc push  # Push data and model to DVC remote
```

---

## 🚀 Running Pipeline via Airflow

### DAG file (inside `dags/airflow_pipeline.py`)
Make sure your DAG includes three PythonOperator tasks:
- `collect_data_task`
- `preprocess_data_task`
- `train_model_task`

Then run Airflow:
```bash
docker-compose up
```

### Airflow UI
Visit: [http://localhost:8081](http://localhost:8081) and trigger the DAG manually or set a schedule interval.

---

## 🔄 Summary: Commands to Run Project from Scratch

```bash
git clone <your_repo_url>
cd Airflow-DVC-Data-Pipeline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# DVC setup
dvc init
pip install dvc[gdrive]  # if using Google Drive

dvc pull  # Fetch tracked files (if available)

# Airflow setup
pip install apache-airflow  # Optional if using docker-compose

# Run pipeline
# Option 1: via DVC
dvc repro

# Option 2: via Airflow
# (Dockerized)
docker-compose up airflow-init
docker-compose up
```



