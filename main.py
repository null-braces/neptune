from prompts.templates import TEMPLATES
from core.prompt_engineer import PromptEngineer
from core.context import ContextManager
from core.llm_client import LLMClient
from core.response_handler import ResponseHandler

# Instantiate components
prompt_engineer = PromptEngineer(TEMPLATES)
context_manager = ContextManager()
llm_client = LLMClient()
response_handler = ResponseHandler()

# Sample interaction
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    context = context_manager.get_context()
    prompt = prompt_engineer.build_prompt("qa_bot", context)
    prompt.append({"role": "user", "content": user_input})

    print("Prompt:", prompt)

    raw_response = llm_client.chat(prompt)
    cleaned_response = response_handler.sanitize(raw_response)

    print("Assistant:", cleaned_response)
    context_manager.add_turn(user_input, cleaned_response)
