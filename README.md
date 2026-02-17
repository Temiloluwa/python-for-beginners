# Python for Beginners: Data Scraping & Analysis

Welcome to the *Python Through Data Scraping* course! Over the next 12 weeks, you will learn Python by doing real-world data projects. We start with simple scripts and end with a full-fledged data pipeline enriched by AI.

## 🚀 Getting Started

To keep your computer organized and successful, we use **Virtual Environments**. This ensures our project's tools don't interfere with other projects on your machine.

### 1. Set Up Your Environment

First, open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and navigate to this folder.

#### Create a Virtual Environment

Run this command to create a new environment named `venv`:

```bash
# Mac/Linux
python3 -m venv venv

# Windows
python -m venv venv
```

#### Activate the Environment

You need to "turn on" the environment every time you work on this project.

```bash
# Mac/Linux
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

*(You'll know it's working if you see `(venv)` appear at the start of your command line!)*

### 2. Install Dependencies

With your environment activated, install the necessary libraries, including Jupyter Notebook:

```bash
pip install jupyter notebook requests pandas beautifulsoup4
```

### 3. Set Up Jupyter Kernel

This is a crucial step! We need to tell Jupyter to use our specific `venv` Python, not the global system Python.

```bash
python -m ipykernel install --user --name=python-for-beginners --display-name "Python (Beginners Course)"
```

---

## 🧠 Concept: Kernels vs. Environments

This confuses everyone at first, so let's clear it up:

-   **Environment (`venv`)**: This is the **Library building**. It contains all the books (packages like pandas, requests) that you have installed.
-   **Kernel**: This is the **Librarian**. It knows *which* library building to go to when you ask for a book.

When you open a Jupyter Notebook, you need to select the correct **Kernel** (Librarian) so that it looks in your **Environment** (Library) for the tools you need.

If you get a "Module Not Found" error, 99% of the time it's because you are using the wrong Kernel!

---
---

## 🏗️ Where to Run Your Code? (Important!)

We use **two different tools** in this course. It is important to use the right one for the job:

| File Type | Extension | Where to run it? | Why? |
| :--- | :--- | :--- | :--- |
| **Notebooks** | `.ipynb` | **Jupyter** | Great for learning, experimenting, and seeing charts. |
| **Scripts** | `.py` | **VS Code** | Great for building real tools, automation, and "production" code. |

**Rule of Thumb:**
- Weeks 1-7: Use **Jupyter** (browsers).
- Weeks 8-12: Use **VS Code** (terminal) to run your `.py` scripts.

---
---

## 🏃‍♂️ Running the Project

1.  **Activate your environment**:
    ```bash
    source venv/bin/activate  # Mac/Linux
    # or
    venv\Scripts\activate     # Windows
    ```

2.  **Start Jupyter**:
    ```bash
    jupyter notebook
    ```

3.  **Open a Notebook**:
    Navigate to `week01_python_intro_scraping/` and open a notebook.

4.  **Check your Kernel**:
    In the top right of the notebook, make sure it says **"Python (Beginners Course)"**. If not, click it and select that kernel from the list.

Happy Coding! 🐍

---

## 🐞 Debugging in VS Code

One of the best features of using VS Code is the built-in debugger. It allows you to pause your code, inspect variables, and step through it line by line.

### How to set it up:

1.  Click the **Run and Debug** icon on the left sidebar (looks like a bug with a play button).
2.  Click **"create a launch.json file"**.
3.  Select **"Python File"** from the list.
4.  This creates a `.vscode/launch.json` file. You can close it.

### How to debug:

1.  Open any `.py` script.
2.  Click to the left of a line number to set a **Red Dot (Breakpoint)**. This tells Python to "stop here".
3.  Press **F5** (or click the Green Play button in the Debug sidebar).
4.  Your code will run and pause at the red dot. You can now hover over variables to see what's inside them!

📺 **[Click here to watch a YouTube tutorial on debugging Python in VS Code](https://www.youtube.com/results?search_query=debugging+python+in+vscode)**
