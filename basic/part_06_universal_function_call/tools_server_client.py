import subprocess
import json

class ToolsServerClient:
    def __init__(self, server_script):
        self.server_script = server_script
        self.proc = None

    def __enter__(self):
        self.proc = subprocess.Popen(
            ['uv', 'run', self.server_script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        return self

    def call_function(self, name, arguments):
        command = {
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            }
        }
        command_json = json.dumps(command)
        self.proc.stdin.write(command_json + '\n')
        self.proc.stdin.flush()
        for line in self.proc.stdout:
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.proc:
            self.proc.terminate()
