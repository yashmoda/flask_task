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


@app.route('/delete/', methods=['GET'])
def delete_record():
    if request.method == 'GET':
        house_id = request.args.get('id')
        print(id)
        try:
            query = 'SELECT * from data where house_id='+house_id
            print('\n\n\n')
            cur.execute(query)
            for row in cur:
                query = 'INSERT INTO changed_data (house_name, city, state) VALUES ("' + row[1] + '","' + row[2] + '","' + row[3] + '")'
                print ('\n\n\n')
                cur.execute(query)
            query = 'delete from data where house_id='+house_id
            cur.execute(query)
            print (con.commit())
            print("Data deleted successfully.")
            msg = "Data deleted successfully."
        except Exception as e:
            print(str(e))
            print("Data does not exist.")
            msg = "Data does not exist."
        finally:
            return msg


if __name__ == '__main__':
    app.run(debug=True)
