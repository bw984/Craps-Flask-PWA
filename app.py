from crapsjack import create_app
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = create_app(base_dir)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
