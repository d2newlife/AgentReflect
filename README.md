# 🚀 AI Tweet Generator with Self-Reflection

> **🎯 Create viral tech tweets with AI-powered self-reflection and optimization**

Though this project is about reflection in the generation of tweets it is a foundational piece in having
your LLM reflect on what it has created and producting something better. I see this for use in blogs, articles, tweets, emails, etc.

This implementation is focused on a content creation system that generates, critiques, and iteratively improves Twitter posts for maximum engagement using LangChain and Google Gemini AI.

## 📋 Table of Contents

- [💡 About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [💻 Technologies Used](#-technologies-used)
- [🛠️ Installation & Setup](#️-installation--setup)
- [▶️ Running Locally](#️-running-locally)
- [🧪 Testing](#-testing)
- [📌 Project Status](#-project-status)

## 💡 About The Project

### 🎯 Motivation
In today's digital landscape, creating engaging social media content is crucial for tech professionals and influencers. However, crafting viral tweets that resonate with audiences requires deep understanding of engagement psychology, timing, and platform-specific optimization strategies.

### 🔍 Problem Solved
This project addresses the challenge of **content optimization for social media virality** by implementing an AI-powered system that:
- Generates compelling tech-focused tweets using advanced language models
- Provides brutally honest, data-driven feedback on content quality
- Iteratively improves content through self-reflection cycles
- Optimizes for maximum engagement (likes, retweets, impressions)

### 🧠 Key Learnings
**LangChain State Management**: Mastered LangGraph's stateful workflow orchestration to create a cyclical AI system where generation and reflection nodes work in tandem. Implemented TypedDict-based state management with operator-based message accumulation for seamless conversation flow.

**AI Content Strategy**: Gained deep expertise in prompt engineering for viral content creation, understanding the psychology of social media engagement, and implementing feedback loops that mirror human content optimization processes.

## ✨ Key Features

- **🤖 AI-Powered Tweet Generation**: Creates engaging tech content using Google Gemini 2.5 Flash
- **🔄 Self-Reflection System**: AI critiques and improves its own content through multiple iterations
- **📊 Virality Optimization**: Built-in strategies for maximizing likes, retweets, and impressions
- **🎯 Tech-Focused Content**: Specialized for software engineers, developers, and tech enthusiasts
- **⚡ Real-time Processing**: Fast content generation with intelligent stopping conditions
- **🎨 Professional Branding**: Configurable influencer persona with consistent tone and style

## 💻 Technologies Used

### Core Technologies
- **Python 3.8+** - Primary programming language
- **LangChain** - AI application framework and workflow orchestration
- **LangGraph** - State graph management for complex AI workflows
- **Google Gemini 2.5 Flash** - Advanced language model for content generation
- **LangSmith** - AI model evaluation and feedback loop

### Development Tools
- **python-dotenv** - Environment variable management
- **typing_extensions** - Enhanced type hints for better code quality
- **Black** - Code formatting and style consistency
- **isort** - Import statement organization

### Architecture Patterns
- **State Management** - TypedDict-based state graphs with operator patterns
- **Chain Orchestration** - Sequential and conditional AI chain execution
- **Message-Based Architecture** - LangChain message system for conversation flow

### Langgraph Visual Depiction
![alt text](https://github.com/d2newlife/AgentReflect/blob/master/image/AgentReflect.Graph.png?raw=true)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Git

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-tweet-generator.git
cd ai-tweet-generator
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your Google Gemini API key
```

5. **Configure your API key**
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

5. **Configure your LangSmit key**
Go to : https://smith.langchain.com/  and get your key
```
In the .env file in the root directory add the following:

LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="AgentReflect"
LANGCHAIN_API_KEY="<YOUR KEY HERE>"
```

## ▶️ Running Locally

### Basic Usage
```bash
python main.py
```

### Custom Tweet Generation
Modify the input message in `main.py`:
```python
input = HumanMessage(content="Your custom tweet topic here")
```

### Expected Output
The system will generate and iterate on tweets, displaying:
- Initial tweet generation
- AI-powered critique and suggestions
- Improved tweet versions
- Final optimized content

## 🧪 Testing

### Run Code Quality Checks
```bash
# Format code with Black
black *.py

# Sort imports with isort
isort *.py
```

### Manual Testing
The project includes built-in testing through the main execution flow. Each run demonstrates:
- State graph execution
- Message passing between nodes
- Conditional logic for iteration control
- Final content output validation

## 📌 Project Status
Version 1.0 Complete