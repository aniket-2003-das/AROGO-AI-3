# Self-Analysis Mental Health Prediction Model

A machine learning system that predicts 17 mental health conditions based on user-reported symptoms, with model interpretability and a Streamlit UI.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Model Development](#model-development)
- [Inference Script](#inference-script)
- [User Interface](#user-interface)
- [LLM Integration (Optional)](#llm-integration-optional)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## Features ✨
- Predicts 14 mental health conditions using clinical thresholds.
- Compares Random Forest and XGBoost models.
- LIME-based model interpretation.
- Streamlit web interface for easy interaction.
- Pre-trained models for production deployment.
- Inference script for API integration.

---

## Installation ⚙️

### Requirements
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/mental-health-prediction.git
cd mental-health-prediction

# Install dependencies
pip install -r requirements.txt
```

---

## BUILD Command 🚀
### Running the script
```markdown
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Define model name and directory
model_name = "t5-small"  # Replace with "t5llm-small" if available
save_directory = "./t5llm_model"  # Change to your preferred path

# Load the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save model and tokenizer to the directory
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

print(f"Model and tokenizer saved to {save_directory}")

```

### Features
- Input symptoms through the web interface.
- View predictions with explanations.
- Explore model interpretation visualizations.
---

## Data Preparation 📊

### Dataset Structure
- 800 entries with 19 clinical features.
- Key features include:
  - **PHQ-9 (Depression) scores**
  - **GAD-7 (Anxiety) scores**
  - **Epworth Sleepiness scores**
  - **BMI categories**
  - **Demographic information**

### Preprocessing Steps
- Missing value imputation (median/mode)
- Categorical encoding (LabelEncoder)
- Feature normalization (MinMaxScaler)
- Target engineering for 17 conditions
- Train-test split (80-20 ratio)

---

## Model Development 🤖

### Evaluation Metrics
```json
{
  "accuracy": 0.86,
  "precision": 0.88,
  "recall": 0.85,
  "f1": 0.86,
  "roc_auc": 0.93
}
```

### Selected Model: **Logistic Regression**
- Higher **ROC-AUC (0.95 vs 0.93)**.
- Better handling of **class imbalance**.
- Faster **inference times**.
---

## Inference Script 📄

### Usage
```python
from predict_mental_health import load_models, predict_mental_health

# Load trained models
models = load_models()

# Create input dictionary
input_data = {
    'age': 25,
    'gender': 1,
    'phq_score': 14,
    # ... other features
}

# Get predictions
predictions = predict_mental_health(input_data, models)
```

---

## User Interface 🖥️

### Streamlit App Components
- Input widgets for symptoms and scores.
- Real-time prediction display.
- SHAP force plots for model explainability.
- Suggested coping mechanisms.
- Exportable diagnostic reports.

---

## LLM Integration  💡
For natural language explanations:
- Provide natural language explanations for predicted mental health conditions.
- Suggest coping mechanisms and potential next steps.
- Option 2: Fine-tune a small transformer model (e.g., BERT, T5) for mental health explanations.

---



---

## Contributing 🤝
1. Fork the repository.
2. Create your feature branch.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

---

## License 📜
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer ⚠️
This tool does **NOT** replace professional medical advice. Always consult a qualified healthcare provider for mental health concerns.
