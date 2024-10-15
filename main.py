from dotenv.main import load_dotenv

load_dotenv()

from albums_python.app import app

if __name__ == "__main__":
    app.run(port=5001)
