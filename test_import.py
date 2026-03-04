import sys
import os
import importlib.util

# Add user site-packages to sys.path
user_site = r'C:\Users\supri\AppData\Roaming\Python\Python312\site-packages'
if user_site not in sys.path:
    sys.path.insert(0, user_site)

# Set paths
backend_dir = r"D:\Final year project\Lumina_backend"
os.chdir(backend_dir)
sys.path.insert(0, backend_dir)

# Redirect output to file
import io
sys.stdout = sys.stderr = io.StringIO()

try:
    # Load main.py directly
    spec = importlib.util.spec_from_file_location("main", os.path.join(backend_dir, "backend", "main.py"))
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    output = "SUCCESS: main.py imported without errors"
except Exception as e:
    output = f"ERROR: {type(e).__name__}: {e}"

# Write result to file
with open(r"D:\Final year project\Lumina_web\test_result.txt", "w") as f:
    f.write(output)

print(output)
