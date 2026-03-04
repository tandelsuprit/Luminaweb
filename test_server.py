import sys
import os
sys.path.insert(0, "D:/Final year project/Lumina_backend")

try:
    from backend.main import app
    print("SUCCESS: FastAPI app imported successfully!")
    print(f"App title: {app.title}")
    print(f"Available routes: {len(app.routes)}")
    for route in app.routes:
        if hasattr(route, 'path'):
            print(f"  - {route.path}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
