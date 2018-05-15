from flaskext.mysql import MySQL
from flask import Flask, request

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'yash1998'
app.config['MYSQL_DATABASE_DB'] = 'address'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con = mysql.connect()
cur = con.cursor()


@app.route('/add/', methods=['GET'])
def add_record():
    if request.method == 'GET':
        house_name = request.args.get('name')
        city = request.args.get('city')
        state = request.args.get('state')
        print(house_name)
        print(city)
        print(state)
        try:
            query = 'INSERT INTO data (house_name, city, state) VALUES ("' + house_name + '","' + city + '","' + state +'")'
            cur.execute(query)
            con.commit()
            print("Data successfully added.")
            msg = "Data successfully added."
        except Exception as e:
            print(str(e))
            print("Data could not be added.")
            msg = "Data could not be added."
        finally:
            return msg


if __name__ == '__main__':
    app.run(debug=True)
