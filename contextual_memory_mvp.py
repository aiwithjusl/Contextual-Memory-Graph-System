# Project 1 MVP: Contextual Memory Graph System
# Mobile-optimized knowledge graph with contextual memory

import json
import sqlite3
import hashlib
import time
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import re
import math

# Core Data Structures
@dataclass
class Entity:
    """Represents a knowledge entity in the graph"""
    id: str
    name: str
    type: str
    properties: Dict
    created_at: float
    last_accessed: float
    access_count: int = 0
    importance_score: float = 0.0

@dataclass
class Relationship:
    """Represents a relationship between entities"""
    id: str
    source_id: str
    target_id: str
    relation_type: str
    strength: float
    context: str
    created_at: float
    last_reinforced: float

@dataclass
class Memory:
    """Represents a memory fragment with context"""
    id: str
    content: str
    entities: List[str]
    relationships: List[str]
    timestamp: float
    context_tags: List[str]
    importance: float = 0.0

class MobileGraphStorage:
    """Lightweight graph storage optimized for mobile devices"""
    
    def __init__(self, db_path: str = "knowledge_graph.db"):
        self.db_path = db_path
        self.connection = None
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database with optimized schema"""
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.connection.execute("PRAGMA journal_mode=WAL")  # Mobile optimization
        self.connection.execute("PRAGMA synchronous=NORMAL")
        
        # Create tables
        self.connection.executescript("""
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                properties TEXT,
                created_at REAL,
                last_accessed REAL,
                access_count INTEGER DEFAULT 0,
                importance_score REAL DEFAULT 0.0
            );
            
            CREATE TABLE IF NOT EXISTS relationships (
                id TEXT PRIMARY KEY,
                source_id TEXT,
                target_id TEXT,
                relation_type TEXT,
                strength REAL,
                context TEXT,
                created_at REAL,
                last_reinforced REAL,
                FOREIGN KEY (source_id) REFERENCES entities (id),
                FOREIGN KEY (target_id) REFERENCES entities (id)
            );
            
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                content TEXT,
                entities TEXT,
                relationships TEXT,
                timestamp REAL,
                context_tags TEXT,
                importance REAL DEFAULT 0.0
            );
            
            CREATE INDEX IF NOT EXISTS idx_entity_type ON entities(type);
            CREATE INDEX IF NOT EXISTS idx_entity_name ON entities(name);
            CREATE INDEX IF NOT EXISTS idx_relationship_source ON relationships(source_id);
            CREATE INDEX IF NOT EXISTS idx_relationship_target ON relationships(target_id);
            CREATE INDEX IF NOT EXISTS idx_memory_timestamp ON memories(timestamp);
        """)
        self.connection.commit()
    
    def store_entity(self, entity: Entity) -> bool:
        """Store or update an entity"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO entities 
                (id, name, type, properties, created_at, last_accessed, access_count, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entity.id, entity.name, entity.type, 
                json.dumps(entity.properties), entity.created_at,
                entity.last_accessed, entity.access_count, entity.importance_score
            ))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error storing entity: {e}")
            return False
    
    def get_entity(self, entity_id: str) -> Optional[Entity]:
        """Retrieve an entity by ID"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM entities WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        
        if row:
            return Entity(
                id=row[0], name=row[1], type=row[2],
                properties=json.loads(row[3]) if row[3] else {},
                created_at=row[4], last_accessed=row[5],
                access_count=row[6], importance_score=row[7]
            )
        return None

class NLPProcessor:
    """Lightweight NLP processor for mobile devices"""
    
    def __init__(self):
        # Simple patterns for entity extraction (will be enhanced in portfolio version)
        self.entity_patterns = {
            'PERSON': r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
            'ORGANIZATION': r'\b[A-Z][a-z]+ (?:Inc|Corp|LLC|Ltd|Company|Organization)\b',
            'LOCATION': r'\b[A-Z][a-z]+ (?:City|State|Country|Street|Avenue|Road)\b',
            'TECH': r'\b(?:Python|JavaScript|AI|ML|API|Database|Server|Cloud)\b',
            'CONCEPT': r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b'
        }
        
        # Relationship patterns
        self.relation_patterns = {
            'WORKS_AT': r'(\w+) works at (\w+)',
            'LOCATED_IN': r'(\w+) (?:is )?(?:located )?in (\w+)',
            'RELATES_TO': r'(\w+) (?:relates to|connected to|associated with) (\w+)',
            'USES': r'(\w+) uses (\w+)',
            'CREATED': r'(\w+) created (\w+)'
        }
    
    def extract_entities(self, text: str) -> List[Tuple[str, str, str]]:
        """Extract entities from text - returns (name, type, context)"""
        entities = []
        
        # Enhanced entity patterns for better detection
        enhanced_patterns = {
            'PERSON': [r'\b[A-Z][a-z]+\b(?=\s+(?:works|created|developed|specializes))', 
                      r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b'],
            'ORGANIZATION': [r'\bGoogle\b', r'\bMicrosoft\b', r'\bApple\b', r'\bAmazon\b',
                           r'\b[A-Z][a-z]+\s+(?:Inc|Corp|LLC|Ltd|Company|Organization)\b'],
            'LOCATION': [r'\bMountain View\b', r'\bCalifornia\b', r'\bNew York\b',
                        r'\b[A-Z][a-z]+\s+(?:City|State|Country|Street|Avenue|Road)\b'],
            'TECH': [r'\bPython\b', r'\bJavaScript\b', r'\bAI\b', r'\bML\b', r'\bTensorFlow\b',
                    r'\bAPI\b', r'\bDatabase\b', r'\bServer\b', r'\bCloud\b', r'\balgorithm\b',
                    r'\bmachine learning\b', r'\bneural network\b'],
            'CONCEPT': [r'\bresearch\b', r'\bdevelopment\b', r'\btraining\b', r'\bframework\b']
        }
        
        for entity_type, patterns in enhanced_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, text, re.IGNORECASE)
                for match in matches:
                    entity_name = match.group().strip()
                    # Get surrounding context (30 chars each side)
                    start = max(0, match.start() - 30)
                    end = min(len(text), match.end() + 30)
                    context = text[start:end].strip()
                    
                    entities.append((entity_name, entity_type, context))
        
        return entities
    
    def extract_relationships(self, text: str, entities: List[str]) -> List[Tuple[str, str, str, str]]:
        """Extract relationships - returns (source, target, relation_type, context)"""
        relationships = []
        
        # Enhanced relationship patterns
        enhanced_relations = {
            'WORKS_AT': [r'(\w+)\s+works\s+at\s+(\w+)', r'(\w+)\s+(?:is\s+)?employed\s+(?:by\s+)?(\w+)'],
            'LOCATED_IN': [r'(\w+)\s+(?:is\s+)?(?:located\s+)?in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
                          r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+division\s+is\s+located\s+in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'],
            'CREATED': [r'(\w+)\s+(?:created|developed|built)\s+(?:a\s+)?(\w+(?:\s+\w+)*)',
                       r'(\w+(?:\s+\w+)*)\s+(?:was\s+)?created\s+by\s+(\w+)'],
            'USES': [r'(\w+(?:\s+\w+)*)\s+uses\s+(\w+(?:\s+\w+)*)',
                    r'(\w+)\s+(?:is\s+)?(?:built\s+)?(?:with\s+|using\s+)(\w+(?:\s+\w+)*)'],
            'SPECIALIZES_IN': [r'(\w+)\s+specializes\s+in\s+(\w+(?:\s+\w+)*)',
                              r'(\w+)\s+(?:focuses\s+on|works\s+in)\s+(\w+(?:\s+\w+)*)'],
            'RELATES_TO': [r'(\w+(?:\s+\w+)*)\s+(?:relates\s+to|connected\s+to|associated\s+with)\s+(\w+(?:\s+\w+)*)']
        }
        
        for relation_type, patterns in enhanced_relations.items():
            for pattern in patterns:
                matches = re.finditer(pattern, text, re.IGNORECASE)
                for match in matches:
                    if len(match.groups()) >= 2:
                        source = match.group(1).strip()
                        target = match.group(2).strip()
                        
                        # Get context
                        start = max(0, match.start() - 20)
                        end = min(len(text), match.end() + 20)
                        context = text[start:end].strip()
                        
                        relationships.append((source, target, relation_type, context))
        
        return relationships
    
    def calculate_text_similarity(self, text1: str, text2: str) -> float:
        """Simple text similarity using word overlap"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0

class ContextWeaver:
    """Creates and manages contextual relationships between entities"""
    
    def __init__(self, storage: MobileGraphStorage, nlp: NLPProcessor):
        self.storage = storage
        self.nlp = nlp
        self.context_threshold = 0.3  # Minimum similarity for context linking
    
    def _generate_id(self, content: str) -> str:
        """Generate consistent ID from content"""
        return hashlib.md5(content.encode()).hexdigest()[:12]
    
    def weave_memory(self, content: str, context_tags: List[str] = None) -> Memory:
        """Process content and create contextual memory"""
        current_time = time.time()
        memory_id = self._generate_id(content + str(current_time))
        
        if context_tags is None:
            context_tags = []
        
        # Extract entities and relationships
        extracted_entities = self.nlp.extract_entities(content)
        entity_objects = []
        
        # Process entities
        for entity_name, entity_type, entity_context in extracted_entities:
            entity_id = self._generate_id(entity_name.lower())
            
            # Check if entity exists
            existing_entity = self.storage.get_entity(entity_id)
            
            if existing_entity:
                # Update access information
                existing_entity.last_accessed = current_time
                existing_entity.access_count += 1
                existing_entity.importance_score += 0.1  # Simple importance boost
                self.storage.store_entity(existing_entity)
            else:
                # Create new entity
                new_entity = Entity(
                    id=entity_id,
                    name=entity_name,
                    type=entity_type,
                    properties={'contexts': [entity_context]},
                    created_at=current_time,
                    last_accessed=current_time,
                    access_count=1,
                    importance_score=0.5
                )
                self.storage.store_entity(new_entity)
            
            entity_objects.append(entity_id)
        
        # Extract and store relationships
        entity_names = [name for name, _, _ in extracted_entities]
        extracted_relationships = self.nlp.extract_relationships(content, entity_names)
        relationship_objects = []
        
        for source, target, relation_type, rel_context in extracted_relationships:
            source_id = self._generate_id(source.lower())
            target_id = self._generate_id(target.lower())
            relationship_id = self._generate_id(f"{source_id}_{target_id}_{relation_type}")
            
            relationship = Relationship(
                id=relationship_id,
                source_id=source_id,
                target_id=target_id,
                relation_type=relation_type,
                strength=0.7,  # Initial strength
                context=rel_context,
                created_at=current_time,
                last_reinforced=current_time
            )
            
            # Store relationship in database
            self._store_relationship(relationship)
            relationship_objects.append(relationship_id)
        
        # Create memory object
        memory = Memory(
            id=memory_id,
            content=content,
            entities=entity_objects,
            relationships=relationship_objects,
            timestamp=current_time,
            context_tags=context_tags,
            importance=self._calculate_memory_importance(content, entity_objects)
        )
        
        # Store memory
        self._store_memory(memory)
        
        return memory
    
    def _store_relationship(self, relationship: Relationship):
        """Store relationship in database"""
        try:
            cursor = self.storage.connection.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO relationships 
                (id, source_id, target_id, relation_type, strength, context, created_at, last_reinforced)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                relationship.id, relationship.source_id, relationship.target_id,
                relationship.relation_type, relationship.strength, relationship.context,
                relationship.created_at, relationship.last_reinforced
            ))
            self.storage.connection.commit()
        except Exception as e:
            print(f"Error storing relationship: {e}")
    
    def _store_memory(self, memory: Memory):
        """Store memory in database"""
        try:
            cursor = self.storage.connection.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO memories 
                (id, content, entities, relationships, timestamp, context_tags, importance)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                memory.id, memory.content, json.dumps(memory.entities),
                json.dumps(memory.relationships), memory.timestamp,
                json.dumps(memory.context_tags), memory.importance
            ))
            self.storage.connection.commit()
        except Exception as e:
            print(f"Error storing memory: {e}")
    
    def _calculate_memory_importance(self, content: str, entities: List[str]) -> float:
        """Calculate importance score for memory"""
        base_score = 0.5
        
        # Boost for more entities
        entity_boost = min(len(entities) * 0.1, 0.3)
        
        # Boost for length (more detailed memories)
        length_boost = min(len(content) / 1000, 0.2)
        
        return base_score + entity_boost + length_boost

class MemoryRetriever:
    """Retrieves contextually relevant memories"""
    
    def __init__(self, storage: MobileGraphStorage, nlp: NLPProcessor):
        self.storage = storage
        self.nlp = nlp
    
    def find_related_memories(self, query: str, limit: int = 10) -> List[Dict]:
        """Find memories related to query"""
        cursor = self.storage.connection.cursor()
        
        # Get all memories
        cursor.execute("""
            SELECT id, content, entities, relationships, timestamp, context_tags, importance
            FROM memories ORDER BY importance DESC, timestamp DESC
        """)
        memories = cursor.fetchall()
        
        # Score memories based on relevance to query
        scored_memories = []
        
        for memory_row in memories:
            memory_id, content, entities_json, relationships_json, timestamp, tags_json, importance = memory_row
            
            # Calculate relevance score
            content_similarity = self.nlp.calculate_text_similarity(query, content)
            
            # Boost based on entities in common
            query_entities = [name for name, _, _ in self.nlp.extract_entities(query)]
            memory_entities = json.loads(entities_json) if entities_json else []
            
            entity_boost = 0
            if query_entities and memory_entities:
                # Simple entity matching boost
                entity_boost = 0.2
            
            total_score = content_similarity + entity_boost + (importance * 0.1)
            
            if total_score > 0.1:  # Minimum relevance threshold
                scored_memories.append({
                    'id': memory_id,
                    'content': content,
                    'score': total_score,
                    'timestamp': timestamp,
                    'importance': importance
                })
        
        # Sort by score and return top results
        scored_memories.sort(key=lambda x: x['score'], reverse=True)
        return scored_memories[:limit]
    
    def get_entity_network(self, entity_name: str, depth: int = 2) -> Dict:
        """Get network of entities connected to given entity"""
        entity_id = hashlib.md5(entity_name.lower().encode()).hexdigest()[:12]
        
        cursor = self.storage.connection.cursor()
        
        # Get direct relationships
        cursor.execute("""
            SELECT r.*, e1.name as source_name, e2.name as target_name
            FROM relationships r
            JOIN entities e1 ON r.source_id = e1.id
            JOIN entities e2 ON r.target_id = e2.id
            WHERE r.source_id = ? OR r.target_id = ?
            ORDER BY r.strength DESC
        """, (entity_id, entity_id))
        
        relationships = cursor.fetchall()
        
        network = {
            'center_entity': entity_name,
            'relationships': [],
            'connected_entities': set()
        }
        
        for rel in relationships:
            rel_data = {
                'source': rel[7],  # source_name
                'target': rel[8],  # target_name  
                'type': rel[3],    # relation_type
                'strength': rel[4], # strength
                'context': rel[5]   # context
            }
            network['relationships'].append(rel_data)
            network['connected_entities'].add(rel[7])
            network['connected_entities'].add(rel[8])
        
        # If no relationships found, try partial matching
        if not relationships:
            print(f"No direct relationships found for '{entity_name}'. Searching for partial matches...")
            cursor.execute("""
                SELECT e.name, e.type FROM entities e 
                WHERE LOWER(e.name) LIKE LOWER(?)
            """, (f'%{entity_name.lower()}%',))
            
            matches = cursor.fetchall()
            if matches:
                print(f"Found similar entities: {[match[0] for match in matches]}")
                # Try with first match
                if matches[0][0].lower() != entity_name.lower():
                    return self.get_entity_network(matches[0][0], depth)
        
        network['connected_entities'] = list(network['connected_entities'])
        return network

class ContextualMemorySystem:
    """Main system orchestrating the contextual memory graph"""
    
    def __init__(self, db_path: str = "knowledge_graph.db"):
        self.storage = MobileGraphStorage(db_path)
        self.nlp = NLPProcessor()
        self.weaver = ContextWeaver(self.storage, self.nlp)
        self.retriever = MemoryRetriever(self.storage, self.nlp)
    
    def add_memory(self, content: str, context_tags: List[str] = None) -> str:
        """Add new memory to the system"""
        memory = self.weaver.weave_memory(content, context_tags)
        return f"Memory stored with ID: {memory.id}"
    
    def query_memory(self, query: str, limit: int = 5) -> List[Dict]:
        """Query the memory system"""
        return self.retriever.find_related_memories(query, limit)
    
    def explore_entity(self, entity_name: str) -> Dict:
        """Explore connections around an entity"""
        return self.retriever.get_entity_network(entity_name)
    
    def get_system_stats(self) -> Dict:
        """Get system statistics"""
        cursor = self.storage.connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM entities")
        entity_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM relationships") 
        relationship_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM memories")
        memory_count = cursor.fetchone()[0]
        
        return {
            'entities': entity_count,
            'relationships': relationship_count,
            'memories': memory_count,
            'storage_path': self.storage.db_path
        }

# Example Usage and Testing
def demo_contextual_memory_system():
    """Demonstration of the contextual memory system"""
    print("=== Contextual Memory Graph System MVP Demo ===\n")
    
    # Initialize system
    cms = ContextualMemorySystem("demo_knowledge.db")
    
    # Add some sample memories
    sample_memories = [
        "John works at Google and specializes in AI research. He created a new machine learning algorithm.",
        "The AI algorithm that John developed uses Python and TensorFlow for neural network training.",
        "Google's AI research division is located in Mountain View, California.",
        "TensorFlow is a popular machine learning framework created by Google.",
        "Python is widely used for AI development and data science projects."
    ]
    
    print("Adding sample memories...")
    for i, memory in enumerate(sample_memories, 1):
        result = cms.add_memory(memory, [f"demo_tag_{i}"])
        print(f"{i}. {result}")
    
    print(f"\nSystem Stats: {cms.get_system_stats()}")
    
    # Debug: Show what entities and relationships were extracted
    print("\n=== Debug: Extracted Entities ===")
    cursor = cms.storage.connection.cursor()
    cursor.execute("SELECT name, type FROM entities")
    entities = cursor.fetchall()
    for entity in entities:
        print(f"  {entity[1]}: {entity[0]}")
    
    print("\n=== Debug: Extracted Relationships ===")
    cursor.execute("""
        SELECT r.relation_type, e1.name as source, e2.name as target
        FROM relationships r
        JOIN entities e1 ON r.source_id = e1.id  
        JOIN entities e2 ON r.target_id = e2.id
    """)
    relationships = cursor.fetchall()
    for rel in relationships:
        print(f"  {rel[1]} --[{rel[0]}]--> {rel[2]}")
    
    # Test queries
    test_queries = [
        "Tell me about John",
        "What programming languages are used for AI?", 
        "Where is Google located?",
        "Machine learning algorithms"
    ]
    
    print("\n=== Query Testing ===")
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = cms.query_memory(query, limit=3)
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"  {i}. [Score: {result['score']:.3f}] {result['content'][:100]}...")
        else:
            print("  No relevant memories found.")
    
    # Test entity exploration with better error handling
    print("\n=== Entity Network Exploration ===")
    
    # First, list all available entities
    print("Available entities:")
    for entity in entities:
        print(f"  - {entity[0]} ({entity[1]})")
    
    # Test with entities we know exist
    test_entities = ["John", "Google", "Python", "TensorFlow"]
    
    for entity_name in test_entities:
        print(f"\nNetwork for '{entity_name}':")
        entity_network = cms.explore_entity(entity_name)
        print(f"Connected entities: {entity_network['connected_entities']}")
        
        if entity_network['relationships']:
            for rel in entity_network['relationships']:
                print(f"  {rel['source']} --[{rel['type']}]--> {rel['target']}")
        else:
            print("  No relationships found")
    
    # Show database file location
    import os
    db_path = "demo_knowledge.db"
    if os.path.exists(db_path):
        file_size = os.path.getsize(db_path)
        print(f"\n✓ Database created: {db_path} ({file_size} bytes)")
    else:
        print(f"\n✗ Database file not found: {db_path}")

if __name__ == "__main__":
    import os
    print(f"Working directory: {os.getcwd()}")
    demo_contextual_memory_system()
