import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Zenith Chat",
    page_icon="💬",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "posts" not in st.session_state:
    st.session_state.posts = []

# Custom CSS
st.markdown("""
    <style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .post-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .post-header {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 0.5rem;
    }
    .post-content {
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("💬 Zenith Chat")
    st.markdown("---")
    
    # Tab selection
    tab = st.radio("Select Mode:", ["Chat", "Posts"], key="mode_selector")
    
    st.markdown("---")
    
    # Clear buttons
    if tab == "Chat":
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
    else:
        if st.button("🗑️ Clear All Posts"):
            st.session_state.posts = []
            st.rerun()
    
    st.markdown("---")
    st.caption("Built with Streamlit")

# Main content area
if tab == "Chat":
    st.header("Chat Interface")
    
    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                st.caption(message["timestamp"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": timestamp
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(timestamp)
        
        # Generate assistant response (placeholder - integrate your LLM here)
        with st.chat_message("assistant"):
            response = f"Echo: {prompt}"
            st.markdown(response)
            response_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.caption(response_timestamp)
        
        # Add assistant message to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": response_timestamp
        })
        
        st.rerun()

else:  # Posts tab
    st.header("Posts")
    
    # Create post section
    with st.expander("✍️ Create New Post", expanded=True):
        with st.form(key="post_form", clear_on_submit=True):
            post_title = st.text_input("Title (optional)")
            post_content = st.text_area("What's on your mind?", height=150)
            col1, col2 = st.columns([1, 5])
            with col1:
                submit_post = st.form_submit_button("📤 Post", use_container_width=True)
            
            if submit_post and post_content:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.posts.insert(0, {
                    "title": post_title if post_title else "Untitled Post",
                    "content": post_content,
                    "timestamp": timestamp
                })
                st.success("Posted successfully!")
                st.rerun()
            elif submit_post and not post_content:
                st.error("Post content cannot be empty!")
    
    st.markdown("---")
    
    # Display posts
    if st.session_state.posts:
        st.subheader(f"All Posts ({len(st.session_state.posts)})")
        for idx, post in enumerate(st.session_state.posts):
            with st.container():
                st.markdown(f"""
                    <div class="post-card">
                        <div class="post-header">
                            <strong>{post['title']}</strong> • {post['timestamp']}
                        </div>
                        <div class="post-content">
                            {post['content']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns([1, 1, 10])
                with col1:
                    if st.button("❤️", key=f"like_{idx}"):
                        st.toast("Liked!")
                with col2:
                    if st.button("🗑️", key=f"delete_{idx}"):
                        st.session_state.posts.pop(idx)
                        st.rerun()
    else:
        st.info("No posts yet. Create your first post above!")

# Footer
st.markdown("---")
st.caption("Zenith Chat Application - Powered by Streamlit")
