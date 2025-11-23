# 🗂 Python File Manager (CLI)

A simple command-line file manager built using Python and `pathlib`.  
It lets you create, read, update, and delete files without typing full filenames.  
Files are listed with index numbers for quick selection.

---

## 🚀 Features

- 🔍 List files recursively from the current directory  
- 📄 Create files with custom content  
- 📖 Read file contents  
- ✏ Update files  
  - Rename files  
  - Overwrite content  
  - Append content  
- 🗑 Delete files by selecting them by index  
- 🚫 Built-in validation for invalid input and missing files

---

## 📂 Project Structure

```
python-file-manager-cli/
├── file_manager.py   # Main CLI program
└── README.md         # Documentation
```

---

## 🛠 Tech Used

| Tool | Purpose |
|------|---------|
| `pathlib` | Path handling & traversal |
| `os` | File deletion |
| Python 3.x | No external libraries required |

---

## ▶ How to Run

```bash
python file_manager.py
```

---

## 📌 Example Usage

Deleting a file by index:

```
Available files:
1. notes/todo.txt
2. logs/debug.log
3. output/report.csv

Enter file number to delete: 2
Are you sure you want to delete 'logs/debug.log'? (y/N): y

FILE REMOVED SUCCESSFULLY
```

---

## 🔮 Future Improvements

| Feature | Why |
|---------|-----|
| Folder operations | Move/copy directories |
| GUI version (Tkinter / Streamlit) | More user-friendly interface |
| Search filter | Useful for long file lists |
| Bulk operations | Productivity boost |

---

## ⚠ Notes

- This tool performs actual file operations — deletions are *permanent*  
- Recommended to test inside a temporary directory before real use

---

### 📍 Repo Path

Ensure the project exists at:

```
/python/python-file-manager-cli/
```

Example GitHub link:

```
https://github.com/anisahmed01/python/tree/main/python-file-manager-cli
```

---
