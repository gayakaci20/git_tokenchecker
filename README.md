# **Token Checker**  

A tool to verify the validity of **GitHub** and **GitLab** API tokens. It also retrieves user information associated with the token and displays the results in **JSON** format.  

---

## **📥 Installation**  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-user/token-checker.git
cd token-checker
```  

### 2️⃣ Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```  

### 3️⃣ Install dependencies  
```bash
pip install requests
```  

---

## **🚀 Usage**  

### 🔍 Check a GitHub token  
```bash
python token_checker.py --github YOUR_GITHUB_TOKEN
```  

### 🔍 Check a GitLab token  
```bash
python token_checker.py --gitlab YOUR_GITLAB_TOKEN
```  

### 🔍 Check both tokens at the same time  
```bash
python token_checker.py --github YOUR_GITHUB_TOKEN --gitlab YOUR_GITLAB_TOKEN
```  

---

## **📊 Example Output**  

### ✅ Valid GitHub Token  
```json
{
    "valid": true,
    "platform": "GitHub",
    "username": "octocat",
    "id": 1234567,
    "name": "Octo Cat",
    "public_repos": 42,
    "scopes": ["repo", "user"]
}
```  

### ✅ Valid GitLab Token  
```json
{
    "valid": true,
    "platform": "GitLab",
    "username": "gitlab_user",
    "id": 7654321,
    "name": "GitLab User",
    "email": "user@example.com"
}
```  
# git_tokenchecker
