"""
Prompt Evaluation System

Evaluate and compare prompt effectiveness.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
import numpy as np


@dataclass
class EvaluationResult:
    """Result of prompt evaluation"""
    prompt: str
    score: float
    metrics: Dict[str, float]
    feedback: str


class PromptEvaluator:
    """Evaluate prompt quality and effectiveness"""
    
    def __init__(self):
        self.evaluation_history = []
    
    def evaluate(self, prompt: str, response: str, ground_truth: str = None) -> EvaluationResult:
        """Evaluate a prompt and its response"""
        metrics = {}
        
        # Length metric
        metrics['prompt_length'] = len(prompt)
        metrics['response_length'] = len(response)
        
        # Clarity score (simple heuristic)
        metrics['clarity'] = self._calculate_clarity(prompt)
        
        # Specificity score
        metrics['specificity'] = self._calculate_specificity(prompt)
        
        # If ground truth provided, calculate accuracy
        if ground_truth:
            metrics['similarity'] = self._calculate_similarity(response, ground_truth)
        
        # Overall score
        score = np.mean(list(metrics.values()))
        
        result = EvaluationResult(
            prompt=prompt,
            score=score,
            metrics=metrics,
            feedback=self._generate_feedback(metrics)
        )
        
        self.evaluation_history.append(result)
        return result
    
    def _calculate_clarity(self, text: str) -> float:
        """Calculate clarity score"""
        # Simple heuristic: shorter prompts with clear structure
        words = text.split()
        avg_word_length = np.mean([len(w) for w in words]) if words else 0
        
        # Prefer moderate word length (5-8 chars)
        clarity = 1.0 - abs(avg_word_length - 6.5) / 10.0
        return max(0, min(1, clarity))
    
    def _calculate_specificity(self, text: str) -> float:
        """Calculate specificity score"""
        # Count specific keywords
        specific_words = ['specific', 'exactly', 'must', 'should', 'requirement']
        count = sum(1 for word in specific_words if word in text.lower())
        return min(1.0, count / 3.0)
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate text similarity"""
        # Simple word overlap
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union)
    
    def _generate_feedback(self, metrics: Dict[str, float]) -> str:
        """Generate feedback based on metrics"""
        feedback = []
        
        if metrics['clarity'] < 0.5:
            feedback.append("Consider simplifying the prompt structure")
        
        if metrics['specificity'] < 0.5:
            feedback.append("Add more specific requirements")
        
        if not feedback:
            feedback.append("Prompt looks good!")
        
        return ". ".join(feedback)
    
    def compare_prompts(self, prompts: List[str], responses: List[str]) -> List[EvaluationResult]:
        """Compare multiple prompts"""
        results = []
        for prompt, response in zip(prompts, responses):
            result = self.evaluate(prompt, response)
            results.append(result)
        
        return sorted(results, key=lambda x: x.score, reverse=True)
