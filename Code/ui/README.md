# Zenith Chat Application

A Streamlit-based chat and posting application.

## Features

- **Chat Interface**: Interactive chat with message history
- **Posts**: Create and manage posts with timestamps
- **Clean UI**: Modern interface with custom styling
- **Session Management**: Persistent chat and post history during session

## Usage

### Run the application:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the Streamlit app
streamlit run Code/ui/chat_app.py
```

### Access the app:
- The app will open in your default browser
- Default URL: http://localhost:8501

## Features Overview

### Chat Mode
- Type messages in the input box
- View chat history with timestamps
- Clear chat history option in sidebar

### Posts Mode
- Create posts with optional titles
- View all posts in chronological order
- Like and delete posts
- Clear all posts option

## Integration Points

The current implementation uses an echo response for demonstration. To integrate with your LLM:

1. Import your LLM client from `Code/src/llms/`
2. Replace the echo response in the chat section (line ~67) with your LLM call
3. Add any necessary prompt engineering or context

Example:
```python
# Replace this line:
response = f"Echo: {prompt}"

# With your LLM integration:
from src.llms.groq_client import get_groq_response
response = get_groq_response(prompt, st.session_state.messages)
```

## Customization

- Modify CSS in the `st.markdown()` section for styling
- Add more features in the sidebar
- Extend post functionality (comments, categories, etc.)
- Integrate RAG or agent workflows from `Code/src/graph/`
