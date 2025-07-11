import requests, zipfile, io
from pathlib import Path


def download_repo(github_url, save_dir="data/downloaded_repos"):
    repo_owner_repo = "/".join(github_url.rstrip("/").split("/")[-2:])
    repo_name = github_url.rstrip("/").split("/")[-1]
    repo_path = Path(save_dir) / repo_name
    repo_path.mkdir(parents=True, exist_ok=True)

    for branch in ["main", "master"]:
        zip_url = (
            f"https://github.com/{repo_owner_repo}/archive/refs/heads/{branch}.zip"
        )
        response = requests.get(zip_url)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                zip_ref.extractall(repo_path)
            extracted_folder = next(repo_path.glob("*"))
            return str(extracted_folder)

    raise Exception("❌ Could not download repo. Branch 'main' or 'master' not found.")
