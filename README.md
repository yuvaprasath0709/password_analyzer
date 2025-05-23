# 🔐 Password Strength Analyzer 

**Evaluate Password Strength & Enhance Security Practices**

[](https://www.python.org/)
[](https://en.wikipedia.org/wiki/Password_strength)
[](https://www.google.com/search?q=LICENSE)
[](https://www.google.com/search?q=https://github.com/codespaces/new%3Frepo%3DYOUR_GITHUB_USERNAME/YOUR_REPO_NAME%26devcontainer_path%3D.devcontainer%252Fdevcontainer.json)
[](https://www.google.com/search?q=https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME)
[](https://www.google.com/search?q=https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/star)

-----

## 🌟 Project Overview

The **Password Strength Analyzer** is a practical cybersecurity utility designed to assess the robustness of passwords, identify common weaknesses, and provide actionable recommendations for creating more secure credentials. This tool helps users understand the vulnerabilities in their chosen passwords and promotes best practices for digital security.

-----

## ✨ Key Features

  * **📊 Detailed Scoring System:** Evaluates password strength on a clear 0-10 scale, offering an intuitive understanding of security levels.
  * **🔍 Comprehensive Weakness Detection:**
      * **Length Analysis:** Assesses adherence to recommended length standards.
      * **Complexity Check:** Verifies the inclusion of diverse character types (lowercase, uppercase, numbers, special characters).
      * **Common Password Blacklist:** Identifies highly prevalent and easily guessable passwords.
      * **Pattern/Repetition Detection:** Flags simple patterns or repeated characters that weaken a password.
  * **🚀 Enhanced User Experience (UX):**
      * **Clear & Colorized Feedback:** Provides immediate, color-coded visual cues for strength ratings and feedback (supports ANSI escape codes in compatible terminals).
      * **Intelligent Recommendations:** Offers specific, actionable advice to improve password strength based on detected weaknesses.
  * **💬 Interactive Mode:** Allows for convenient, real-time password analysis via a command-line prompt.
  * **📂 Batch Analysis (Optional):** Supports analyzing multiple passwords from a text file, ideal for educational auditing purposes.
  * **📝 Professional Output:** Includes a clear banner, developer credits, and an ethical use note.

-----

## 🛠️ Technologies Used

  * **Python 3:** The core programming language.
  * **Standard Python Libraries:** Utilizes `re` (regular expressions) for pattern matching, `string` for character sets, and `sys`/`time` for system interactions and timestamps.
      * *Note: This tool does not require any external `pip` installations; it relies solely on standard Python libraries.*

-----

## 🚀 Getting Started

This project is configured to run seamlessly with **GitHub Codespaces**, providing a zero-setup, ready-to-use development environment directly in your browser.

### 🖥️ Run Locally 

If you prefer to run this project on your local machine:

1.  **Prerequisites:** Ensure you have [Python 3](https://www.python.org/downloads/) installed.

## 📝 Usage

The tool offers both an **Interactive Mode** and a **Command-Line Mode** for flexible analysis.

### Interactive Mode 💬

Run the script without any arguments for a guided experience:

```bash
python password_analyzer.py
```

The tool will prompt you to enter passwords one by one for analysis. Type `q` to quit.

### Command-Line Mode 🚀

Execute operations directly by providing a file path for batch analysis:

  * **Batch Analysis (from file):**
    Create a text file (e.g., `passwords.txt`) with one password per line:
    ```
    password123
    StrongPass!2024
    mySecretKey!!
    ```
    Then, run the tool:
    ```bash
    python password_analyzer.py passwords.txt
    ```
    *The tool will analyze each password in the file and print its strength report.*

-----

## 🧠 How It Works

The `score_password` function is the core of the analyzer. It applies a scoring rubric based on several criteria:

1.  **Length:** Points are awarded for exceeding certain length thresholds (e.g., 8, 12, 16+ characters).
2.  **Character Diversity:** Points are awarded for the inclusion of lowercase letters, uppercase letters, numbers, and special characters.
3.  **Common Password Check:** The password is compared against a blacklist of frequently used and easily guessed passwords. If a match is found, the score is heavily penalized. It also checks for common words *within* the password.
4.  **Pattern/Repetition Detection:** Regular expressions are used to identify simple, easily predictable patterns like consecutive repeating characters (e.g., `aaaa`) or repeating character sequences.

The final score is then translated into an intuitive strength rating (Weak, Moderate, Strong, Very Strong) with corresponding color indicators.

-----

## 💡 Future Enhancements

We are continuously looking to improve the tool's security, usability, and features:

  * **🌐 Real-World Breach Checks:** Integrate with APIs like HaveIBeenPwned to check if a password has appeared in known data breaches.
  * **🖥️ Graphical User Interface (GUI):** Develop a user-friendly GUI (e.g., using Tkinter) to make the tool more accessible.
  * **🔢 Password Generation:** Add functionality to generate strong, random passwords based on user-defined criteria.
  * **📚 Expand Dictionary:** Incorporate a larger dictionary or common phrase list for more robust common password detection.

-----

## 🔒 Security Considerations

  * **Ethical Use:** This tool is intended solely for educational purposes and ethical cybersecurity research. Misuse of this tool for unauthorized or malicious activities is strictly prohibited.
  * **No Password Storage:** This tool analyzes passwords in real-time and does not store them. However, be cautious when typing sensitive passwords into any analysis tool, especially if the environment is not fully trusted.

## 🧑‍💻 Author

**Developed by Yuva Prasath**
