import requests
import argparse
import json

def check_github_token(token):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    
    response = requests.get(url, headers=headers)
    scope = response.headers.get("X-OAuth-Scopes", "No scopes found")
    
    if response.status_code == 200:
        user_data = response.json()
        return {
            "valid": True,
            "platform": "GitHub",
            "username": user_data.get("login"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "public_repos": user_data.get("public_repos"),
            "scopes": scope.split(", ") if scope else []
        }
    else:
        return {"valid": False, "platform": "GitHub", "error": response.json().get("message", "Invalid token")}

def check_gitlab_token(token):
    url = "https://gitlab.com/api/v4/user"
    headers = {"PRIVATE-TOKEN": token}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        return {
            "valid": True,
            "platform": "GitLab",
            "username": user_data.get("username"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "email": user_data.get("email")
        }
    else:
        return {"valid": False, "platform": "GitLab", "error": response.json().get("message", "Invalid token")}

def main():
    parser = argparse.ArgumentParser(description="Check GitHub or GitLab API tokens.")
    parser.add_argument("--github", type=str, help="GitHub API token")
    parser.add_argument("--gitlab", type=str, help="GitLab API token")
    
    args = parser.parse_args()
    
    if args.github:
        result = check_github_token(args.github)
        print(json.dumps(result, indent=4))
    
    if args.gitlab:
        result = check_gitlab_token(args.gitlab)
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()