<div align="center">
  <svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    <!-- Background Gradient -->
    <defs>
      <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#0a1428;stop-opacity:1" />
        <stop offset="50%" style="stop-color:#1a2040;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#2d1b69;stop-opacity:1" />
      </linearGradient>
      
      <!-- Glow effects -->
      <filter id="glow">
        <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
        <feMerge> 
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      
      <filter id="softGlow">
        <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
        <feMerge> 
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    
    <!-- Background -->
    <rect width="800" height="400" fill="url(#bgGradient)"/>
    
    <!-- Left Side - Circuit Brain -->
    <g transform="translate(80,100)">
      <!-- Brain outline -->
      <path d="M20,60 Q20,20 60,20 Q100,20 120,40 Q140,20 180,20 Q220,20 220,60 Q220,80 200,100 Q220,120 220,160 Q220,200 180,200 Q140,200 120,180 Q100,200 60,200 Q20,200 20,160 Q20,120 40,100 Q20,80 20,60 Z" 
            fill="none" 
            stroke="#00d4ff" 
            stroke-width="3" 
            filter="url(#glow)"/>
      
      <!-- Circuit patterns inside brain -->
      <!-- Horizontal lines -->
      <line x1="40" y1="80" x2="100" y2="80" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="120" y1="80" x2="180" y2="80" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="60" y1="120" x2="120" y2="120" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="140" y1="120" x2="200" y2="120" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="40" y1="160" x2="100" y2="160" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="120" y1="160" x2="180" y2="160" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      
      <!-- Vertical lines -->
      <line x1="80" y1="50" x2="80" y2="90" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="160" y1="50" x2="160" y2="90" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="100" y1="100" x2="100" y2="140" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="140" y1="100" x2="140" y2="140" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="80" y1="140" x2="80" y2="180" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      <line x1="160" y1="140" x2="160" y2="180" stroke="#00d4ff" stroke-width="2" opacity="0.8"/>
      
      <!-- Circuit nodes -->
      <circle cx="80" cy="80" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      <circle cx="160" cy="80" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      <circle cx="100" cy="120" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      <circle cx="140" cy="120" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      <circle cx="80" cy="160" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      <circle cx="160" cy="160" r="4" fill="#00d4ff" filter="url(#softGlow)"/>
      
      <!-- Additional circuit elements -->
      <circle cx="60" cy="100" r="3" fill="#00d4ff" opacity="0.7"/>
      <circle cx="180" cy="100" r="3" fill="#00d4ff" opacity="0.7"/>
      <circle cx="120" cy="60" r="3" fill="#00d4ff" opacity="0.7"/>
      <circle cx="120" cy="180" r="3" fill="#00d4ff" opacity="0.7"/>
    </g>
    
    <!-- Center Text -->
    <g transform="translate(400,200)">
      <text x="0" y="-20" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="42" font-weight="300">Contextual Memory</text>
      <text x="0" y="30" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="42" font-weight="300">Graph System</text>
    </g>
    
    <!-- Right Side - Knowledge Graph Network -->
    <g transform="translate(580,100)">
      <!-- Large central node -->
      <circle cx="60" cy="60" r="12" fill="none" stroke="#b83dba" stroke-width="3" filter="url(#glow)"/>
      
      <!-- Medium nodes -->
      <circle cx="20" cy="40" r="8" fill="none" stroke="#b83dba" stroke-width="2" opacity="0.8"/>
      <circle cx="100" cy="30" r="8" fill="none" stroke="#b83dba" stroke-width="2" opacity="0.8"/>
      <circle cx="120" cy="80" r="8" fill="none" stroke="#b83dba" stroke-width="2" opacity="0.8"/>
      <circle cx="90" cy="120" r="8" fill="none" stroke="#b83dba" stroke-width="2" opacity="0.8"/>
      <circle cx="30" cy="100" r="8" fill="none" stroke="#b83dba" stroke-width="2" opacity="0.8"/>
      
      <!-- Small nodes -->
      <circle cx="40" cy="20" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      <circle cx="140" cy="50" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      <circle cx="130" cy="110" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      <circle cx="60" cy="140" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      <circle cx="10" cy="80" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      <circle cx="80" cy="10" r="5" fill="none" stroke="#d946ef" stroke-width="2" opacity="0.6"/>
      
      <!-- Connection lines -->
      <line x1="60" y1="60" x2="20" y2="40" stroke="#b83dba" stroke-width="2" opacity="0.6"/>
      <line x1="60" y1="60" x2="100" y2="30" stroke="#b83dba" stroke-width="2" opacity="0.6"/>
      <line x1="60" y1="60" x2="120" y2="80" stroke="#b83dba" stroke-width="2" opacity="0.6"/>
      <line x1="60" y1="60" x2="90" y2="120" stroke="#b83dba" stroke-width="2" opacity="0.6"/>
      <line x1="60" y1="60" x2="30" y2="100" stroke="#b83dba" stroke-width="2" opacity="0.6"/>
      
      <!-- Secondary connections -->
      <line x1="20" y1="40" x2="40" y2="20" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      <line x1="100" y1="30" x2="140" y2="50" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      <line x1="120" y1="80" x2="130" y2="110" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      <line x1="90" y1="120" x2="60" y2="140" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      <line x1="30" y1="100" x2="10" y2="80" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      <line x1="100" y1="30" x2="80" y2="10" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
      
      <!-- Inter-node connections -->
      <line x1="20" y1="40" x2="30" y2="100" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
      <line x1="100" y1="30" x2="120" y2="80" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
      <line x1="120" y1="80" x2="90" y2="120" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
      
      <!-- Memory nodes (smaller, different color) -->
      <circle cx="160" cy="40" r="4" fill="#ec4899" opacity="0.8"/>
      <circle cx="150" cy="90" r="4" fill="#ec4899" opacity="0.8"/>
      <circle cx="110" cy="140" r="4" fill="#ec4899" opacity="0.8"/>
      <circle cx="40" cy="130" r="4" fill="#ec4899" opacity="0.8"/>
      <circle cx="0" cy="60" r="4" fill="#ec4899" opacity="0.8"/>
    </g>
    
    <!-- Decorative elements -->
    <!-- Top subtle grid -->
    <g opacity="0.1">
      <line x1="0" y1="50" x2="800" y2="50" stroke="#ffffff" stroke-width="1"/>
      <line x1="0" y1="100" x2="800" y2="100" stroke="#ffffff" stroke-width="1"/>
      <line x1="0" y1="300" x2="800" y2="300" stroke="#ffffff" stroke-width="1"/>
      <line x1="0" y1="350" x2="800" y2="350" stroke="#ffffff" stroke-width="1"/>
    </g>
  </svg>
</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Mobile](https://img.shields.io/badge/Mobile-Optimized-brightgreen.svg)](https://github.com/aiwithjusl/contextual-memory-graph-system)
[![AI](https://img.shields.io/badge/AI-Knowledge%20Graph-purple.svg)](https://github.com/aiwithjusl/contextual-memory-graph-system)

**🧠 Advanced AI Knowledge Graph with Contextual Memory**

*Mobile-optimized system that builds dynamic relationships from conversations and documents*

</div>

---

## 🚀 What It Does

- **🔗 Builds Knowledge Graphs** - Automatically extracts entities and relationships from text
- **🧠 Contextual Memory** - Preserves meaning across interactions, not just keywords  
- **📱 Mobile-First** - Optimized for Android devices with efficient SQLite storage
- **🔒 Privacy-Preserving** - All processing happens locally on your device

## ⚡ Quick Start

```bash
# Download and run
python contextual_memory_mvp.py

# Add memories
cms.add_memory("John works at Google and specializes in AI research.")

# Query the system  
results = cms.query_memory("Tell me about AI research")
```

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Entity Extraction** | Automatically identifies people, organizations, concepts |
| **Relationship Detection** | Discovers connections like "works at", "created", "uses" |
| **Semantic Search** | Context-aware retrieval beyond keyword matching |
| **Importance Scoring** | Memory relevance evolves based on access patterns |

## 🏗️ Architecture

```
ContextualMemorySystem
├── NLP Processor (Entity extraction, relationships)
├── Context Weaver (Memory creation, linking)  
├── Memory Retriever (Query processing, ranking)
└── Mobile Storage (SQLite backend, graph relations)
```

## 📊 Demo Results

```
System Stats: {'entities': 48, 'relationships': 15, 'memories': 5}

Query: 'Tell me about John'
  1. [Score: 0.348] John works at Google and specializes in AI research...
  2. [Score: 0.348] The AI algorithm that John developed uses Python...

✓ Database created: demo_knowledge.db (77,824 bytes)
```

## 🎯 Use Cases

- **Personal AI Assistant** - Build personalized knowledge from conversations
- **Enterprise Knowledge Management** - Extract insights from company documents  
- **Research & Development** - Track connections and dependencies
- **Education & Learning** - Create personalized learning paths

## 🛡️ Privacy & Security

- 🔒 **Local Processing** - All data stays on device
- 🚫 **No External APIs** - No data transmitted to external services
- 🔐 **Encrypted Storage** - SQLite database with optional encryption

## 📱 Requirements

- Python 3.7+
- Standard library only (no external dependencies)
- Tested on Samsung Galaxy S24 with Pydroid 3

## 📁 Files

- `contextual_memory_mvp.py` - Main system implementation
- `README.md` - Complete technical documentation
- `LICENSE` - MIT License

## 📞 Contact

<div align="center">

**Justin Lane** | *AI/ML Developer*

[![Email](https://img.shields.io/badge/Email-aiwithjusl.dev%40gmail.com-red?style=flat&logo=gmail)](mailto:aiwithjusl.dev@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Justin%20Lane-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/justin-lane-69b960219)
[![GitHub](https://img.shields.io/badge/GitHub-aiwithjusl-black?style=flat&logo=github)](https://github.com/aiwithjusl)

</div>

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

*Built for senior-level AI/ML engineering positions and enterprise consulting opportunities.*

</div>
