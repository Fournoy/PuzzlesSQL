# PuzzlesSQL


PuzzlesSQL is a Python package designed to simplify and accelerate SQL Injection (SQLi) automation. The main goal is to provide pre-built functions that users can assemble like puzzle pieces to create custom scripts tailored to their needs. Currently, the package includes support for **time-based blind SQLi**, with plans to expand to other types of SQLi in the future.

---

## Table of Contents

- [About the Package](#about-the-package)
- [Installation](#installation)
- [Usage](#usage)
- [Functionalities](#functionalities)
- [Contact](#contact)

---

## About the Package

PuzzlesSQL is ideal for:

- **Home Labs:** Test and refine SQLi techniques in a controlled environment.
- **Capture The Flag (CTF) Challenges:** Use the package for competitions or challenges like those on **PortSwigger** and similar platforms.
- **Personal Learning:** Practice and understand SQLi automation by customizing scripts to match specific scenarios.

Currently, the package supports **time-based blind SQLi**, but additional SQLi techniques will be included in future updates. While primarily intended for educational purposes, the long-term goal is to refine the package for real-world applications, providing robust and reliable solutions for professionals.

---

## Installation

To get started, clone the repository and install the dependencies:

1. Clone the repository:

   ```bash
   git clone https://github.com/Fournoy/PuzzlesSQL.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PuzzlesSQL
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

This package provides a modular approach to SQLi automation. Each function is designed to handle a specific task, and users can combine these functions in the `main.py` file to create a custom script that suits their needs. They are other main file with pre-made programm for specifique type of SQL injection.

### Steps to Use:

1. **Edit:** Modify the main script to combine the provided functions in the desired sequence for your SQLi attack.
2. **Customize Parameters:** Adjust necessary parameters (e.g., target URLs, payloads) to fit your target or CTF challenge.
3. **Run Your Script:** Once assembled, execute the script and monitor its behavior.

> **Note:** The package is not plug-and-play; users are encouraged to understand the functions and assemble their scripts manually, as this is a puzzle-like approach for learning and flexibility.

---

## Functionalities

### Current Features:

- **Time-Based Blind SQLi:** Automate the process of extracting data using time delays to infer true/false conditions.

### Future Plans:

- Add support for other SQLi techniques, such as:
  - Boolean-based blind SQLi
  - Error-based SQLi
  - Union-based SQLi
  - Out-of-band SQLi

---

## Contact

For questions, feedback, or contributions, feel free to reach out:
- **Email:** [fournoyfr@protonmail.com](mailto\:fournoyfr@protonmail.com)

---


