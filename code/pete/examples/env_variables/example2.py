import dotenv
import os

dotenv.load_dotenv()

print(os.environ.get('SECRET_KEY'))