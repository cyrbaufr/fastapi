# 1. Library imports
import uvicorn
from fastapi import FastAPI
from CreditScores import CreditScore
import numpy as np
import pickle
import pandas as pd


# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier_final.pkl","rb")
classifier=pickle.load(pickle_in)

def out_of_range(var_name, var_num,
                msg=" field must take value 0 (No) or 1 (Yes)"):
    error_msg = var_name + " field must take value 0 (No) or 1 (Yes)"
    error = {"Error": error_msg}
    if (var_num>1) or (var_num<0):
        return error

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to the Home Page of Credit Scoring API'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Credit Score with the confidence
@app.post('/predict')
def predict_creditscore(data:CreditScore):
    data = data.dict()
    EXT_SOURCE_3 = data['EXT_SOURCE_3']
    EXT_SOURCE_2 = data['EXT_SOURCE_2']
    AMT_CREDIT = data['AMT_CREDIT']
    FLAG_DOCUMENT_3 = data['FLAG_DOCUMENT_3']
    out_of_range('FLAG_DOCUMENT_3', FLAG_DOCUMENT_3)
    AMT_GOODS_PRICE = data['AMT_GOODS_PRICE']
    CODE_GENDER = data['CODE_GENDER']
    out_of_range('CODE_GENDER', CODE_GENDER,
                 msg=" field must take value 0 (Female) or 1 (Male)")
    INSTAL_DAYS_ENTRY_PAYMENT_MAX = data['INSTAL_DAYS_ENTRY_PAYMENT_MAX']
    INSTAL_DAYS_ENTRY_PAYMENT_MEAN = data['INSTAL_DAYS_ENTRY_PAYMENT_MEAN']
    DAYS_EMPLOYED = data['DAYS_EMPLOYED']
    NAME_INCOME_TYPE_Working = data['NAME_INCOME_TYPE_Working']
    out_of_range('NAME_INCOME_TYPE_Working', NAME_INCOME_TYPE_Working)


    # print(classifier.predict([[EXT_SOURCE_3, EXT_SOURCE_2,
    #                            AMT_CREDIT, FLAG_DOCUMENT_3,
    #                            AMT_GOODS_PRICE, CODE_GENDER,
    #                            INSTAL_DAYS_ENTRY_PAYMENT_MAX,
    #                            INSTAL_DAYS_ENTRY_PAYMENT_MEAN,
    #                            DAYS_EMPLOYED,
    #                            NAME_INCOME_TYPE_Working]]))
    prediction = classifier.predict([[EXT_SOURCE_3, EXT_SOURCE_2,
                                      AMT_CREDIT, FLAG_DOCUMENT_3,
                                      AMT_GOODS_PRICE, CODE_GENDER,
                                      INSTAL_DAYS_ENTRY_PAYMENT_MAX,
                                      INSTAL_DAYS_ENTRY_PAYMENT_MEAN,
                                      DAYS_EMPLOYED,
                                      NAME_INCOME_TYPE_Working]])
    if(prediction[0]>0.5):
        prediction = "Credit default"
    else:
        prediction = "Credit Reimbursed"
    return {
        'prediction': prediction,
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload