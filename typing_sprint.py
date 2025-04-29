import random
import time

words = [
    "python", "developer", "challenge", "keyboard", "algorithm",
    "function", "variable", "condition", "exception", "iteration",
    "sprint", "performance", "debug", "compile", "syntax",
    "library", "object", "inheritance", "module", "runtime"
]

def typing_sprint():
    print("⌨️  Welcome to Typing Sprint!")
    print("You have 30 seconds to type as many words correctly as you can.")
    input("Press Enter to start...")
    
    score = 0
    start_time = time.time()
    end_time = start_time + 30

    while time.time() < end_time:
        word = random.choice(words)
        print(f"\nType: {word}")
        typed = input("Your input: ").strip()

        if typed == word:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print(f"\n⏱ Time's up! You scored {score} point(s).")

if __name__ == "__main__":
    typing_sprint()
