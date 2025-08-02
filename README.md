<p align="center">
  <img src="images/file_0000000084c061f8b0bb3ac20bbd9b7d (1).png" alt="Contextual Memory Graph System Banner" width="100%" />
</p>

# Contextual Memory Graph System

> **Advanced AI Knowledge Graph with Contextual Memory for Mobile Devices**

A sophisticated, mobile-optimized knowledge graph system that builds dynamic contextual relationships from conversations, documents, and interactions. Unlike traditional RAG systems, this creates persistent, interconnected memories that improve understanding over time.

## 🚀 Features

### Core Capabilities
- **Dynamic Knowledge Graph**: Automatically builds relationships between entities, concepts, and memories
- **Contextual Memory**: Preserves context and meaning across interactions, not just keyword matching  
- **Advanced NLP Pipeline**: Entity extraction, relationship detection, and semantic similarity
- **Mobile-First Architecture**: Optimized for Android devices with efficient SQLite storage
- **Privacy-Preserving**: All processing happens locally on device
- **Scalable Design**: Foundation for enterprise knowledge management systems

### Technical Highlights
- **Graph Neural Network Concepts**: Implements importance scoring and relationship weighting
- **Incremental Learning**: Memory importance evolves based on access patterns and connections
- **Semantic Retrieval**: Context-aware search beyond simple keyword matching
- **Mobile Optimization**: WAL mode SQLite, memory-efficient processing, battery-conscious design
- **Modular Architecture**: Clean separation of concerns for easy extension and modification

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│           ContextualMemorySystem            │
├─────────────────────────────────────────────┤
│  ┌─────────────┐ ┌──────────────────────┐   │
│  │ NLP         │ │ ContextWeaver        │   │
│  │ Processor   │ │ - Entity Linking     │   │
│  │             │ │ - Relationship       │   │
│  │             │ │   Detection          │   │
│  └─────────────┘ └──────────────────────┘   │
│  ┌─────────────┐ ┌──────────────────────┐   │
│  │ Memory      │ │ MobileGraphStorage   │   │
│  │ Retriever   │ │ - SQLite Backend     │   │
│  │             │ │ - Graph Relations    │   │
│  │             │ │ - Mobile Optimized   │   │
│  └─────────────┘ └──────────────────────┘   │
└─────────────────────────────────────────────┘
```

## 📱 Requirements

### Software Dependencies
```bash
- Python 3.7+
- SQLite3 (included with Python)
- Standard library only (no external dependencies for core functionality)
```

### Mobile Environment
- **Tested on**: Samsung Galaxy S24 with Pydroid 3
- **Storage**: ~100KB for core system + variable data storage
- **Memory**: Efficient memory usage with streaming processing
- **Performance**: Sub-second response times for typical queries

## 🛠️ Installation

### Option 1: Direct Download
1. Download `contextual_memory_mvp.py`
2. Run directly with Python 3.7+

### Option 2: Clone Repository
```bash
git clone https://github.com/yourusername/contextual-memory-graph-system.git
cd contextual-memory-graph-system
python contextual_memory_mvp.py
```

### Option 3: Mobile (Pydroid 3)
1. Install Pydroid 3 from Google Play Store
2. Copy the code into a new Python file
3. Run directly on your Android device

## 🎯 Quick Start

### Basic Usage
```python
from contextual_memory_mvp import ContextualMemorySystem

# Initialize the system
cms = ContextualMemorySystem("my_knowledge.db")

# Add memories
cms.add_memory("John works at Google and specializes in AI research.")
cms.add_memory("Python is widely used for machine learning projects.")

# Query the system
results = cms.query_memory("Tell me about AI research")
for result in results:
    print(f"[{result['score']:.3f}] {result['content']}")

# Explore entity relationships  
network = cms.explore_entity("John")
print(f"Connected to: {network['connected_entities']}")
```

### Advanced Features
```python
# Add contextual tags
cms.add_memory("Neural networks require large datasets", ["ml", "data"])

# Get system statistics
stats = cms.get_system_stats()
print(f"Entities: {stats['entities']}, Relationships: {stats['relationships']}")

# Export/backup knowledge graph
# Database is automatically saved to SQLite file
```

## 📊 Demo Output

Running the included demo shows the system in action:

```
=== Contextual Memory Graph System MVP Demo ===

Adding sample memories...
1. Memory stored with ID: fd4f261fee03
2. Memory stored with ID: 1448b5f2d586
[... additional memories ...]

System Stats: {'entities': 48, 'relationships': 15, 'memories': 5}

=== Debug: Extracted Entities ===
  PERSON: John
  ORGANIZATION: Google  
  TECH: Python
  TECH: TensorFlow
  CONCEPT: research
[... additional entities ...]

=== Debug: Extracted Relationships ===
  John --[WORKS_AT]--> Google
  He --[CREATED]--> new machine learning algorithm
  AI research --[LOCATED_IN]--> Mountain View
[... additional relationships ...]

✓ Database created: demo_knowledge.db (77824 bytes)
```

## 🔧 Configuration

### Customization Options
```python
# Adjust similarity thresholds
cms.retriever.nlp.context_threshold = 0.4  # Default: 0.3

# Modify entity extraction patterns
cms.nlp.entity_patterns['CUSTOM'] = r'\b[A-Z][a-z]+Pattern\b'

# Configure importance scoring
cms.weaver._calculate_memory_importance()  # Override for custom scoring
```

### Performance Tuning
```python
# Database optimization
storage = MobileGraphStorage("optimized.db")
storage.connection.execute("PRAGMA cache_size=10000")
storage.connection.execute("PRAGMA temp_store=MEMORY")
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
python contextual_memory_mvp.py
```

The demo includes:
- Entity extraction validation
- Relationship detection testing  
- Query relevance scoring
- Memory importance calculation
- Database integrity checks

## 🚀 Use Cases

### Personal AI Assistant
- Build personalized knowledge from conversations
- Remember context across sessions
- Learn individual preferences and patterns

### Enterprise Knowledge Management  
- Extract insights from company documents
- Build organizational knowledge graphs
- Enable contextual search across information silos

### Research and Development
- Track research connections and dependencies
- Build knowledge maps from literature
- Identify gaps and opportunities in knowledge domains

### Education and Learning
- Create personalized learning paths
- Build concept maps from study materials
- Track learning progress and connections

## 🛡️ Privacy & Security

- **Local Processing**: All data stays on device
- **No External APIs**: No data transmitted to external services
- **Encrypted Storage**: SQLite database with optional encryption
- **Minimal Footprint**: Lightweight system with small attack surface

## 🔄 Roadmap

### Portfolio Version Enhancements
- **Advanced NLP**: Transformer-based entity extraction and embedding
- **Graph Neural Networks**: Sophisticated relationship learning and inference
- **Multi-modal Support**: Image, audio, and video content integration
- **Real-time Sync**: Multi-device synchronization with conflict resolution
- **Enterprise Features**: Role-based access, audit trails, compliance reporting

### Potential Integrations
- **Vector Databases**: Hybrid graph + vector storage for semantic search
- **Knowledge Base APIs**: Integration with external knowledge sources
- **Machine Learning Pipelines**: Automated insight extraction and prediction
- **Visualization Tools**: Interactive graph exploration and analysis

## 📄 License

MIT License - see LICENSE file for details

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

**Project Developer**: Justin Lane
- Email: aiwithjusl.dev@gmail.com
- LinkedIn: Justin Lane (https://www.linkedin.com/in/justin-lane-69b960219)
- GitHub: aiwithjusl (https://github.com/aiwithjusl/aiwithjusl)

---

## 🎖️ Recognition

*This project demonstrates advanced capabilities in:*
- **Graph Database Design** - Custom SQLite schema with relationship modeling
- **Natural Language Processing** - Entity extraction and semantic analysis  
- **Mobile Optimization** - Resource-efficient algorithms for mobile deployment
- **System Architecture** - Modular, scalable design for enterprise applications
- **AI/ML Engineering** - Contextual learning and importance scoring algorithms

*Built for senior-level AI/ML engineering positions and enterprise consulting opportunities.*
