# 🔐 Password-Cracker (Advanced Hash Cracker v5.0)

A simple but powerful **multi-threaded password cracking tool** built using Python.
This tool is designed for **educational purposes and security auditing** (especially for university projects like APU).

---

## 🚀 Features

* 🔓 Supports multiple hash types:

  * MD5
  * SHA1
  * SHA256
  * SHA512

* ⚡ Multi-threaded cracking (faster performance)

* 📊 Real-time progress display

* 💾 Auto-save cracked results into `results.txt`

* 🧠 Smart test wordlist generator (for demo/testing)

* 🖥️ Interactive CLI interface (easy to use)

---

## 📁 Project Structure

```
Password-Cracker/
│── Passwordcracker.py   # Main program
│── README.md            # Documentation
│── results.txt          # Auto-generated output file
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/tanmay1802-art/Password-Cracker.git
cd Password-Cracker
```

### 2. Install Python (if not installed)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

## ▶️ How to Run

```bash
python3 Passwordcracker.py
```

---

## 🧪 Example Usage

* Enter the hash you want to crack
* Select hash type (MD5/SHA1/SHA256/SHA512)
* Provide a wordlist OR use built-in test wordlist

Example:

```
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
Select algorithm: md5
Wordlist: rockyou.txt
```

Output:

```
[✓] Password Found: password
Saved in results.txt
```

---

## 📌 Output

All cracked passwords are automatically saved in:

```
results.txt
```

Format:

```
[Date Time] | Hash | Password | Algorithm | Time Taken
```

---

## ⚠️ Disclaimer

This tool is created for:

* ✅ Educational use
* ✅ Security testing (own systems only)
* ✅ Learning cybersecurity concepts

❌ Do NOT use this tool for illegal activities or unauthorized access.
The developer is not responsible for misuse.

---

## 🎓 Project Purpose

This project was built as part of **Cybersecurity / Penetration Testing practice at APU**.
It demonstrates:

* Hashing & cryptography basics
* Password attack techniques (dictionary attack)
* Multi-threading in Python
* Real-world security audit concepts

---

## 🧠 Future Improvements

* Add GUI version (Tkinter)
* Add brute-force mode
* Add rainbow table support
* Export results in CSV format
* Add more hashing algorithms

---

## 👨‍💻 Author

**Tanmay Sarkar Emon**
Cybersecurity Student | Ethical Hacking Enthusiast

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!

---
