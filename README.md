# Zenith AI Assistant

An end-to-end Agentic AI application built with LangGraph and Streamlit, adapted from [krishnaik06/Agentic-Ai-Project](https://github.com/krishnaik06/Agentic-Ai-Project).

## 🌟 Features

- **Basic Chatbot**: Simple conversational AI powered by Groq LLMs
- **Chatbot with Tools**: Enhanced chatbot with web search capabilities using Tavily
- **LangGraph Integration**: Modular, graph-based workflow architecture
- **Multiple LLM Support**: Groq models (Mixtral, Llama 3.1, Llama 3.3, Gemma2)
- **Streamlit UI**: Clean, interactive web interface

## 📁 Project Structure

```
zenith/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── Code/
│   ├── main.py                # Application logic
│   ├── src/
│   │   ├── state/             # State management
│   │   ├── llms/              # LLM providers
│   │   ├── tools/             # Agent tools
│   │   ├── nodes/             # Graph nodes
│   │   └── graph/             # Workflow graphs
│   └── ui/                    # UI components
│       ├── config.py          # Configuration manager
│       ├── config.ini         # UI settings
│       ├── load_ui.py         # UI loader
│       ├── display_result.py  # Result display
│       └── chat_app.py        # Standalone chat interface
└── Docs/                      # Documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+ (recommended)
- Groq API Key ([Get one here](https://console.groq.com/keys))
- Tavily API Key for tool-based chatbot ([Get one here](https://app.tavily.com/home))

### Installation

1. **Activate virtual environment**
```bash
cd /Users/tarunwuyyuru/Battinson/GenAI_Work/projects/zenith
source .venv/bin/activate
```

2. **Install dependencies** (if not already installed)
```bash
pip install -r requirements.txt
```

### Running the Application

**Main Agentic Application:**
```bash
streamlit run app.py
```

**Standalone Chat Interface:**
```bash
streamlit run Code/ui/chat_app.py
```

## 🎯 Usage

1. **Select LLM Provider**: Choose Groq
2. **Select Model**: Pick your preferred model
3. **Enter API Key**: Provide your Groq API key
4. **Select Use Case**: Basic Chatbot or Chatbot with Tool
5. **Start Chatting**: Enter your message

## 🏗️ Architecture

### LangGraph Workflow

```
Basic Chatbot Flow:
START → chatbot → END

Chatbot with Tools Flow:
START → chatbot → [conditional] → tools → chatbot → END
```

### Components

- **State**: Manages message history with automatic aggregation
- **Nodes**: Process units (chatbot logic, tool execution)
- **Edges**: Define workflow transitions
- **Tools**: External capabilities (web search via Tavily)
- **LLMs**: Language models (Groq integration)

## 🔧 Configuration

Edit `Code/ui/config.ini` to customize settings.

## 📚 Key Dependencies

- LangChain & LangGraph
- Streamlit
- Groq & Tavily APIs
