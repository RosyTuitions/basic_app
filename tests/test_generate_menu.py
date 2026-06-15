import pytest
import json
import tempfile
from pathlib import Path
from scripts.generate_menu import (
    extract_title_from_markdown,
    write_json_menu,
    write_text_menu,
    generate_menu
)


class TestExtractTitleFromMarkdown:
    """Tests for extract_title_from_markdown function"""
    
    def test_extract_title_with_h1_header(self, tmp_path):
        """Test extracting title from valid markdown with H1 header"""
        md_file = tmp_path / "test.md"
        md_file.write_text("# Physics Cheatsheet\n\nSome content")
        
        title = extract_title_from_markdown(md_file)
        assert title == "Physics Cheatsheet"
    
    def test_extract_title_with_multiple_headers(self, tmp_path):
        """Test that only first H1 is extracted"""
        md_file = tmp_path / "test.md"
        md_file.write_text("# First Title\n# Second Title\n")
        
        title = extract_title_from_markdown(md_file)
        assert title == "First Title"
    
    def test_extract_title_fallback_from_filename(self, tmp_path):
        """Test fallback to filename when H1 not found"""
        md_file = tmp_path / "cheatsheet_chemistry_101.md"
        md_file.write_text("No H1 header here\nJust content")
        
        title = extract_title_from_markdown(md_file)
        assert title == "Chemistry 101"
    
    def test_extract_title_from_nonexistent_file(self, tmp_path):
        """Test handling of nonexistent file"""
        md_file = tmp_path / "nonexistent.md"
        
        title = extract_title_from_markdown(md_file)
        assert title == "Nonexistent"
    
    def test_extract_title_with_empty_file(self, tmp_path):
        """Test handling of empty markdown file"""
        md_file = tmp_path / "cheatsheet_biology.md"
        md_file.write_text("")
        
        title = extract_title_from_markdown(md_file)
        assert title == "Biology"


class TestWriteJsonMenu:
    """Tests for write_json_menu function"""
    
    def test_write_json_menu_success(self, tmp_path):
        """Test successful JSON menu generation"""
        items = [
            {"file": "physics.md", "title": "Physics", "path": "posts/physics.md"},
            {"file": "chemistry.md", "title": "Chemistry", "path": "posts/chemistry.md"}
        ]
        
        result = write_json_menu(items, tmp_path)
        
        assert result is True
        menu_file = tmp_path / "menu.json"
        assert menu_file.exists()
        
        # Verify content
        with open(menu_file) as f:
            data = json.load(f)
        assert len(data) == 2
        assert data[0]["title"] == "Physics"
    
    def test_write_json_menu_empty_list(self, tmp_path):
        """Test JSON menu with empty items list"""
        items = []
        
        result = write_json_menu(items, tmp_path)
        
        assert result is True
        menu_file = tmp_path / "menu.json"
        assert menu_file.exists()
        
        with open(menu_file) as f:
            data = json.load(f)
        assert data == []


class TestWriteTextMenu:
    """Tests for write_text_menu function"""
    
    def test_write_text_menu_success(self, tmp_path):
        """Test successful text menu generation"""
        items = [
            {"file": "physics.md", "title": "Physics", "path": "posts/physics.md"},
            {"file": "chemistry.md", "title": "Chemistry", "path": "posts/chemistry.md"}
        ]
        
        result = write_text_menu(items, tmp_path)
        
        assert result is True
        menu_file = tmp_path / "menu.txt"
        assert menu_file.exists()
        
        # Verify content
        content = menu_file.read_text()
        assert "Available Cheatsheets" in content
        assert "1. Physics" in content
        assert "2. Chemistry" in content
    
    def test_write_text_menu_empty_list(self, tmp_path):
        """Test text menu with empty items list"""
        items = []
        
        result = write_text_menu(items, tmp_path)
        
        assert result is True
        menu_file = tmp_path / "menu.txt"
        assert menu_file.exists()
        
        content = menu_file.read_text()
        assert "Available Cheatsheets" in content


class TestGenerateMenu:
    """Tests for main generate_menu function"""
    
    def test_generate_menu_with_valid_posts(self, tmp_path):
        """Test menu generation with valid markdown files"""
        # Create posts directory
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        
        # Create output directory
        output_dir = tmp_path / "artifacts"
        
        # Create markdown files
        (posts_dir / "cheatsheet_physics.md").write_text("# Physics\n\nContent")
        (posts_dir / "cheatsheet_chemistry.md").write_text("# Chemistry\n\nContent")
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        assert result is True
        assert (output_dir / "menu.json").exists()
        assert (output_dir / "menu.txt").exists()
    
    def test_generate_menu_nonexistent_posts_dir(self, tmp_path):
        """Test menu generation when posts directory doesn't exist"""
        posts_dir = tmp_path / "nonexistent"
        output_dir = tmp_path / "artifacts"
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        assert result is False
    
    def test_generate_menu_posts_is_file(self, tmp_path):
        """Test menu generation when posts path is a file, not directory"""
        posts_file = tmp_path / "posts"
        posts_file.write_text("I am a file")
        output_dir = tmp_path / "artifacts"
        
        result = generate_menu(str(posts_file), str(output_dir))
        
        assert result is False
    
    def test_generate_menu_empty_posts_dir(self, tmp_path):
        """Test menu generation with empty posts directory"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        output_dir = tmp_path / "artifacts"
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        # Should succeed but with empty menu
        assert result is True
        menu_json = output_dir / "menu.json"
        with open(menu_json) as f:
            data = json.load(f)
        assert data == []
    
    def test_generate_menu_with_non_markdown_files(self, tmp_path):
        """Test that only .md files are processed"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        output_dir = tmp_path / "artifacts"
        
        # Create mixed files
        (posts_dir / "readme.txt").write_text("Not markdown")
        (posts_dir / "physics.md").write_text("# Physics\n\nContent")
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        assert result is True
        menu_json = output_dir / "menu.json"
        with open(menu_json) as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]["title"] == "Physics"


class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""
    
    def test_generate_menu_with_special_characters(self, tmp_path):
        """Test handling of special characters in markdown"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        output_dir = tmp_path / "artifacts"
        
        (posts_dir / "special.md").write_text("# Physics & Chemistry (2024)\n\nContent")
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        assert result is True
        menu_json = output_dir / "menu.json"
        with open(menu_json) as f:
            data = json.load(f)
        assert data[0]["title"] == "Physics & Chemistry (2024)"
    
    def test_generate_menu_with_unicode_characters(self, tmp_path):
        """Test handling of unicode characters"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        output_dir = tmp_path / "artifacts"
        
        (posts_dir / "unicode.md").write_text("# उच्च भौतिकी\n\nContent")
        
        result = generate_menu(str(posts_dir), str(output_dir))
        
        assert result is True
        menu_json = output_dir / "menu.json"
        with open(menu_json) as f:
            data = json.load(f)
        assert data[0]["title"] == "उच्च भौतिकी"
    
    def test_extract_title_with_h1_and_whitespace(self, tmp_path):
        """Test H1 extraction with extra whitespace"""
        md_file = tmp_path / "test.md"
        md_file.write_text("#   Physics   \n\nContent")
        
        title = extract_title_from_markdown(md_file)
        assert title == "Physics"
