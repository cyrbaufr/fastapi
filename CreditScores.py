"""
This file indicates the format of features expected
to predict if a credit wll be reimbursed or not
"""

from pydantic import BaseModel

# Class which describes features used for credit scoring
class CreditScore(BaseModel):
    EXT_SOURCE_3: float
    EXT_SOURCE_2: float
    AMT_CREDIT: float
    FLAG_DOCUMENT_3: int
    AMT_GOODS_PRICE: float
    CODE_GENDER: int
    INSTAL_DAYS_ENTRY_PAYMENT_MAX: float
    INSTAL_DAYS_ENTRY_PAYMENT_MEAN: float
    DAYS_EMPLOYED: float
    NAME_INCOME_TYPE_Working: int
