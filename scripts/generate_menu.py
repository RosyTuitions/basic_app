#!/usr/bin/env python3
"""
Generate menu from markdown posts.

This script scans the posts directory and generates a menu
of available cheatsheets in JSON and text formats.
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Optional


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


def extract_title_from_markdown(file_path: Path) -> str:
    """
    Extract title from markdown file.
    
    Attempts to read the first H1 header from the file,
    falls back to filename-based title if not found.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        Title string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
    except (IOError, OSError) as e:
        logger.warning(f"Could not read {file_path}: {e}")
    
    # Fallback to filename-based title
    filename = file_path.stem
    return filename.replace("cheatsheet_", "").replace("_", " ").title()


def write_json_menu(items: list, output_path: Path) -> bool:
    """
    Write menu items to JSON file.
    
    Args:
        items: List of menu item dictionaries
        output_path: Path to output directory
        
    Returns:
        True if successful, False otherwise
    """
    try:
        menu_json = output_path / "menu.json"
        with open(menu_json, "w", encoding='utf-8') as f:
            json.dump(items, f, indent=2)
        logger.info(f"Menu generated: {menu_json}")
        return True
    except (IOError, OSError) as e:
        logger.error(f"Error writing JSON menu: {e}")
        return False


def write_text_menu(items: list, output_path: Path) -> bool:
    """
    Write menu items to plain text file.
    
    Args:
        items: List of menu item dictionaries
        output_path: Path to output directory
        
    Returns:
        True if successful, False otherwise
    """
    try:
        menu_txt = output_path / "menu.txt"
        with open(menu_txt, "w", encoding='utf-8') as f:
            f.write("Available Cheatsheets\n")
            f.write("=" * 30 + "\n\n")
            for i, item in enumerate(items, 1):
                f.write(f"{i}. {item['title']}\n")
        logger.info(f"Text menu generated: {menu_txt}")
        return True
    except (IOError, OSError) as e:
        logger.error(f"Error writing text menu: {e}")
        return False


def generate_menu(posts_dir: str = "posts", output_dir: str = "artifacts") -> bool:
    """
    Generate menu from markdown files in posts directory.
    
    Args:
        posts_dir: Directory containing markdown files
        output_dir: Directory to output generated menu files
        
    Returns:
        True if successful, False otherwise
    """
    posts_path = Path(posts_dir)
    output_path = Path(output_dir)
    menu_items = []
    
    # Validate posts directory
    if not posts_path.exists():
        logger.error(f"{posts_path} directory not found.")
        return False
    
    if not posts_path.is_dir():
        logger.error(f"{posts_path} is not a directory.")
        return False
    
    # Create output directory if it doesn't exist
    try:
        output_path.mkdir(parents=True, exist_ok=True)
    except (IOError, OSError) as e:
        logger.error(f"Error creating output directory: {e}")
        return False
    
    # Scan for markdown files
    md_files = sorted(posts_path.glob("*.md"))
    
    if not md_files:
        logger.warning(f"No markdown files found in {posts_path}")
    
    for md_file in md_files:
        try:
            title = extract_title_from_markdown(md_file)
            
            menu_items.append({
                "file": md_file.name,
                "title": title,
                "path": str(md_file)
            })
        except Exception as e:
            logger.warning(f"Error processing {md_file}: {e}")
            continue
    
    # Write both menu formats
    json_success = write_json_menu(menu_items, output_path)
    text_success = write_text_menu(menu_items, output_path)
    
    # Log summary
    logger.info(f"Found {len(menu_items)} items:")
    for item in menu_items:
        logger.info(f"  - {item['title']} ({item['file']})")
    
    return json_success and text_success


def main() -> int:
    """
    Main entry point with argument parsing.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    parser = argparse.ArgumentParser(
        description="Generate menu from markdown posts."
    )
    parser.add_argument(
        "posts_dir",
        nargs="?",
        default="posts",
        help="Directory containing markdown files (default: posts)"
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="artifacts",
        help="Directory to output generated menu files (default: artifacts)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress informational logging"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging"
    )
    
    args = parser.parse_args()
    
    # Adjust logging level based on flags
    if args.quiet:
        logger.setLevel(logging.ERROR)
    elif args.verbose:
        logger.setLevel(logging.DEBUG)
    
    success = generate_menu(args.posts_dir, args.output_dir)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
