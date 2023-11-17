from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Хранилище результатов голосования
vote_results = {}

# Обработка голосования
@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    selected_option = data.get('option')

    if selected_option:
        # Записываем результат в хранилище
        vote_results[selected_option] = vote_results.get(selected_option, 0) + 1
        return jsonify({'success': True, 'message': 'Голос принят!'}), 200
    else:
        return jsonify({'success': False, 'message': 'Выберите одну из опций.'}), 400

# Получение результатов голосования
@app.route('/results', methods=['GET'])
def get_results():
    return jsonify({'results': vote_results}), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
