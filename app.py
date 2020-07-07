import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load("model.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[str(x) for x in request.form.values()]]
    d = request.form['education']
    if (d == "college"):
        s1,s2,s3,s4,s5 = 0,0,1,0,0
    if (d == "Below College"):
        s1,s2,s3,s4,s5 = 0,1,0,0,0
    if (d == "Master"):
        s1,s2,s3,s4,s5 = 0,0,0,0,1
    if (d == "Bachelor"):
        s1,s2,s3,s4,s5 = 1,0,0,0,0
    if (d == "doctor"):
        s1,s2,s3,s4,s5 = 0,0,0,1,0
    e = request.form['jobinvolvement']
    if (e == "High"):
        d1 = 0
    if (e == "Medium"):
        d1 = 2
    if (e == "Very high"):
        d1 = 3
    if (e == "Low"):
        d1 = 1

    a = request.form['JobLevel']
    b = request.form['DailyRate(USD)']
    c = request.form['MonthlyIncome(USD)']
    f = request.form['NoofCompaniesWorked']
    g = request.form['TotalWorkingYears']
    h = request.form['YearsAtCompany']
    i = request.form['YearsInCurrentRole']
    j = request.form['YearsSinceLastPromotion']
    k = request.form['YearsWithCurrentManager']
    l = request.form['TrainingTimesLastYear']
    m = request.form['PerformanceRating']
    if (m == "Excellent"):
        m1 = 0
    if (m == "Outstanding"):
        m1 = 1


    total = [[int(s1),int(s2),int(s3),int(s4),int(s5),int(d1),a,b,c,f,g,h,i,j,k,l,int(m1)]]
    sc = load("transform.save") 
    prediction = model.predict(sc.transform(total))
    print(prediction)
    output=prediction[0]
    if(output==0):
        pred="Attrition YES"
    else:
        pred="Attrition NO"
    
    return render_template('index.html', prediction_text='EMPLOYEE {}'.format(pred))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    '''

if __name__ == "__main__":
    app.run(debug=True)
