import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model(data_file):
    """
    Trains a machine learning model using the provided data file and returns the trained model.
    """
    # Load the data into a Pandas DataFrame
    data = pd.read_csv(data_file)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), data['target'], test_size=0.2, random_state=42)
    
    # Train a logistic regression model on the training data
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model on the testing data
    score = model.score(X_test, y_test)
    print(f"Model accuracy: {score:.2f}")
    
    # Return the trained model
    return model
