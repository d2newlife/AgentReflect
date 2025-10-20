from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    print("This script is being run directly.")

    print(os.getenv("LANGCHAIN_API_KEY"))