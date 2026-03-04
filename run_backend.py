import sys
import os
import site

# Add user site-packages to sys.path for ultralytics
user_site = site.getusersitepackages()
if user_site not in sys.path:
    sys.path.insert(0, user_site)

# Set path to Lumina_backend directory
base_dir = os.path.join(os.path.dirname(__file__), '..', 'Lumina_backend')
sys.path.insert(0, base_dir)

from backend.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
