from django.shortcuts import render
# from tablib import Dataset
from .models import Employee,DataExcel,error
import pandas as pd
from celery import shared_task,current_task
# import pickle


@shared_task
def ImportExcle(data):
    for id in data:
        data=DataExcel.objects.get(id=id)
        if ".xlsx" in str(data.excel_file):
            
            df = pd.read_excel(data.excel_file)
            
        else:
            df= pd.read_csv(data.excel_file)
   
        for index, row in df.iterrows():
            null_columns =row.isnull()
            col=null_columns[null_columns].index.tolist()
            if not  col :
                if Employee.objects.filter(email=row['email']).exists():
                    try:
                        Employee.objects.filter(email=row['email']).update(first_name=row['first_name'],last_name=row['last_name'],phone=row['phone'],position=row['position'],address=row[ 'address'],age=row[ 'age'])
                    except:
                        pass
                else:
                    try:
                        
                        Employee.objects.create(**row)
                    except Exception as e:
                        print(e)
            else:
                null_col = ",".join(col)
                error_data=f'the {index + 2} row {null_col} has a null values'
                error.objects.create(error_key=ImportExcle.request.id,error=error_data)
                
                    
        