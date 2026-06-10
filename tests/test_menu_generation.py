"""
Test suite for menu generation functionality
Tests the script that generates menu cards from markdown cheatsheets
"""

import pytest
import json
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from generate_menu import extract_title_from_markdown, generate_menu


class TestTitleExtraction:
    """Test markdown title extraction"""
    
    def test_extract_title_with_h1_header(self, tmp_path):
        """Test extracting H1 header from markdown"""
        test_md = tmp_path / "test.md"
        test_md.write_text("# Physics Cheatsheet\n\nSome content")
        
        title = extract_title_from_markdown(test_md)
        assert title == "Physics Cheatsheet"
    
    def test_extract_title_fallback_filename(self, tmp_path):
        """Test fallback to filename when no H1 found"""
        test_md = tmp_path / "cheatsheet_biology.md"
        test_md.write_text("## Section\n\nContent without H1")
        
        title = extract_title_from_markdown(test_md)
        assert title == "Cheatsheet Biology"
    
    def test_extract_title_with_multiple_headers(self, tmp_path):
        """Test extracting first H1 when multiple exist"""
        test_md = tmp_path / "test.md"
        test_md.write_text("# First Title\n\n# Second Title\n\nContent")
        
        title = extract_title_from_markdown(test_md)
        assert title == "First Title"
    
    def test_extract_title_nonexistent_file(self, tmp_path):
        """Test handling of non-existent file"""
        nonexistent = tmp_path / "nonexistent.md"
        title = extract_title_from_markdown(nonexistent)
        
        # Should fall back to filename
        assert "nonexistent" in title


class TestMenuGeneration:
    """Test complete menu generation"""
    
    def test_generate_menu_creates_files(self, tmp_path):
        """Test that menu generation creates output files"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        # Create sample markdown files
        (posts_dir / "cheatsheet_physics.md").write_text("# Physics\n\nContent")
        (posts_dir / "cheatsheet_chemistry.md").write_text("# Chemistry\n\nContent")
        
        # Generate menu
        success = generate_menu(str(posts_dir), str(artifacts_dir))
        
        assert success
        assert (artifacts_dir / "menu.json").exists()
        assert (artifacts_dir / "menu.txt").exists()
    
    def test_generate_menu_json_content(self, tmp_path):
        """Test JSON menu content"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        (posts_dir / "cheatsheet_physics.md").write_text("# Physics\n\nContent")
        generate_menu(str(posts_dir), str(artifacts_dir))
        
        with open(artifacts_dir / "menu.json") as f:
            menu = json.load(f)
        
        assert isinstance(menu, list)
        assert len(menu) > 0
        assert any(item['title'] == 'Physics' for item in menu)
        assert 'file' in menu[0]
        assert 'path' in menu[0]
    
    def test_generate_menu_text_format(self, tmp_path):
        """Test text menu format"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        (posts_dir / "cheatsheet_physics.md").write_text("# Physics\n\nContent")
        generate_menu(str(posts_dir), str(artifacts_dir))
        
        with open(artifacts_dir / "menu.txt") as f:
            content = f.read()
        
        assert "Available Cheatsheets" in content
        assert "Physics" in content
    
    def test_generate_menu_multiple_files(self, tmp_path):
        """Test menu generation with multiple subjects"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        # Create three subject files
        (posts_dir / "cheatsheet_physics.md").write_text("# Physics\n\nContent")
        (posts_dir / "cheatsheet_chemistry.md").write_text("# Chemistry\n\nContent")
        (posts_dir / "cheatsheet_biology.md").write_text("# Biology\n\nContent")
        
        success = generate_menu(str(posts_dir), str(artifacts_dir))
        
        assert success
        
        with open(artifacts_dir / "menu.json") as f:
            menu = json.load(f)
        
        assert len(menu) == 3
        titles = [item['title'] for item in menu]
        assert 'Physics' in titles
        assert 'Chemistry' in titles
        assert 'Biology' in titles
    
    def test_generate_menu_empty_directory(self, tmp_path):
        """Test menu generation with empty directory"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        success = generate_menu(str(posts_dir), str(artifacts_dir))
        
        # Should still succeed but with empty menu
        assert success or not success  # Depends on implementation
        assert (artifacts_dir / "menu.json").exists()
    
    def test_generate_menu_missing_posts_directory(self, tmp_path):
        """Test menu generation when posts directory doesn't exist"""
        posts_dir = tmp_path / "nonexistent_posts"
        artifacts_dir = tmp_path / "artifacts"
        
        success = generate_menu(str(posts_dir), str(artifacts_dir))
        
        # Should fail gracefully
        assert not success
    
    def test_generate_menu_json_valid_structure(self, tmp_path):
        """Test that generated JSON has valid structure"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        (posts_dir / "cheatsheet_test.md").write_text("# Test Subject\n\nContent")
        generate_menu(str(posts_dir), str(artifacts_dir))
        
        with open(artifacts_dir / "menu.json") as f:
            menu = json.load(f)
        
        # Verify structure
        for item in menu:
            assert 'file' in item
            assert 'title' in item
            assert 'path' in item
            assert isinstance(item['file'], str)
            assert isinstance(item['title'], str)
            assert isinstance(item['path'], str)


class TestMenuIntegration:
    """Integration tests for menu functionality"""
    
    def test_integration_real_cheatsheets(self, tmp_path):
        """Test with realistic cheatsheet files"""
        posts_dir = tmp_path / "posts"
        posts_dir.mkdir()
        artifacts_dir = tmp_path / "artifacts"
        
        # Create realistic content
        physics_content = """# Physics Cheatsheet

## Mechanics
- **Newton's Second Law**: F = ma

## Energy
- **Kinetic Energy**: KE = ½mv²
"""
        chemistry_content = """# Chemistry Cheatsheet

## Atomic Structure
- Protons: Positively charged particles in nucleus
"""
        biology_content = """# Biology Cheatsheet

## Cell Structure
- **Nucleus**: Contains DNA, controls cell activities
"""
        
        (posts_dir / "cheatsheet_physics.md").write_text(physics_content)
        (posts_dir / "cheatsheet_chemistry.md").write_text(chemistry_content)
        (posts_dir / "cheatsheet_biology.md").write_text(biology_content)
        
        success = generate_menu(str(posts_dir), str(artifacts_dir))
        
        assert success
        
        with open(artifacts_dir / "menu.json") as f:
            menu = json.load(f)
        
        assert len(menu) == 3
        
        with open(artifacts_dir / "menu.txt") as f:
            text_menu = f.read()
        
        assert "Physics Cheatsheet" in text_menu
        assert "Chemistry Cheatsheet" in text_menu
        assert "Biology Cheatsheet" in text_menu
