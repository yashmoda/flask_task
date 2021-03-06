import json

from flaskext.mysql import MySQL
from flask import Flask, request, render_template, redirect, url_for
import time

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'yash1998'
app.config['MYSQL_DATABASE_DB'] = 'address'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con = mysql.connect()
cur = con.cursor()


@app.route('/')
def home():
    response_json = {'data': [], 'changed_data': []}
    try:
        query = 'select * from data'
        print("Time taken")
        start = time.clock()
        cur.execute(query)
        print(time.clock() - start)
        for row in cur:
            temp_json = {'id': row[0],
                         'name': row[1],
                         'city': row[2],
                         'state': row[3]}
            response_json['data'].append(temp_json)
        query = 'select * from changed_data'
        cur.execute(query)
        for row in cur:
            temp_json = {'id': row[0],
                         'name': row[1],
                         'city': row[2],
                         'state': row[3]}
            response_json['changed_data'].append(temp_json)
        con.commit()
        print(str(response_json))
        print("Data shown.")
    except Exception as e:
        print(str(e))
        print("Data could not be shown.")
    finally:
        return render_template('home.html', response=response_json)


@app.route('/show_add/')
def show_add():
    return render_template('add.html')


@app.route('/show_edit/')
def show_edit():
    return render_template('edit.html')


@app.route('/add/', methods=['POST'])
def add_record():
    if request.method == 'POST':
        house_name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        print(house_name)
        print(city)
        print(state)
        try:
            query = 'INSERT INTO data (house_name, city, state) VALUES (%s, %s, %s)'
            data = (house_name, city, state)
            print("Time taken")
            start = time.clock()
            cur.execute(query, data)
            print(time.clock() - start)
            con.commit()
            print("Data successfully added.")
        except Exception as e:
            print(str(e))
            print("Data could not be added.")
        finally:
            return redirect('/', 200)


@app.route('/delete/', methods=['GET'])
def delete_record():
    if request.method == 'GET':
        house_id = request.args.getlist('id')
        print(house_id)
        print('\n\n\n\n\n')
        ids = json.loads(house_id[0])
        print("Time taken")
        start = time.clock()
        for i in ids['ids']:
            print (i)
            try:
                query = 'SELECT * from data where house_id=%s'
                data = i
                print ('\n\n\n')
                cur.execute(query, data)
                for row in cur:
                    query = 'INSERT INTO changed_data (house_name, city, state) VALUES (%s, %s, %s)'
                    data = (row[1], row[2], row[3])
                    print ('\n\n\n')
                    cur.execute(query, data)
                query = 'delete from data where house_id=%s'
                data = i
                cur.execute(query, data)
                print (con.commit())
                print("Data deleted successfully.")
            except Exception as e:
                print(str(e))
                print("Data does not exist.")
            finally:
                print(time.clock() - start)
        return redirect('/', 200)


@app.route('/modify/', methods=['POST'])
def modify_record():
    print('\n\n\n\n\n')
    if request.method == 'POST':
        house_id = request.form['id']
        print(house_id)
        house_name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        print(house_name)
        print(city)
        print(state)
        try:
            print("Time taken")
            start = time.clock()
            query = 'SELECT * from data where house_id = %s'
            data = house_id
            cur.execute(query, data)
            for row in cur:
                print(row[1])
                query = 'INSERT INTO changed_data (house_name, city, state) VALUES (%s, %s, %s)'
                data = (row[1], row[2], row[3])
                print ('\n\n\n')
                cur.execute(query, data)
            query = 'update data set house_name = %s, city = %s, state = %s where house_id = %s'
            data = (house_name, city, state, house_id)
            cur.execute(query, data)
            print(time.clock()-start)
            con.commit()
            print "Data fetched."
        except Exception as e:
            print(str(e))
            print ("Data not modified.")
        finally:
            return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
