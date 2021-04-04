import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from Data.Variables import *


class Logistic:

    def ranking(self, predict_array):
        # Importing the dataset
        dataset = pd.read_csv(issue_history_csv)
        X = dataset.iloc[:, [0, 1, 2]].values
        y = dataset.iloc[:, 3].values

        # Splitting the dataset into the Training set and Test set
        # from sklearn.model_selection import train_test_split

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

        # Feature Scaling
        #

        # sc = StandardScaler()
        # X_train = sc.fit_transform(X)
        # X_test = sc.transform(X_test)

        # print(X_train)
        # Fitting Logistic Regression to the Training set

        model = LogisticRegression(random_state=0, max_iter=400)
        model.fit(X, y)

        import pickle

        filename = rank_model_path
        pickle.dump(model, open(filename, 'wb'))

        # some time later...

        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
        # result = loaded_model.score(X_test, y_test)
        # print(result)

        # Predicting the  results
        y_pred = loaded_model.predict([predict_array])
        print(y_pred)
        return y_pred
