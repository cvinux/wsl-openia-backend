from dotenv import load_dotenv
from app.services.openai_service import ask_openai

load_dotenv()

def main():
    prompt = "Explícame qué es Docker en una frase"
    print("\n--- OpenAI ---")
    print(ask_openai(prompt))

if __name__ == "__main__":
    main()