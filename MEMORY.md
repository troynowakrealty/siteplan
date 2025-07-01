My system includes a persistent local agent (`local-agent`) running on http://localhost:5001. It exposes `POST /run-task`, which executes tasks from a `/tasks` directory. Each task is a Python file with a `run(params)` function.

I use `local-agent` to verify that other agents like `web-agent`, `siteplan`, and `3D Home Gen` are working correctly. After building or fixing a task (like `tasks/shell.py`) in another agent, I send a curl command to local-agent like this:

```bash
curl -X POST http://localhost:5001/run-task \
  -H "Content-Type: application/json" \
  -d '{"task":"shell","params":{"command":"cd /Volumes/SSD/GITHUB/AGENT_NAME && python3 tasks/shell.py"}}'
```

I expect a JSON response with `"status": "success"` and `"result"` matching the shell output. If the result is missing or an error occurs, Codex should fix the broken task or file and retry until the test passes.

All agents follow the same layout:
- `api_server.py` with dynamic task loading
- `tasks/shell.py`
- `verify_with_local_agent.sh` for local testing

This pattern should be reused for all new agents unless I instruct otherwise. Always verify through local-agent, not internal mocks.
