from flask import Flask, render_template
from modules.module import document_scanner
app = Flask(__name__)
 
@app.route('/')
def library():
    title = "x3beche - library"
    return render_template('library.html', title = title, documents=document_scanner())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)