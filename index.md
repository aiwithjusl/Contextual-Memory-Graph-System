<div align="center">
  
<svg width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Background Gradient -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a1428;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#1a2040;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2d1b69;stop-opacity:1" />
    </linearGradient>
    
    <!-- Glow effects -->
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge> 
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="1" result="coloredBlur"/>
      <feMerge> 
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="600" height="300" fill="url(#bgGradient)"/>
  
  <!-- Left Side - Circuit Brain (scaled down) -->
  <g transform="translate(50,75)">
    <!-- Brain outline -->
    <path d="M15,45 Q15,15 45,15 Q75,15 90,30 Q105,15 135,15 Q165,15 165,45 Q165,60 150,75 Q165,90 165,120 Q165,150 135,150 Q105,150 90,135 Q75,150 45,150 Q15,150 15,120 Q15,90 30,75 Q15,60 15,45 Z" 
          fill="none" 
          stroke="#00d4ff" 
          stroke-width="2" 
          filter="url(#glow)"/>
    
    <!-- Circuit patterns inside brain -->
    <!-- Horizontal lines -->
    <line x1="30" y1="60" x2="75" y2="60" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="90" y1="60" x2="135" y2="60" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="45" y1="90" x2="90" y2="90" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="105" y1="90" x2="150" y2="90" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="30" y1="120" x2="75" y2="120" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="90" y1="120" x2="135" y2="120" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    
    <!-- Vertical lines -->
    <line x1="60" y1="37" x2="60" y2="67" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="120" y1="37" x2="120" y2="67" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="75" y1="75" x2="75" y2="105" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="105" y1="75" x2="105" y2="105" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="60" y1="105" x2="60" y2="135" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    <line x1="120" y1="105" x2="120" y2="135" stroke="#00d4ff" stroke-width="1.5" opacity="0.8"/>
    
    <!-- Circuit nodes -->
    <circle cx="60" cy="60" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    <circle cx="120" cy="60" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    <circle cx="75" cy="90" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    <circle cx="105" cy="90" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    <circle cx="60" cy="120" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    <circle cx="120" cy="120" r="3" fill="#00d4ff" filter="url(#softGlow)"/>
    
    <!-- Additional circuit elements -->
    <circle cx="45" cy="75" r="2" fill="#00d4ff" opacity="0.7"/>
    <circle cx="135" cy="75" r="2" fill="#00d4ff" opacity="0.7"/>
    <circle cx="90" cy="45" r="2" fill="#00d4ff" opacity="0.7"/>
    <circle cx="90" cy="135" r="2" fill="#00d4ff" opacity="0.7"/>
  </g>
  
  <!-- Center Text -->
  <g transform="translate(300,150)">
    <text x="0" y="-15" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="32" font-weight="300">Contextual Memory</text>
    <text x="0" y="20" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="32" font-weight="300">Graph System</text>
  </g>
  
  <!-- Right Side - Knowledge Graph Network (scaled down) -->
  <g transform="translate(435,75)">
    <!-- Large central node -->
    <circle cx="45" cy="45" r="9" fill="none" stroke="#b83dba" stroke-width="2" filter="url(#glow)"/>
    
    <!-- Medium nodes -->
    <circle cx="15" cy="30" r="6" fill="none" stroke="#b83dba" stroke-width="1.5" opacity="0.8"/>
    <circle cx="75" cy="22" r="6" fill="none" stroke="#b83dba" stroke-width="1.5" opacity="0.8"/>
    <circle cx="90" cy="60" r="6" fill="none" stroke="#b83dba" stroke-width="1.5" opacity="0.8"/>
    <circle cx="67" cy="90" r="6" fill="none" stroke="#b83dba" stroke-width="1.5" opacity="0.8"/>
    <circle cx="22" cy="75" r="6" fill="none" stroke="#b83dba" stroke-width="1.5" opacity="0.8"/>
    
    <!-- Small nodes -->
    <circle cx="30" cy="15" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    <circle cx="105" cy="37" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    <circle cx="97" cy="82" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    <circle cx="45" cy="105" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    <circle cx="7" cy="60" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    <circle cx="60" cy="7" r="4" fill="none" stroke="#d946ef" stroke-width="1.5" opacity="0.6"/>
    
    <!-- Connection lines -->
    <line x1="45" y1="45" x2="15" y2="30" stroke="#b83dba" stroke-width="1.5" opacity="0.6"/>
    <line x1="45" y1="45" x2="75" y2="22" stroke="#b83dba" stroke-width="1.5" opacity="0.6"/>
    <line x1="45" y1="45" x2="90" y2="60" stroke="#b83dba" stroke-width="1.5" opacity="0.6"/>
    <line x1="45" y1="45" x2="67" y2="90" stroke="#b83dba" stroke-width="1.5" opacity="0.6"/>
    <line x1="45" y1="45" x2="22" y2="75" stroke="#b83dba" stroke-width="1.5" opacity="0.6"/>
    
    <!-- Secondary connections -->
    <line x1="15" y1="30" x2="30" y2="15" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    <line x1="75" y1="22" x2="105" y2="37" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    <line x1="90" y1="60" x2="97" y2="82" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    <line x1="67" y1="90" x2="45" y2="105" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    <line x1="22" y1="75" x2="7" y2="60" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    <line x1="75" y1="22" x2="60" y2="7" stroke="#d946ef" stroke-width="1" opacity="0.4"/>
    
    <!-- Inter-node connections -->
    <line x1="15" y1="30" x2="22" y2="75" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
    <line x1="75" y1="22" x2="90" y2="60" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
    <line x1="90" y1="60" x2="67" y2="90" stroke="#d946ef" stroke-width="1" opacity="0.3"/>
    
    <!-- Memory nodes (smaller, different color) -->
    <circle cx="120" cy="30" r="3" fill="#ec4899" opacity="0.8"/>
    <circle cx="112" cy="67" r="3" fill="#ec4899" opacity="0.8"/>
    <circle cx="82" cy="105" r="3" fill="#ec4899" opacity="0.8"/>
    <circle cx="30" cy="97" r="3" fill="#ec4899" opacity="0.8"/>
    <circle cx="0" cy="45" r="3" fill="#ec4899" opacity="0.8"/>
  </g>
  
  <!-- Decorative elements -->
  <!-- Top subtle grid -->
  <g opacity="0.05">
    <line x1="0" y1="37" x2="600" y2="37" stroke="#ffffff" stroke-width="1"/>
    <line x1="0" y1="75" x2="600" y2="75" stroke="#ffffff" stroke-width="1"/>
    <line x1="0" y1="225" x2="600" y2="225" stroke="#ffffff" stroke-width="1"/>
    <line x1="0" y1="262" x2="600" y2="262" stroke="#ffffff" stroke-width="1"/>
  </g>
</svg>            
  
</div>

<div align="center">

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

## 👤 About the Author

**Justin Lane**  
🔗 GitHub: [@aiwithjusl](https://github.com/aiwithjusl)  
🔗 LinkedIn: [Justin Lane](https://www.linkedin.com/in/justin-lane-69b960219)  
📬 Email: aiwithjusl.dev@gmail.com

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

*Built for senior-level AI/ML engineering positions and enterprise consulting opportunities.*

</div>
