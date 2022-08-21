from flask import  Flask ,request
import mysql.connector as conn

app = Flask(__name__)


@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')

    return "this is my first function for get {} {} {}".format(get_name ,mobile_number,mail_id )

@app.route("/getData")
def get_data():
    db = request.args.get("db")
    tn = request.args.get("tn")
    mydb = conn.connect(host="localhost", user="root", passwd="root@123")
    cursor = mydb.cursor()
    cursor.execute("select * from {}.{}".format(db,tn))
    l = []
    for i in cursor.fetchall():
        l.append(str(i))
    return (l)
if __name__=="__main__":
    app.run(port= 5002)