import re
import string
import sys
import time

# Common password blacklist
COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "123456789", "12345", "letmein", "football", "iloveyou",
    "admin", "welcome", "monkey", "login", "dragon"
}

# Password complexity check
def score_password(password):
    score = 0
    feedback = []

    length = len(password)

    # 1. Length
    if length >= 16:
        score += 3
        feedback.append("✅ Excellent length (16+ characters).")
    elif length >= 12:
        score += 2
        feedback.append("✅ Good length (12+ characters).")
    elif length >= 8:
        score += 1
        feedback.append("⚠️ Acceptable length (8+ characters).")
    else:
        feedback.append("❌ Too short. Use at least 8 characters.")

    # 2. Lowercase, Uppercase, Digits, Special
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add numbers.")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%^&*).")

    # 3. Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ Very weak – this is a common password.")
        score = 0

    elif any(common in password.lower() for common in COMMON_PASSWORDS):
        feedback.append("⚠️ Contains a common word. Risky.")
        score -= 1

    # 4. Pattern/Repetition Detection
    if re.fullmatch(r"(.)\1{3,}", password):
        feedback.append("❌ Repeated characters detected.")
        score -= 1

    if re.search(r"(.)\1\1", password):
        feedback.append("⚠️ Repeating patterns reduce strength.")
        score -= 1

    return max(score, 0), feedback

# Result interpretation
def get_rating(score):
    if score >= 9:
        return "🟢 Very Strong"
    elif score >= 7:
        return "🟡 Strong"
    elif score >= 5:
        return "🟠 Moderate"
    else:
        return "🔴 Weak"

# Color output (basic)
def colorize(text, color):
    colors = {
        "red": "\033[91m", "green": "\033[92m",
        "yellow": "\033[93m", "blue": "\033[94m",
        "bold": "\033[1m", "end": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"

# UI
def banner():
    print(colorize("=" * 66, "bold"))
    print(colorize("	PASSWORD STRENGTH ANALYZER", "blue"))
    print("	Developed by Yuva Prasath")
    print("	Date:", time.strftime("%Y-%m-%d"))
    print(colorize("=" * 66, "bold"))

# Main password analyzer
def analyze_password(password):
    score, tips = score_password(password)
    result = get_rating(score)

    print("\n🧪 Analysis Result")
    print("-" * 30)
    print(f"🔑 Password : {password}")
    print(f"📊 Score    : {score}/10")
    print(f"📈 Strength : {colorize(result, 'green' if score >= 7 else 'yellow' if score >= 5 else 'red')}\n")

    print("💡 Recommendations:")
    for tip in tips:
        print("  -", tip)

    print("\n✅ Tip: Use passphrases or combine unrelated words.")
    print("✅ Example: Rain!Forest42$Cat\n")

# Batch mode (optional enhancement)
def batch_analyze(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        print(f"\n📂 Analyzing passwords from: {file_path}\n")
        for pwd in lines:
            if pwd.strip():
                print(colorize("-" * 40, "yellow"))
                analyze_password(pwd.strip())
    except Exception as e:
        print(colorize(f"[✘] Failed to read file: {e}", "red"))

# CLI
def main():
    banner()

    if len(sys.argv) == 2 and sys.argv[1].endswith(".txt"):
        batch_analyze(sys.argv[1])
        return

    while True:
        pwd = input("🔑 Enter a password to analyze (or 'q' to quit): ").strip()
        if pwd.lower() == 'q':
            print(colorize("\n[✔] Exiting analyzer. Stay secure!\n", "green"))
            break
        analyze_password(pwd)

if __name__ == "__main__":
    main()
