from setuptools import setup, find_packages
import json
import os
import subprocess

def upload_to_pypi():
    with open('config.json') as f:
        config = json.load(f)
    token = config['TOKEN']

    # Prepare the command to upload all files in the dist/ directory
    command = [
        "twine", "upload",
        "--repository", "pypi",
        "--username", "__token__",
        "--password", token,
        "dist/*"
    ]

    try:
        # Use subprocess to call the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    upload_to_pypi()

