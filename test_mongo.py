import sys
import os
sys.path.insert(0, "D:/Final year project/Lumina_backend")

try:
    print("Step 1: Testing MongoDB connection...", flush=True)
    from backend.database import client
    server_info = client.server_info()
    print(f"SUCCESS: MongoDB connected! Version: {server_info['version']}", flush=True)
except Exception as e:
    print(f"ERROR connecting to MongoDB: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("\nStep 2: Testing FastAPI import...", flush=True)
    from backend.main import app
    print(f"SUCCESS: FastAPI app imported! Title: {app.title}", flush=True)
    print(f"Routes: {len(app.routes)}", flush=True)
except Exception as e:
    print(f"ERROR importing FastAPI: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nStep 3: All tests passed!", flush=True)
