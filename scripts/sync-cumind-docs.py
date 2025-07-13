#!/usr/bin/env python3
import os
import json
import requests
import yaml
import shutil
from pathlib import Path

CUMIND_REPO = "carletonai/CuMind"
CUMIND_BRANCH = "dev"
CUMIND_DOCS_PATH = "docs"
LOCAL_CUMIND_DOCS_PATH = "docs/CuMind"
GITHUB_API_BASE = "https://api.github.com"

def get_github_token():
    """Get GitHub token from environment or use default (public access)"""
    return os.environ.get('GITHUB_TOKEN', '')

def fetch_docs_from_github():
    """Fetch documentation files from CuMind repository"""
    headers = {}
    token = get_github_token()
    if token:
        headers['Authorization'] = f'token {token}'
    
    # Get the tree for the docs directory
    tree_url = f"{GITHUB_API_BASE}/repos/{CUMIND_REPO}/contents/{CUMIND_DOCS_PATH}?ref={CUMIND_BRANCH}"
    
    try:
        response = requests.get(tree_url, headers=headers)
        response.raise_for_status()
        
        files = response.json()
        md_files = [f for f in files if f['name'].endswith('.md')]
        
        return md_files
    except requests.exceptions.RequestException as e:
        print(f"Error fetching docs list: {e}")
        return []

def download_file(file_info, headers):
    """Download a single file from GitHub"""
    try:
        response = requests.get(file_info['download_url'], headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {file_info['name']}: {e}")
        return None

def ensure_cumind_docs_dir():
    """Ensure the CuMind docs directory exists"""
    Path(LOCAL_CUMIND_DOCS_PATH).mkdir(parents=True, exist_ok=True)

def clean_cumind_docs_dir():
    """Clean existing CuMind docs before syncing"""
    if os.path.exists(LOCAL_CUMIND_DOCS_PATH):
        shutil.rmtree(LOCAL_CUMIND_DOCS_PATH)
    ensure_cumind_docs_dir()

def save_doc_file(filename, content):
    """Save documentation file locally"""
    filepath = os.path.join(LOCAL_CUMIND_DOCS_PATH, filename)
    
    # Add frontmatter if not present
    if not content.startswith('---'):
        title = filename.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
        content = f"""---
title: {title}
---

{content}"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved: {filename}")

def update_mkdocs_nav():
    """Update mkdocs.yml to include CuMind section in navigation"""
    mkdocs_path = 'mkdocs.yml'
    
    with open(mkdocs_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Get list of synced files
    cumind_files = sorted([f for f in os.listdir(LOCAL_CUMIND_DOCS_PATH) if f.endswith('.md')])
    
    if not cumind_files:
        print("No CuMind documentation files found to add to navigation")
        return
    
    # Create CuMind navigation section
    cumind_nav = []
    for file in cumind_files:
        title = file.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
        path = f"CuMind/{file}"
        cumind_nav.append({title: path})
    
    # Initialize nav if it doesn't exist
    if 'nav' not in config:
        config['nav'] = []
    
    # Remove existing CuMind section if it exists
    config['nav'] = [item for item in config['nav'] if not (isinstance(item, dict) and 'CuMind' in item)]
    
    # Add CuMind section
    config['nav'].append({'CuMind': cumind_nav})
    
    # Write updated config
    with open(mkdocs_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    print("Updated mkdocs.yml with CuMind navigation")

def main():
    """Main sync function"""
    print("Starting CuMind documentation sync...")
    
    # Clean and prepare directory
    clean_cumind_docs_dir()
    
    # Fetch docs list
    headers = {}
    token = get_github_token()
    if token:
        headers['Authorization'] = f'token {token}'
    
    md_files = fetch_docs_from_github()
    
    if not md_files:
        print("No markdown files found in CuMind docs")
        return
    
    print(f"Found {len(md_files)} markdown files to sync")
    
    # Download and save each file
    for file_info in md_files:
        content = download_file(file_info, headers)
        if content:
            save_doc_file(file_info['name'], content)
    
    # Update navigation
    update_mkdocs_nav()
    
    print("CuMind documentation sync completed!")

if __name__ == "__main__":
    main()