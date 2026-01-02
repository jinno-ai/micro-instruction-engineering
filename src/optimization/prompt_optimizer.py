"""
Prompt Optimization System

Systematic optimization of prompts using various techniques.
"""

from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
import json


@dataclass
class OptimizationResult:
    """Result of prompt optimization"""
    original_prompt: str
    optimized_prompt: str
    improvement_score: float
    techniques_applied: List[str]
    iterations: int


class PromptOptimizer:
    """
    Systematic prompt optimization using multiple techniques.
    
    Techniques:
    - Chain-of-thought decomposition
    - Few-shot example selection
    - Instruction clarification
    - Output format specification
    - Constraint addition
    """
    
    def __init__(self, llm: Any = None):
        self.llm = llm
        self.optimization_history: List[OptimizationResult] = []
    
    def optimize(
        self,
        prompt: str,
        task_type: str = "general",
        target_improvement: float = 0.2,
        max_iterations: int = 5
    ) -> OptimizationResult:
        """
        Optimize a prompt for better performance.
        
        Args:
            prompt: Original prompt
            task_type: Type of task (general, coding, analysis, creative)
            target_improvement: Target improvement score
            max_iterations: Maximum optimization iterations
            
        Returns:
            OptimizationResult with optimized prompt
        """
        current_prompt = prompt
        techniques_applied = []
        
        for iteration in range(max_iterations):
            # Apply optimization techniques based on task type
            if task_type == "coding":
                current_prompt = self._optimize_for_coding(current_prompt)
                techniques_applied.append("coding_optimization")
            
            elif task_type == "analysis":
                current_prompt = self._optimize_for_analysis(current_prompt)
                techniques_applied.append("analysis_optimization")
            
            elif task_type == "creative":
                current_prompt = self._optimize_for_creative(current_prompt)
                techniques_applied.append("creative_optimization")
            
            else:
                current_prompt = self._optimize_general(current_prompt)
                techniques_applied.append("general_optimization")
            
            # Add chain-of-thought if not present
            if "step by step" not in current_prompt.lower():
                current_prompt = self._add_chain_of_thought(current_prompt)
                techniques_applied.append("chain_of_thought")
            
            # Add output format if not specified
            if not self._has_output_format(current_prompt):
                current_prompt = self._add_output_format(current_prompt, task_type)
                techniques_applied.append("output_format")
        
        # Calculate improvement score
        improvement_score = self._calculate_improvement(prompt, current_prompt)
        
        result = OptimizationResult(
            original_prompt=prompt,
            optimized_prompt=current_prompt,
            improvement_score=improvement_score,
            techniques_applied=list(set(techniques_applied)),
            iterations=max_iterations
        )
        
        self.optimization_history.append(result)
        return result
    
    def _optimize_general(self, prompt: str) -> str:
        """Apply general optimization techniques"""
        optimized = prompt
        
        # Add role specification if not present
        if not any(word in prompt.lower() for word in ['you are', 'act as', 'as a']):
            optimized = f"You are a helpful AI assistant.\n\n{optimized}"
        
        # Add clarity instructions
        if "clear" not in prompt.lower() and "concise" not in prompt.lower():
            optimized += "\n\nProvide a clear and concise response."
        
        return optimized
    
    def _optimize_for_coding(self, prompt: str) -> str:
        """Optimize prompt for coding tasks"""
        additions = []
        
        # Add code quality instructions
        if "comment" not in prompt.lower():
            additions.append("Include comments explaining the code.")
        
        if "error" not in prompt.lower():
            additions.append("Handle potential errors appropriately.")
        
        if "example" not in prompt.lower():
            additions.append("Provide usage examples.")
        
        if additions:
            prompt += "\n\nAdditional requirements:\n" + "\n".join(f"- {a}" for a in additions)
        
        return prompt
    
    def _optimize_for_analysis(self, prompt: str) -> str:
        """Optimize prompt for analysis tasks"""
        additions = []
        
        if "evidence" not in prompt.lower():
            additions.append("Support your analysis with evidence.")
        
        if "consider" not in prompt.lower():
            additions.append("Consider multiple perspectives.")
        
        if "conclusion" not in prompt.lower():
            additions.append("Provide a clear conclusion.")
        
        if additions:
            prompt += "\n\nAnalysis guidelines:\n" + "\n".join(f"- {a}" for a in additions)
        
        return prompt
    
    def _optimize_for_creative(self, prompt: str) -> str:
        """Optimize prompt for creative tasks"""
        additions = []
        
        if "original" not in prompt.lower():
            additions.append("Be original and creative.")
        
        if "engaging" not in prompt.lower():
            additions.append("Make the content engaging.")
        
        if additions:
            prompt += "\n\nCreative guidelines:\n" + "\n".join(f"- {a}" for a in additions)
        
        return prompt
    
    def _add_chain_of_thought(self, prompt: str) -> str:
        """Add chain-of-thought instruction"""
        return prompt + "\n\nThink through this step by step."
    
    def _has_output_format(self, prompt: str) -> bool:
        """Check if prompt specifies output format"""
        format_indicators = [
            'format:', 'output:', 'respond with', 'return',
            'json', 'markdown', 'bullet', 'numbered'
        ]
        return any(indicator in prompt.lower() for indicator in format_indicators)
    
    def _add_output_format(self, prompt: str, task_type: str) -> str:
        """Add appropriate output format specification"""
        formats = {
            "coding": "\n\nProvide your response as:\n1. Code block with the solution\n2. Brief explanation\n3. Usage example",
            "analysis": "\n\nStructure your response as:\n1. Summary\n2. Key findings\n3. Detailed analysis\n4. Conclusion",
            "creative": "\n\nFormat your response appropriately for the creative content.",
            "general": "\n\nProvide a well-structured response."
        }
        return prompt + formats.get(task_type, formats["general"])
    
    def _calculate_improvement(self, original: str, optimized: str) -> float:
        """Calculate improvement score"""
        # Simple heuristic based on added structure
        score = 0.0
        
        # Check for added structure
        if len(optimized) > len(original):
            score += 0.1
        
        # Check for chain-of-thought
        if "step by step" in optimized.lower() and "step by step" not in original.lower():
            score += 0.2
        
        # Check for output format
        if self._has_output_format(optimized) and not self._has_output_format(original):
            score += 0.2
        
        # Check for role specification
        if "you are" in optimized.lower() and "you are" not in original.lower():
            score += 0.1
        
        return min(score, 1.0)


class MicroInstructionDecomposer:
    """
    Decompose complex instructions into micro-instructions.
    
    This improves LLM performance by breaking down complex tasks
    into smaller, more manageable steps.
    """
    
    def __init__(self):
        self.decomposition_patterns = {
            "analyze": ["identify key elements", "examine relationships", "evaluate significance", "draw conclusions"],
            "create": ["understand requirements", "plan structure", "generate content", "refine output"],
            "compare": ["identify items to compare", "list characteristics", "find similarities", "find differences", "summarize comparison"],
            "explain": ["identify the concept", "break into components", "provide examples", "summarize"],
            "solve": ["understand the problem", "identify constraints", "explore solutions", "implement solution", "verify result"]
        }
    
    def decompose(self, instruction: str) -> List[str]:
        """
        Decompose a complex instruction into micro-instructions.
        
        Args:
            instruction: Complex instruction
            
        Returns:
            List of micro-instructions
        """
        instruction_lower = instruction.lower()
        
        # Find matching pattern
        for keyword, steps in self.decomposition_patterns.items():
            if keyword in instruction_lower:
                return self._apply_pattern(instruction, steps)
        
        # Default decomposition
        return self._default_decomposition(instruction)
    
    def _apply_pattern(self, instruction: str, pattern_steps: List[str]) -> List[str]:
        """Apply a decomposition pattern"""
        micro_instructions = []
        
        for i, step in enumerate(pattern_steps, 1):
            micro_instructions.append(f"Step {i}: {step.capitalize()}")
        
        return micro_instructions
    
    def _default_decomposition(self, instruction: str) -> List[str]:
        """Default decomposition for unmatched instructions"""
        return [
            "Step 1: Understand the task requirements",
            "Step 2: Identify key information needed",
            "Step 3: Process the information systematically",
            "Step 4: Generate the response",
            "Step 5: Review and refine the output"
        ]
    
    def create_decomposed_prompt(self, instruction: str) -> str:
        """
        Create a prompt with decomposed instructions.
        
        Args:
            instruction: Original instruction
            
        Returns:
            Prompt with micro-instructions
        """
        micro_instructions = self.decompose(instruction)
        
        prompt = f"""Task: {instruction}

Let's approach this systematically:

{chr(10).join(micro_instructions)}

Now, work through each step:
"""
        return prompt
