import json
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'hive_mind.json'))

def search_hive(query):
    try:
        if not os.path.exists(DB_PATH):
            return None

        with open(DB_PATH, 'r') as f:
            data = json.load(f)
            
        if not query:
            return None
            
        query_words = set(query.lower().split())
        
        for entry in data.get('fixes', []):
            issue_words = set(entry['issue'].lower().split())
            
            if not issue_words:
                continue
                
            common = query_words.intersection(issue_words)
            overlap_ratio = len(common) / len(issue_words)
            
            if overlap_ratio > 0.5:
                return entry['solution']
                
    except Exception as e:
        print(f"Hive Database Error: {e}")
        return None
        
    return None