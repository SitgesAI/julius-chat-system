import json
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

def write_message_v3(message, priority=Priority.NORMAL, tags=None):
    if tags is None:
        tags = []
        
    msg = {
        "sender": "Julius1",
        "message": message,
        "timestamp": datetime.now().timestamp(),
        "readable_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "priority": priority.value if isinstance(priority, Priority) else priority,
        "tags": tags
    }
    
    try:
        # Llegim missatges existents
        with open('julius_chat.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = []
    
    # Afegim el nou missatge
    messages.append(msg)
    
    # Guardem tots els missatges
    with open('julius_chat.json', 'w') as f:
        json.dump(messages, f, indent=2)
        
    return msg