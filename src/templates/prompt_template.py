"""
Prompt Template System

Systematic prompt engineering and optimization.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import json


@dataclass
class PromptTemplate:
    """Structured prompt template"""
    name: str
    description: str
    template: str
    variables: List[str]
    examples: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    
    def format(self, **kwargs) -> str:
        """Format template with variables"""
        return self.template.format(**kwargs)
    
    def validate(self, **kwargs) -> bool:
        """Validate that all required variables are provided"""
        return all(var in kwargs for var in self.variables)


class MicroInstructionEngine:
    """Engine for micro-instruction prompt engineering"""
    
    def __init__(self):
        self.templates = {}
        self.optimizations = []
    
    def register_template(self, template: PromptTemplate) -> None:
        """Register a prompt template"""
        self.templates[template.name] = template
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Get template by name"""
        return self.templates.get(name)
    
    def create_chain_of_thought_prompt(self, task: str, steps: List[str]) -> str:
        """Create chain-of-thought prompt"""
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])
        
        prompt = f"""Task: {task}

Let's break this down step by step:

{steps_text}

Now, let's work through each step:
"""
        return prompt
    
    def create_few_shot_prompt(self, task: str, examples: List[Dict[str, str]], query: str) -> str:
        """Create few-shot learning prompt"""
        examples_text = "\n\n".join([
            f"Input: {ex['input']}\nOutput: {ex['output']}"
            for ex in examples
        ])
        
        prompt = f"""Task: {task}

Here are some examples:

{examples_text}

Now, solve this:
Input: {query}
Output:"""
        return prompt
    
    def decompose_instruction(self, instruction: str) -> List[str]:
        """Decompose complex instruction into micro-instructions"""
        # Simple decomposition (can be enhanced with LLM)
        micro_instructions = [
            "Understand the main task",
            "Identify required information",
            "Break down into sub-tasks",
            "Execute each sub-task",
            "Combine results",
            "Verify output"
        ]
        return micro_instructions
    
    def optimize_prompt(self, prompt: str, feedback: str) -> str:
        """Optimize prompt based on feedback"""
        optimization = {
            'original': prompt,
            'feedback': feedback,
            'optimized': prompt  # Placeholder
        }
        self.optimizations.append(optimization)
        return prompt
