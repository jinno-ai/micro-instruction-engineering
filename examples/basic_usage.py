"""
Basic Usage Example

Demonstrates micro-instruction engineering concepts.
"""

from src.templates.prompt_template import MicroInstructionEngine, PromptTemplate
from src.evaluation.prompt_evaluator import PromptEvaluator


def main():
    # Create engine
    engine = MicroInstructionEngine()
    
    # Example 1: Chain of Thought
    task = "Calculate the total cost of 3 apples at $2 each and 2 oranges at $3 each"
    steps = [
        "Calculate cost of apples: 3 × $2",
        "Calculate cost of oranges: 2 × $3",
        "Add both costs together"
    ]
    
    cot_prompt = engine.create_chain_of_thought_prompt(task, steps)
    print("Chain of Thought Prompt:")
    print(cot_prompt)
    print("\n" + "="*60 + "\n")
    
    # Example 2: Few-Shot Learning
    examples = [
        {"input": "2 + 2", "output": "4"},
        {"input": "5 × 3", "output": "15"},
    ]
    
    few_shot_prompt = engine.create_few_shot_prompt(
        task="Solve the math problem",
        examples=examples,
        query="7 + 3"
    )
    print("Few-Shot Prompt:")
    print(few_shot_prompt)
    print("\n" + "="*60 + "\n")
    
    # Example 3: Instruction Decomposition
    complex_instruction = "Write a report analyzing sales data"
    micro_instructions = engine.decompose_instruction(complex_instruction)
    print("Micro-Instructions:")
    for i, instruction in enumerate(micro_instructions, 1):
        print(f"{i}. {instruction}")
    print("\n" + "="*60 + "\n")
    
    # Example 4: Prompt Evaluation
    evaluator = PromptEvaluator()
    
    test_prompt = "Calculate the sum of 2 and 3"
    test_response = "The sum of 2 and 3 is 5"
    
    result = evaluator.evaluate(test_prompt, test_response)
    print("Evaluation Result:")
    print(f"Score: {result.score:.2f}")
    print(f"Metrics: {result.metrics}")
    print(f"Feedback: {result.feedback}")


if __name__ == "__main__":
    main()
