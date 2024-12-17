# Real-Estate-Price-Prediction

This project demonstrates the use of machine learning to predict numerical values using Ridge Regression. The model is trained on a custom dataset and deployed on a local web application using Streamlit.

veri.ipynb: Generates the custom dataset (veri.csv).
algoritma.ipynb: Trains and evaluates machine learning models; selects the best model.
eniyi.joblib: The best-performing model for predictions.
veri.csv: The custom dataset used for training models.
app.py: Streamlit app for real-time predictions using the Ridge Regression (the best-performing model) model.
requirements.txt: Lists dependencies required for the project.

Best Algorithm

    Algorithm Used: Ridge Regression
    RMSE: 11952.31
    R²: 0.9582 (95.82% variance explained)

How to Run
1. Clone the repository:
git clone https://github.com/yourusername/ml-model-deployment.git
cd ml-model-deployment

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py
