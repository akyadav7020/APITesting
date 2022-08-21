from flask import Flask , request,jsonify

app = Flask(__name__) #Object to access from outer program

#@app.route('/abc',method=['GET','POST']) #@-Notation to run next function,
# #GET -throw URL(search on google),
# #POST- through body(Gmail login)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

if __name__ =='__main__':
    app.run()
