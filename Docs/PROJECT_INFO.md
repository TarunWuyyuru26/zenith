# Zenith AI Assistant - Project Documentation

## Overview

Zenith is an end-to-end Agentic AI application that demonstrates LangGraph's capabilities for building modular, stateful AI workflows. The project is adapted from Krish Naik's Agentic AI Project and implements a multi-use-case chatbot system with tool integration.

## Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────┐
│                      Streamlit UI Layer                      │
│  (User Interface, Configuration, Display Management)         │
└──────────────────┬──────────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                   Application Layer                          │
│  (main.py - Orchestrates UI, LLM, and Graph)                │
└──────────────────┬──────────────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
┌───────▼────────┐   ┌────────▼─────────┐
│  LLM Provider  │   │  Graph Builder   │
│   (Groq)       │   │  (LangGraph)     │
└───────┬────────┘   └────────┬─────────┘
        │                     │
        │            ┌────────▼─────────┐
        │            │   State Manager  │
        │            └────────┬─────────┘
        │                     │
        │            ┌────────▼─────────┐
        │            │      Nodes       │
        │            │  - Basic Chat    │
        │            │  - Tool-Enhanced │
        └────────────┤                  │
                     └────────┬─────────┘
                              │
                     ┌────────▼─────────┐
                     │      Tools       │
                     │  (Tavily Search) │
                     └──────────────────┘
```

### Component Details

#### 1. State Management (`Code/src/state/`)
- **Purpose**: Manages conversation state across graph nodes
- **Key File**: `state.py`
- **Implementation**: Uses LangGraph's `add_messages` for automatic message aggregation

```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

#### 2. LLM Providers (`Code/src/llms/`)
- **Purpose**: Abstracts LLM provider implementations
- **Current Implementation**: Groq (ChatGroq)
- **Extensible**: Can add OpenAI, Anthropic, Ollama, etc.

**Groq Client Features:**
- API key management
- Model selection
- Error handling
- Environment variable support

#### 3. Tools (`Code/src/tools/`)
- **Purpose**: External capabilities for enhanced chatbot
- **Current Implementation**: Tavily web search
- **Pattern**: Tool definition + ToolNode creation

```python
tools = [TavilySearchResults(max_results=2)]
tool_node = ToolNode(tools=tools)
```

#### 4. Nodes (`Code/src/nodes/`)
- **Purpose**: Processing units in the graph workflow
- **Implementations**:
  - **BasicChatbotNode**: Simple LLM invocation
  - **ChatbotWithToolNode**: LLM with tool binding

**Node Pattern:**
```python
class Node:
    def __init__(self, model):
        self.llm = model
    
    def process(self, state: State) -> dict:
        # Process and return updated state
        return {"messages": ...}
```

#### 5. Graph Builder (`Code/src/graph/`)
- **Purpose**: Constructs LangGraph workflows
- **Methods**:
  - `basic_chatbot_build_graph()`: Simple linear flow
  - `chatbot_with_tools_build_graph()`: Conditional tool routing
  - `setup_graph(usecase)`: Factory method

**Graph Construction Pattern:**
```python
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
compiled_graph = graph_builder.compile()
```

#### 6. UI Layer (`Code/ui/`)

**Components:**
- **config.py**: Configuration management from INI file
- **load_ui.py**: Streamlit UI loader and user control collector
- **display_result.py**: Result rendering for different use cases
- **chat_app.py**: Standalone chat interface

**UI Flow:**
1. Load configuration
2. Display sidebar controls (LLM, model, API keys, use case)
3. Collect user input
4. Return control dictionary

## Use Cases

### 1. Basic Chatbot

**Description**: Simple conversational AI without external tools.

**Workflow:**
```
User Input → LLM Processing → Response
```

**Graph Structure:**
```
START → chatbot_node → END
```

**Example Queries:**
- "Explain machine learning"
- "Write a Python function"
- "Tell me a story"

### 2. Chatbot with Tool

**Description**: Enhanced chatbot with web search capabilities.

**Workflow:**
```
User Input → LLM (decide tool use) → [Tool Execution?] → Response
                                           ↓
                                      Tool Node → LLM (with tool results)
```

**Graph Structure:**
```
START → chatbot → [tools_condition] → tools → chatbot → END
                        ↓
                       END (if no tools needed)
```

**Example Queries:**
- "What's the latest AI news?"
- "Search for LangGraph tutorials"
- "Find information about quantum computing"

## Configuration

### UI Configuration (`Code/ui/config.ini`)

```ini
[DEFAULT]
PAGE_TITLE = Zenith AI Assistant
LLM_OPTIONS = Groq
GROQ_MODEL_OPTIONS = mixtral-8x7b-32768, llama-3.1-70b-versatile, llama-3.3-70b-versatile, gemma2-9b-it
USECASE_OPTIONS = Basic Chatbot, Chatbot with Tool
```

### Environment Variables

Required:
- `GROQ_API_KEY`: Groq API key (can be entered in UI)
- `TAVILY_API_KEY`: Tavily API key for tool-based chatbot

## Extending the Application

### Adding a New LLM Provider

1. Create `Code/src/llms/new_provider.py`:
```python
class NewProviderLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
    
    def get_llm_model(self):
        # Implementation
        return model
```

2. Update `config.ini`:
```ini
LLM_OPTIONS = Groq, NewProvider
```

3. Update `load_ui.py` to handle new provider

### Adding a New Tool

1. Create `Code/src/tools/new_tool.py`:
```python
from langchain_community.tools import NewTool

def get_new_tool():
    return NewTool(...)
```

2. Update `search_tool.py` to include new tool:
```python
def get_tools():
    return [TavilySearchResults(), NewTool()]
```

### Adding a New Use Case

1. Create node in `Code/src/nodes/new_usecase_node.py`
2. Add graph building method in `graph_builder.py`:
```python
def new_usecase_build_graph(self):
    # Define nodes and edges
    pass
```

3. Update `setup_graph()` method
4. Update `config.ini` with new use case option
5. Update `display_result.py` to handle new use case

## Development Workflow

### Local Development

1. Activate virtual environment:
```bash
source .venv/bin/activate
```

2. Run application:
```bash
streamlit run app.py
```

3. Test changes in real-time (Streamlit auto-reloads)

### Testing

Manual testing checklist:
- [ ] UI loads without errors
- [ ] API key validation works
- [ ] Basic chatbot responds correctly
- [ ] Tool-based chatbot invokes search
- [ ] Error handling displays appropriate messages

### Code Organization Guidelines

- **Separation of Concerns**: UI, logic, and data layers separate
- **Modularity**: Each component is self-contained
- **Extensibility**: Easy to add new LLMs, tools, use cases
- **Configuration-Driven**: Settings in INI file, not hardcoded

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all `__init__.py` files exist
   - Check virtual environment is activated
   - Verify all dependencies installed

2. **Graph Compilation Errors**
   - Check node return types match State structure
   - Verify all edges are properly defined
   - Ensure START and END are connected

3. **LLM Connection Issues**
   - Verify API key is correct
   - Check internet connection
   - Review provider-specific error messages

4. **Tool Execution Failures**
   - Ensure TAVILY_API_KEY is set
   - Check tool configuration
   - Verify tool output format matches expected structure

## Performance Considerations

- **Streaming**: Consider implementing streaming responses for better UX
- **Caching**: Add caching for repeated queries
- **Async**: Use async operations for tool calls
- **Rate Limiting**: Implement rate limiting for API calls

## Security Best Practices

- Store API keys in environment variables or `.env` file
- Add `.env` to `.gitignore`
- Never commit API keys to repository
- Validate user input before processing
- Implement proper error handling to avoid exposing sensitive info

## Future Enhancements

- [ ] Add more LLM providers (OpenAI, Anthropic, Ollama)
- [ ] Implement RAG (Retrieval-Augmented Generation)
- [ ] Add memory/conversation persistence
- [ ] Implement user authentication
- [ ] Add more tools (web scraper, calculator, code executor)
- [ ] Create AI News aggregation use case
- [ ] Add streaming responses
- [ ] Implement conversation export/import
- [ ] Add analytics dashboard
- [ ] Multi-language support

## References

- [Original Project by Krish Naik](https://github.com/krishnaik06/Agentic-Ai-Project)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Tavily API Documentation](https://docs.tavily.com/)

## License

Apache 2.0

## Contributors

- Original: Krish Naik
- Adaptation: Tarun Wuyyuru
