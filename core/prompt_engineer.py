
from string import Template

class PromptEngineer:
    def __init__(self, templates):
        self.templates = templates

    def build_prompt(self, template_name, contexts):
        template_str = self.templates.get(template_name)
        if not template_str:
            raise ValueError(f"Template '{template_name}' not found.")

        prompt = [
            {"role": "system", "content": template_str},
        ]

        for context in contexts:
            prompt.append({"role": "user", "content": context["user"]})
            prompt.append({"role": "assistant", "content": context["assistant"]})

        return prompt
