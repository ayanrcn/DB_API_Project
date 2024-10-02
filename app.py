from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1996",
    database="DB_API_Project"
)
cursor = db.cursor()

#Add data
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'User added successfully!'}), 201

#Read data
@app.route('/api/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

#Read by ID
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    return jsonify(user)

#Update
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (data['name'], data['email'], id)
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'User updated successfully!'})

#Delete
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    db.commit()
    return jsonify({'message': 'User deleted successfully!'})

#Run flask
#if __name__ == '__main__':
    #app.run(debug=True)





