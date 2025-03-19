# ============================================================
# Day 84-86: AI Integration — Chatbot using OpenAI/Gemini APIs
# ============================================================
# pip install openai google-generativeai python-dotenv
# ============================================================

import os

# ============================================================
# OPTION A: OpenAI ChatGPT
# ============================================================
# pip install openai
# Get key at: https://platform.openai.com/api-keys

def openai_chatbot():
    """Simple terminal chatbot using OpenAI GPT."""
    try:
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        print("🤖 OpenAI Chatbot (type 'quit' to exit)")
        print("-" * 40)

        conversation_history = [
            {"role": "system", "content": "You are a helpful Python programming tutor."}
        ]

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit"]:
                break

            conversation_history.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                max_tokens=500,
            )

            assistant_reply = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": assistant_reply})
            print(f"\n🤖 GPT: {assistant_reply}\n")

    except ImportError:
        print("pip install openai")
    except Exception as e:
        print(f"Error: {e}")

# ============================================================
# OPTION B: Google Gemini
# ============================================================
# pip install google-generativeai
# Get key at: https://aistudio.google.com/app/apikey

def gemini_chatbot():
    """Simple terminal chatbot using Google Gemini."""
    try:
        import google.generativeai as genai

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash")
        chat  = model.start_chat(history=[])

        print("🤖 Google Gemini Chatbot (type 'quit' to exit)")
        print("-" * 40)

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit"]:
                break

            response = chat.send_message(user_input)
            print(f"\n🤖 Gemini: {response.text}\n")

    except ImportError:
        print("pip install google-generativeai")
    except Exception as e:
        print(f"Error: {e}")

# ============================================================
# MAIN MENU
# ============================================================
if __name__ == "__main__":
    print("=== Day 84-86: AI Chatbot ===")
    print("1. OpenAI GPT")
    print("2. Google Gemini")
    choice = input("Choose (1/2): ")

    if choice == "1":
        if not os.getenv("OPENAI_API_KEY"):
            print("⚠️  Set OPENAI_API_KEY environment variable first!")
        else:
            openai_chatbot()
    elif choice == "2":
        if not os.getenv("GEMINI_API_KEY"):
            print("⚠️  Set GEMINI_API_KEY environment variable first!")
        else:
            gemini_chatbot()
    else:
        print("Set your API key in a .env file and run again.")
        print("Create .env file:")
        print("  OPENAI_API_KEY=your_key_here")
        print("  GEMINI_API_KEY=your_key_here")
