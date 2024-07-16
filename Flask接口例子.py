from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    try:
        data = request.get_json()  # 获取POST请求中的JSON数据
        name = data.get('name')
        id = data.get('id')
        age = data.get('age')
        
        return jsonify({
            "name": name,
            "id": id,
            "age": age
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
