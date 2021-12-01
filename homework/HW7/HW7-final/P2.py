# Part A
import sqlite3
import pandas as pd
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

###################################################
# Part B Function
def save_to_database(model_id, model_desc, db, model, X_train, X_test,y_train, y_test):
    
    # model params
    params_dict = model.get_params()
    param_name = list(params_dict.keys())
    param_value = list(params_dict.values())
    

    for i in range(len(param_name)):
        cursor.execute('''INSERT INTO model_params
                  (id, desc, param_name, value)
                  VALUES (?, ?, ?, ?)''', (int(model_id),model_desc,param_name[i],param_value[i]))
  
    
    # #model coef
    coef = list(model.coef_[0])
    intercept = model.intercept_[0]
    coef.insert(0, intercept)
    feature_name = list(X_train.columns)
    feature_name.insert(0, 'intercept')
    
    for j in range(len(feature_name)):
        cursor.execute('''INSERT INTO model_coefs
                  (id, desc, feature_name, value)
                  VALUES (?, ?, ?, ?)''', (int(model_id),model_desc,feature_name[j],coef[j]))
    
    # scores/model results
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    cursor.execute('''INSERT INTO model_results
                  (id, desc, train_score, test_score)
                  VALUES (?, ?, ?, ?)''', (int(model_id),model_desc,train_score,test_score))
    
    db.commit()
    
###################################################
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")


cursor.execute('''CREATE TABLE model_params (
               id INTEGER,
               desc TEXT,
               param_name TEXT,
               value FLOAT)''')

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER,
               desc TEXT,
               feature_name TEXT,
               value FLOAT)''')

cursor.execute('''CREATE TABLE model_results (
               id INTEGER,
               desc TEXT,
               train_score FLOAT,
               test_score FLOAT)''')

db.commit() # Commit changes to the database

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)


###################################################
## Part B adding to database
# baseline
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

#reduced
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
save_to_database(3, 'L1 penalty model', db, penalized_model, X_train, X_test, y_train, y_test)

# see data base
def viz_tables(cols, query):
    q = cursor.execute(query).fetchall()
    framelist = dict()
    for i, col_name in enumerate(cols):
        framelist[col_name] = [row[i] for row in q]
    return pd.DataFrame.from_dict(framelist)

###################################################
# Part C
model_cols = [col[1] for col in cursor.execute("PRAGMA table_info(model_results)")]
query = '''SELECT * FROM model_results'''
print("Table showing the model results:")
print(viz_tables(model_cols, query), '\n')

query = '''SELECT id FROM model_results ORDER BY test_score DESC limit 1'''
cursor.execute(query)
best_id = cursor.fetchall()[0][0]
print("Best model id:", best_id, '\n')

query = '''SELECT test_score FROM model_results ORDER BY test_score DESC limit 1'''
cursor.execute(query)
val_score = cursor.fetchall()[0][0]
print("Best validation score:",val_score, '\n')

# Query the coefs
query = '''SELECT feature_name,value FROM model_coefs WHERE id == 3'''
cursor.execute(query)
print("Coefficient list:",cursor.fetchall(), '\n')

# Dummy fit
test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
query = '''SELECT value FROM model_coefs WHERE id == 3'''
cursor.execute(query)
coef = cursor.fetchall()

coef_list = []
for i in range(len(coef)):
    coef_list.append(coef[i][0])

test_model.coef_ = np.array([coef_list[1:]])
test_model.intercept_ = np.array([coef_list[0]])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.close()
