from app import create_app, jsonify
import app.eventdata.sync

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return jsonify({'response': 'service zk devices ..'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True, use_reloader=False)
