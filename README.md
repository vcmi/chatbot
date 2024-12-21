# VCMI chatbot

GPT prompt and knowledge base used by VCMI chatbot:
https://chatgpt.com/g/g-1kNhX0mlO-vcmi-assistant

The list of actual knowledge base files is in `knowledgeFiles.yaml`. They need to be directly uploaded to GPT Chatbot settings, ask Warmonger to do it if neccessary.

### Dependencies

`pip install dotenv`

### Extract Knowledge Base from VCMI source code

1. Set `VCMI_PATH` environment variable to your VCMI source code folder. Use `.env` file to set it.

2. Run script to extract knowledge base:

`cd knowledge_base/tools && python concat.py`
