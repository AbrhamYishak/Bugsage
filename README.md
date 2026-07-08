```ascii
██████╗ ██╗   ██╗ ██████╗ ███████╗ █████╗  ██████╗ ███████╗
██╔══██╗██║   ██║██╔════╝ ██╔════╝██╔══██╗██╔════╝ ██╔════╝
██████╔╝██║   ██║██║  ███╗███████╗███████║██║  ███╗█████╗  
██╔══██╗██║   ██║██║   ██║╚════██║██╔══██║██║   ██║██╔══╝  
██████╔╝╚██████╔╝╚██████╔╝███████║██║  ██║╚██████╔╝███████╗
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```
> AI-powered CLI that explains programming errors using local caching, community knowledge, web search, and AI fallback.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

Bugsage is a command-line debugging assistant that helps developers understand programming errors instantly. Instead of repeatedly searching the web or sending every error to an AI model, Bugsage first checks a local cache and a community knowledge base before falling back to AI.

---

## ✨ Features

- ⚡ Instant lookup from a local SQLite cache
- 🌍 Search a community-maintained error database
- 🤖 AI-powered explanations when no existing solution is found
- 💾 Save useful explanations locally for future use
- 📈 Community upvoting for high-quality solutions
- 🔍 Search and filter previously encountered errors
- 🖥️ Lightweight command-line interface

---

## 🚀 How It Works

```text
                Programming Error
                        │
                        ▼
             Local SQLite Cache
                │          │
            Found?       Not Found
                │             │
                ▼             ▼
          Return Result   Community API
                                │
                          Found? │
                                ▼
                           Return Result
                                │
                                ▼
                          AI Explanation
                                │
                                ▼
                     Save (Optional)
```

---

## 📦 Installation

```bash
git clone https://github.com/AbrhamYishak/Bugsage.git

cd Bugsage

pip install -r requirements.txt
```

or

```bash
pip install bugsage
```

*(Coming soon on PyPI.)*

---

## 💻 Usage

Explain an error

```bash
bugsage "AttributeError: 'NoneType' object has no attribute 'split'"
```

Example output

```text
✓ Found in local cache

────────────────────────────────────

Error Type
AttributeError

Explanation
You attempted to call split() on a variable whose value is None.

Solution

• Check where the variable is assigned.
• Ensure it is not None before calling split().
• Use:

if value is not None:
    value.split()

Source
Community Database

────────────────────────────────────
```

---

## 🏗️ Architecture

```text
                 CLI
                  │
                  ▼
        Error Processing Layer
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 SQLite Cache   REST API    AI Service
      │           │           │
      └───────────┴───────────┘
                  │
                  ▼
          Formatted Response
```

---

## 🛠️ Tech Stack

### Backend

- Python
- Django REST Framework
- SQLite
- Requests

### AI

- OpenAI API *(configurable)*

### CLI

- Typer *(or Click if you use Click)*

---

## 📂 Project Structure

```text
bugsage/
│
├── cli/
├── analyzer/
├── web/
├── ai/
├── database/
├── templates/
├── tests/
│
├── main.py
└── requirements.txt
```

---

## 🌟 Roadmap

- [x] Local SQLite cache
- [x] AI fallback
- [x] Community API
- [x] Save explanations locally
- [ ] PyPI package
- [ ] VS Code extension
- [ ] Semantic search
- [ ] Offline mode
- [ ] Multi-language support
- [ ] Plugin system

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve Bugsage:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If Bugsage helps you debug faster, consider giving the repository a ⭐.

It helps other developers discover the project.
