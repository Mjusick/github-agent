# GitHub Issues AI Agent

## Project Overview

This AI-powered GitHub Issues Agent is a tool designed to fetch, process, and analyze GitHub issues using advanced language models and vector storage technologies. The agent leverages OpenAI's language models and AstraDB for intelligent issue retrieval and processing.

## Key Features

- Fetch GitHub issues from specified repositories
- Convert issues into structured document format
- Store and index issues in a vector database
- Enable intelligent querying and analysis of GitHub issues

## Prerequisites

- Python 3.9+
- pip (Python package manager)

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/github-agent.git
cd github-agent
```

### 2. Create a Virtual Environment

```bash
# For macOS/Linux
python3 -m venv github-agent-env

# For Windows
python -m venv github-agent-env
```

### 3. Activate the Virtual Environment

```bash
# For macOS/Linux
source github-agent-env/bin/activate

# For Windows
github-agent-env\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key

# GitHub Configuration
GITHUB_TOKEN=your_github_personal_access_token

# AstraDB Configuration
ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
ASTRA_DB_KEYSPACE=optional_keyspace_name
```

### 6. Run the Agent

```bash
python main.py
```

## Configuration Notes

- Obtain an OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
- Generate a GitHub Personal Access Token from [GitHub Developer Settings](https://github.com/settings/tokens)
- Create a free AstraDB account at [DataStax Astra](https://astra.datastax.com/)

## Security Recommendations

- Never commit your `.env` file to version control
- Use environment-specific configurations
- Rotate API tokens periodically

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

