import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_string():
    """Test compression of a string."""
    original = "Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))

def test_compress_bytes():
    """Test compression of bytes."""
    original = b"Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)

def test_decompress_data():
    """Test decompression of compressed data."""
    original = "Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original

def test_different_compression_levels():
    """Test compression with different levels."""
    original = "Hello, World!" * 100  # Repeat to have more data to compress
    
    # Compare compressed sizes at different levels
    comp_level_0 = compress_data(original, compression_level=0)
    comp_level_6 = compress_data(original, compression_level=6)
    comp_level_9 = compress_data(original, compression_level=9)
    
    assert len(comp_level_0) >= len(comp_level_6)
    assert len(comp_level_6) >= len(comp_level_9)

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels."""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)

def test_decompression_error():
    """Test error handling for invalid compressed data."""
    with pytest.raises(zlib.error):
        decompress_data(b"invalid compressed data")

def test_round_trip_large_data():
    """Test compression and decompression of large data."""
    original = "This is a large piece of text " * 1000
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original