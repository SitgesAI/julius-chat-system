import pytest
from src.communication import Priority, write_message_v3
import json
import os

def test_priority_enum():
    assert Priority.LOW.value == "low"
    assert Priority.NORMAL.value == "normal"
    assert Priority.HIGH.value == "high"

def test_write_message():
    # Test message
    test_msg = "Test message"
    result = write_message_v3(test_msg)
    
    # Check file exists
    assert os.path.exists('julius_chat.json')
    
    # Read file
    with open('julius_chat.json', 'r') as f:
        messages = json.load(f)
    
    # Check last message
    last_msg = messages[-1]
    assert last_msg['message'] == test_msg
    assert last_msg['sender'] == "Julius1"
    assert last_msg['priority'] == "normal"
    assert isinstance(last_msg['tags'], list)