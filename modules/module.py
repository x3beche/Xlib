from os import scandir, getcwd, path
from time import localtime

def document_scanner():
    documents = []
    for i,d in enumerate(scandir(getcwd()+"/static/documents")):
        file_dir = getcwd()+f"/static/documents/{d.name}"
        file_size = str(round(path.getsize(file_dir)*0.000001, 2))+" MB"
        year,month,day=localtime(path.getmtime(file_dir))[:-6]
        creation_date = "%02d/%02d/%d"%(day,month,year)
        documents.append({"id":str(i+1), "name":d.name, "title":d.name.rsplit(".",1)[0].replace("_"," "), "size":file_size, "date":creation_date})
    return documents