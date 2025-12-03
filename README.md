# 🩺 Diabetes Risk Prediction App

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
[![Model](https://img.shields.io/badge/Model-GaussianNB-green)](https://scikit-learn.org/)

## 📄 Overview
This project is a **Web Application** that predicts the probability of diabetes based on diagnostic measures. 

It is based on a **Comparative Analysis** of Naive Bayes classifiers, where **Gaussian Naive Bayes** was identified as the most accurate model (90.48% Accuracy) for this dataset.

## 🚀 Live Demo
You can run this app locally by following the installation steps below.

## 📊 Methodology
We compared three variants of Naive Bayes:
1.  **Gaussian NB:** Best for continuous features (Glucose, BMI). **(Selected Model)**
2.  **Bernoulli NB:** Best for binary features.
3.  **Multinomial NB:** Best for count data.

### Key Metrics
| Model | Accuracy |
|-------|----------|
| **Gaussian NB** | **90.48%** |
| Bernoulli NB | ~88% |
| Multinomial NB | ~76% |

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Muhammad-Shahan/Diabetes-Risk-Prediction.git](https://github.com/Muhammad-Shahan/Diabetes-Risk-Prediction.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure
* `app.py`: The main Streamlit interface.
* `train_model.py`: Script used to train and save the model.
* `analysis.ipynb`: Jupyter Notebook containing the research and EDA.
* `diabetes_model.pkl`: The trained GaussianNB model file.
* `diabetes_prediction_dataset.csv`: The dataset used for training.

## 🤝 Citation
If you find this useful, please star the repo!
