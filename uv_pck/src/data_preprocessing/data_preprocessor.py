from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin 



class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, config):
        self._is_fitted = False
        self.config = None

    def fit(self, X, y=None):
        pass

    def transform(self, X): 
        # Implement your data preprocessing logic here
        # For example, handling missing values, encoding categorical variables, etc.
        return X    
    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)

     