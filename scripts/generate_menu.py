#!/usr/bin/env python3
"""
Generate menu from markdown posts.

This script scans the posts directory and generates a menu
of available cheatsheets in JSON and text formats.
"""

import os
import sys
import json
from pathlib import Path


def generate_menu(posts_dir="posts", output_dir="artifacts"):
    """
    Generate menu from markdown files in posts directory.
    
    Args:
        posts_dir: Directory containing markdown files
        output_dir: Directory to output generated menu files
    """
    posts_path = Path(posts_dir)
    output_path = Path(output_dir)
    menu_items = []
    
    if not posts_path.exists():
        print(f"Error: {posts_path} directory not found.")
        return False
    
    # Create output directory if it doesn't exist
    output_path.mkdir(exist_ok=True)
    
    # Scan for markdown files
    for md_file in sorted(posts_path.glob("*.md")):
        filename = md_file.stem
        title = filename.replace("cheatsheet_", "").replace("_", " ").title()
        
        menu_items.append({
            "file": md_file.name,
            "title": title,
            "path": str(md_file)
        })
    
    # Write menu to JSON file
    menu_json = output_path / "menu.json"
    with open(menu_json, "w") as f:
        json.dump(menu_items, f, indent=2)
    
    print(f"✓ Menu generated: {menu_json}")
    print(f"✓ Found {len(menu_items)} items:")
    for item in menu_items:
        print(f"  - {item['title']} ({item['file']})")
    
    # Also generate a simple text menu
    menu_txt = output_path / "menu.txt"
    with open(menu_txt, "w") as f:
        f.write("Available Cheatsheets\n")
        f.write("=" * 30 + "\n\n")
        for i, item in enumerate(menu_items, 1):
            f.write(f"{i}. {item['title']}\n")
    
    print(f"✓ Text menu generated: {menu_txt}")
    return True


if __name__ == "__main__":
    # Get arguments from command line
    posts_dir = sys.argv[1] if len(sys.argv) > 1 else "posts"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "artifacts"
    
    success = generate_menu(posts_dir, output_dir)
    sys.exit(0 if success else 1)
