from django.shortcuts import render
# from tablib import Dataset
from .models import Employee,DataExcel,error
import pandas as pd
from .task import ImportExcle
from .forms import FileForm
from django_celery_results.models import TaskResult
# from .resource import EmployeeResource
# import tablib
# from import_export import resources

# Create your views here.

def ImportData(request):
    if request.method=="POST":
        idlist=[]
        outfile=[]
        status=False
        files=request.FILES.getlist('excel_file')
     
        for i in range(0,len(files)):
            if files[i].name.endswith('.csv'):
                data=DataExcel.objects.create(excel_file=files[i])
                idlist.append(data.id)
            elif files[i].name.endswith('.xlsx'):
                data=DataExcel.objects.create(excel_file=files[i])
                idlist.append(data.id)
            else:
                outfile.append(str(files[i]))
                error=True
        
        if  idlist :
            task_id=ImportExcle.delay(idlist)
            status=True
            
        error_data = ",".join(outfile)
        
        # ImportExcle.delay(data.id)
        # print(form.cleaned_data,"view clean data")
            # for i in files:
            #     data=DataExcel.objects.create(excel_file=i)
            #     idlist.append(data.id)
        
            # ImportExcle.delay(data.id)
        # print(form)
        return render(request, "import.html",locals())
    return render(request, "import.html")
    

            # data=DataExcel.objects.create(excel_file=file)
            # print(data)
            # print(data.id)
            # id=data.id
            # excel_file= pd.ExcelFile(file)
            # d=pickle.dumps(excel_file)
        # new_user=request.FILES['excel_file']
        # print(new_user)
        
        # excel_file= pd.ExcelFile(new_user)
        # with open(excel_file, 'r') as f:
        #     file_contents = f.read()
        # ImportExcle.delay(file_contents)
        # print(excel_file)
        # all_sheets=excel_file.sheet_names
        # print(all_sheets)
        # df=pd.read_excel(new_user,index_col=None,sheet_names='Sheet1')
        # df = pd.read_excel(excel_file,index_col=None)
        # data=df.dropna()
        # print("null",df.isnull())
        # print(data)
        # records = data.to_dict('records')
        # print(records)
        
        # for row in records:
        #     if Employee.objects.filter(email=row['email']).exists():
        #         try:
        #             Employee.objects.filter(email=row['email']).update(first_name=row['first_name'],last_name=row['last_name'],phone=row['phone'],position=row['position'],address=row[ 'address'],age=row[ 'age'])
        #         except:
        #             pass
        #     else:
        #         try:
                    
        #             Employee.objects.create(**row)
        #         except Exception as e:
        #             print(e)

        # print(excel_file)
        # all_sheets=excel_file.sheet_names
        # print(all_sheets)
        # df=pd.read_excel(new_user,index_col=None,sheet_names='Sheet1')
        # data_index=df.columns.get_loc('first_name')
        # for row in df.values:
        #     print(row)
        #     # Employee.objects.update_or_create(fi)
        #     print(row[data_index])
        # # user_resource=EmployeeResource()
        # # dataset=Dataset()
        # new_user=request.FILES['excel_file']
        # # imported_data=dataset.load(new_user.read(),format='xlsx')
        # # for data in imported_data:
        # #     value=Employee(
        # #         data[0],
        # #         data[1],
        # #          data[2],
        # #           data[3],
        # #            data[4],
        # #             data[5]
        # #     )
        # #     value.save()
        # book_resource = resources.modelresource_factory(model=Employee)()
        # dataset = Dataset( headers=['first_name','last_name','email','phone','position','address','age']).load(new_user.read(),format='xlsx')
        # result = book_resource.import_data(dataset)
        # print(result.has_errors())
            
        
    # return render(request, "import.html")

def taskes(request):
    data=TaskResult.objects.all()
    return render(request, "task.html",locals())

def task_error(request,id):
    print(id)
    data=error.objects.filter(error_key=id)
    return render(request, 'eror.html',locals())
    