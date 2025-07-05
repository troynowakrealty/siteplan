import sysnimport osnsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from flask import Flask, request, jsonify
import importlib

app = Flask(__name__)

@app.route('/run-task', methods=['POST'])
def run_task():
    data = request.get_json()
    task_name = data.get('task')
    params = data.get('params', {})
    try:
        module = importlib.import_module(f"codex_tasks.{task_name}")
        result = module.run(params)
        return jsonify({'result': result, 'error': None})
    except Exception as e:
        return jsonify({'result': None, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000 if 'siteplan' == 'local-agent' else (8001 if 'siteplan' == 'web-agent' else 8002))
