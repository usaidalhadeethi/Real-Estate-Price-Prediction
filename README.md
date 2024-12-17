# Real-Estate-Price-Prediction

## This project demonstrates the use of machine learning to predict numerical values using Ridge Regression. The model is trained on a custom dataset and deployed on a local web application using Streamlit.


## Project Files:

* **veri.ipynb:** Generates the custom dataset (veri.csv).
* **algoritma.ipynb:** Trains and evaluates machine learning models; selects the best model.
* **eniyi.joblib:** The best-performing model for predictions.
* **veri.csv:** The custom dataset used for training models.
* **app.py:** Streamlit app for real-time predictions using the Ridge Regression (the best-performing model) model.
* **requirements.txt:** Lists dependencies required for the project.

# Best Algorithm

    Algorithm Used: Ridge Regression
    RMSE: 11952.31
    R²: 0.9582 (95.82% variance explained)


# How to Run
1. Clone the repository:
```
   git clone https://github.com/yourusername/ml-model-deployment.git
```
```
   cd ml-model-deployment
```

3. Install dependencies:
```
   pip install -r requirements.txt
```

5. Run the Streamlit app:
```
   streamlit run app.py
```

## App UI :
![Screenshot 2024-12-18 013542](https://github.com/user-attachments/assets/b2f587aa-9546-472d-bac3-f22708d34dbb)

