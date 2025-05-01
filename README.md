# 🌦️ Airflow-DVC Weather Data Pipeline

This project is a complete data pipeline for collecting, preprocessing, and training a Linear Regression model on weather data using **DVC (Data Version Control)** and **Apache Airflow** for orchestration.

## 📁 Project Structure

```
🔍
🔹 main.py                  # Collects raw weather data
🔹 process_data.py          # Cleans and preprocesses raw data
🔹 train_model.py           # Trains linear regression model
🔹 model.pkl                # Trained model file (generated)
🔹 raw_data.csv             # Raw data (generated)
🔹 processed_data.csv       # Cleaned data (generated)
🔹 dvc.yaml                 # DVC pipeline stages
🔹 dvc.lock                 # Locked versions of inputs/outputs
🔹 requirements.txt         # Python dependencies
🔹 README.md
🔹 .dvc/                    # DVC config directory
```

---

## ✅ Step-by-Step Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Airflow-DVC-Data-Pipeline.git
cd Airflow-DVC-Data-Pipeline
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Activate environment:
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up DVC and Pull Data

```bash
# Initialize DVC (only needed once if starting fresh)
dvc init

# Pull data and model files from remote
dvc pull
```

---

## 🚀 Running the DVC Pipeline

This will automatically run all stages:

```bash
dvc repro
```

Stages run in order:
1. `collect_data` → runs `main.py` → saves `raw_data.csv`
2. `preprocess_data` → runs `process_data.py` → saves `processed_data.csv`
3. `train_model` → runs `train_model.py` → saves `model.pkl`

---

## 🛄 Pushing Changes 

If you've made changes (e.g., retrained the model):

```bash
# Add changed files
git add .
git commit -m "Updated model or data"

# Push to DVC remote
dvc push

# Push code to GitHub
git push
```

---

## 🔀 Summary of Key Commands

```bash
# Clone repo
git clone <repo-url>
cd <repo-folder>

# Set up environment
python -m venv venv
.\venv\Scripts\activate  # (or source venv/bin/activate)

# Install dependencies
pip install -r requirements.txt

# Pull data and model
dvc pull

# Reproduce entire pipeline
dvc repro
```
