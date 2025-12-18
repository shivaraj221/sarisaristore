# main/core/utils.py - SIMPLIFIED WORKING VERSION
import os
import json
import re
from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SentimentState(TypedDict):
    feedback_text: str
    sentiment: str
    confidence: float
    reasoning: str
    error: str
    analysis_complete: bool

class EnhancedFeedbackAnalyzer:
    def __init__(self):
        self.cache = {}
        self.setup_negation_patterns()
    
    def setup_negation_patterns(self):
        """Define negation patterns for sentiment analysis"""
        self.negation_patterns = [
            (r'\bnot\s+(?:so\s+)?good\b', "NEGATIVE", 0.95),
            (r'\bnot\s+(?:so\s+)?great\b', "NEGATIVE", 0.95),
            (r'\bnot\s+(?:so\s+)?excellent\b', "NEGATIVE", 0.95),
            (r'\bnot\s+(?:so\s+)?nice\b', "NEGATIVE", 0.9),
            (r'\bno\s+good\b', "NEGATIVE", 0.96),
            (r'\bnever\s+(?:so\s+)?good\b', "NEGATIVE", 0.96),
            (r'\bnot\s+(?:that\s+)?bad\b', "POSITIVE", 0.85),  # "not bad" is positive
            (r'\bnot\s+(?:too\s+)?bad\b', "POSITIVE", 0.85),   # "not too bad" is positive
        ]
        
        # Positive and negative keywords with weights
        self.positive_keywords = {
            'good': 0.7, 'great': 0.8, 'excellent': 0.9, 'awesome': 0.85,
            'love': 0.9, 'perfect': 0.95, 'best': 0.85, 'happy': 0.8,
            'nice': 0.6, 'fine': 0.5, 'okay': 0.4, 'satisfied': 0.7,
            'recommend': 0.8, 'excited': 0.8, 'pleased': 0.7
        }
        
        self.negative_keywords = {
            'bad': 0.7, 'terrible': 0.9, 'awful': 0.9, 'horrible': 0.9,
            'worst': 0.95, 'hate': 0.9, 'poor': 0.7, 'useless': 0.8,
            'disappointed': 0.8, 'waste': 0.75, 'broken': 0.8,
            'awful': 0.9, 'terrible': 0.9, 'horrible': 0.9
        }
    
    # ==================== LANGGRAPH NODES ====================
    
    def preprocess_node(self, state: SentimentState) -> SentimentState:
        """Node 1: Preprocess the feedback text"""
        try:
            text = state["feedback_text"].strip()
            
            # Basic cleaning
            text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
            text = text[:1000]  # Limit length
            
            # Detect features
            has_negation = bool(re.search(r'\bnot\s+\w+', text.lower()))
            has_exclamation = '!' in text
            has_question = '?' in text
            
            logger.info(f"Preprocessing: {text[:50]}...")
            
            return {
                **state,
                "feedback_text": text,
                "analysis_complete": False,
                "error": ""
            }
        except Exception as e:
            return {
                **state,
                "error": f"Preprocessing error: {str(e)}"
            }
    
    def pattern_analysis_node(self, state: SentimentState) -> SentimentState:
        """Node 2: Check for common patterns and negation"""
        if state.get("error"):
            return state
            
        try:
            text = state["feedback_text"].lower()
            
            # First, check for strong negation patterns
            for pattern, sentiment, confidence in self.negation_patterns:
                if re.search(pattern, text):
                    logger.info(f"Matched pattern: {pattern} → {sentiment}")
                    return {
                        **state,
                        "sentiment": sentiment,
                        "confidence": confidence,
                        "reasoning": f"Matched negation pattern: '{pattern}'",
                        "analysis_complete": True
                    }
            
            # Check for very clear positive/negative phrases
            positive_phrases = [
                r'\blove\s+it\b', r'\bvery\s+good\b', r'\bexcellent\b', 
                r'\bperfect\b', r'\bawesome\b'
            ]
            
            negative_phrases = [
                r'\bhate\s+it\b', r'\bvery\s+bad\b', r'\bterrible\b',
                r'\bawful\b', r'\bhorrible\b'
            ]
            
            for phrase in positive_phrases:
                if re.search(phrase, text):
                    return {
                        **state,
                        "sentiment": "POSITIVE",
                        "confidence": 0.9,
                        "reasoning": f"Matched positive phrase: '{phrase}'",
                        "analysis_complete": True
                    }
            
            for phrase in negative_phrases:
                if re.search(phrase, text):
                    return {
                        **state,
                        "sentiment": "NEGATIVE",
                        "confidence": 0.9,
                        "reasoning": f"Matched negative phrase: '{phrase}'",
                        "analysis_complete": True
                    }
            
            # If no strong patterns found, continue to next node
            return state
            
        except Exception as e:
            return {
                **state,
                "error": f"Pattern analysis error: {str(e)}"
            }
    
    def keyword_analysis_node(self, state: SentimentState) -> SentimentState:
        """Node 3: Perform keyword-based analysis"""
        if state.get("error") or state.get("analysis_complete"):
            return state
            
        try:
            text = state["feedback_text"].lower()
            
            # Calculate weighted scores
            pos_score = 0
            neg_score = 0
            
            # Check positive keywords
            for keyword, weight in self.positive_keywords.items():
                if re.search(rf'\b{keyword}\b', text):
                    pos_score += weight
                    logger.debug(f"Found positive: {keyword} (+{weight})")
            
            # Check negative keywords
            for keyword, weight in self.negative_keywords.items():
                if re.search(rf'\b{keyword}\b', text):
                    neg_score += weight
                    logger.debug(f"Found negative: {keyword} (+{weight})")
            
            # Determine sentiment
            if pos_score > neg_score and pos_score > 0:
                sentiment = "POSITIVE"
                confidence = min(0.85, pos_score / (pos_score + neg_score + 0.1))
            elif neg_score > pos_score and neg_score > 0:
                sentiment = "NEGATIVE"
                confidence = min(0.85, neg_score / (pos_score + neg_score + 0.1))
            else:
                sentiment = "NEUTRAL"
                confidence = 0.5
            
            # Apply negation override
            if "not " in text:
                if sentiment == "POSITIVE":
                    sentiment = "NEGATIVE"
                    confidence = max(confidence, 0.7)
                elif sentiment == "NEUTRAL" and (pos_score > 0 or neg_score > 0):
                    sentiment = "NEGATIVE"
                    confidence = 0.6
            
            reasoning = f"Keyword analysis: positive score={pos_score:.2f}, negative score={neg_score:.2f}"
            
            logger.info(f"Keyword analysis: {sentiment} ({confidence:.2f})")
            
            return {
                **state,
                "sentiment": sentiment,
                "confidence": round(confidence, 2),
                "reasoning": reasoning,
                "analysis_complete": True
            }
            
        except Exception as e:
            return {
                **state,
                "error": f"Keyword analysis error: {str(e)}"
            }
    
    def finalize_node(self, state: SentimentState) -> SentimentState:
        """Node 4: Final validation and cleanup"""
        try:
            # If there was an error, provide default response
            if state.get("error"):
                return {
                    **state,
                    "sentiment": "NEUTRAL",
                    "confidence": 0.5,
                    "reasoning": f"Analysis failed: {state['error']}",
                    "analysis_complete": True
                }
            
            # Ensure we have a result
            if not state.get("analysis_complete"):
                return {
                    **state,
                    "sentiment": "NEUTRAL",
                    "confidence": 0.5,
                    "reasoning": "Analysis could not determine sentiment",
                    "analysis_complete": True
                }
            
            # Add timestamp and clean up
            result = {
                "sentiment": state["sentiment"],
                "confidence": state["confidence"],
                "reasoning": state["reasoning"],
                "original_text": state["feedback_text"],
                "analysis_complete": True,
                "error": ""
            }
            
            logger.info(f"Final result: {result['sentiment']} ({result['confidence']:.2f})")
            return result
            
        except Exception as e:
            return {
                "sentiment": "NEUTRAL",
                "confidence": 0.5,
                "reasoning": f"Finalization error: {str(e)}",
                "analysis_complete": True,
                "error": str(e)
            }
    
    # ==================== WORKFLOW CREATION ====================
    
    def create_workflow(self) -> StateGraph:
        """Create the LangGraph workflow"""
        # Define the workflow
        workflow = StateGraph(SentimentState)
        
        # Add nodes
        workflow.add_node("preprocess", self.preprocess_node)
        workflow.add_node("pattern_analysis", self.pattern_analysis_node)
        workflow.add_node("keyword_analysis", self.keyword_analysis_node)
        workflow.add_node("finalize", self.finalize_node)
        
        # Set entry point
        workflow.set_entry_point("preprocess")
        
        # Define edges
        workflow.add_edge("preprocess", "pattern_analysis")
        
        # Conditional edge: If pattern analysis found something, go to finalize
        # Otherwise, continue to keyword analysis
        workflow.add_conditional_edges(
            "pattern_analysis",
            lambda state: "finalize" if state.get("analysis_complete") else "keyword_analysis"
        )
        
        workflow.add_edge("keyword_analysis", "finalize")
        workflow.add_edge("finalize", END)
        
        return workflow
    
    def analyze_feedback(self, feedback_text: str) -> Dict:
        """Main analysis function"""
        try:
            # Create workflow
            workflow = self.create_workflow()
            
            # Compile
            app = workflow.compile()
            
            # Initial state
            initial_state = {
                "feedback_text": feedback_text,
                "sentiment": "",
                "confidence": 0.0,
                "reasoning": "",
                "error": "",
                "analysis_complete": False
            }
            
            # Execute workflow
            result = app.invoke(initial_state)
            
            # Return clean result
            return {
                "sentiment": result.get("sentiment", "NEUTRAL"),
                "confidence": result.get("confidence", 0.5),
                "reasoning": result.get("reasoning", "Analysis completed"),
                "success": not result.get("error", ""),
                "error": result.get("error", "")
            }
            
        except Exception as e:
            logger.error(f"Workflow execution failed: {e}")
            return {
                "sentiment": "NEUTRAL",
                "confidence": 0.5,
                "reasoning": f"Workflow failed: {str(e)}",
                "success": False,
                "error": str(e)
            }
    
    # ==================== LLM ANALYSIS (OPTIONAL) ====================
    
    def analyze_with_llm(self, feedback_text: str) -> Dict:
        """Optional LLM-based analysis for complex cases"""
        try:
            from openai import OpenAI
            
            # Initialize client
            client = OpenAI(
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
            
            prompt = f"""Analyze this feedback sentiment:

"{feedback_text}"

Return ONLY a JSON object with this exact format:
{{
    "sentiment": "POSITIVE", "NEGATIVE", or "NEUTRAL",
    "confidence": 0.0 to 1.0,
    "reasoning": "Brief explanation"
}}"""

            response = client.chat.completions.create(
                model="qwen/qwen-2.5-32b-instruct:free",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=200
            )
            
            content = response.choices[0].message.content.strip()
            
            # Extract JSON
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                content = json_match.group(0)
            
            result = json.loads(content)
            
            return {
                "sentiment": result.get("sentiment", "NEUTRAL").upper(),
                "confidence": min(1.0, max(0.0, float(result.get("confidence", 0.5)))),
                "reasoning": result.get("reasoning", "LLM analysis"),
                "success": True,
                "source": "llm"
            }
            
        except Exception as e:
            logger.error(f"LLM analysis failed: {e}")
            # Fall back to regular analysis
            return self.analyze_feedback(feedback_text)


# ==================== MAIN FUNCTION ====================

def analyze_feedback_sentiment(feedback_text: str, use_llm: bool = False) -> dict:
    """
    Main function to analyze feedback sentiment
    
    Args:
        feedback_text: The feedback text to analyze
        use_llm: Whether to use LLM (OpenRouter) for analysis
    
    Returns:
        Dictionary with sentiment analysis results
    """
    try:
        analyzer = EnhancedFeedbackAnalyzer()
        
        if use_llm and os.getenv("OPENROUTER_API_KEY"):
            logger.info("Using LLM analysis")
            return analyzer.analyze_with_llm(feedback_text)
        else:
            logger.info("Using rule-based analysis")
            return analyzer.analyze_feedback(feedback_text)
            
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        return {
            "sentiment": "NEUTRAL",
            "confidence": 0.5,
            "reasoning": f"Analysis failed: {str(e)}",
            "success": False,
            "error": str(e)
        }


# ==================== QUICK TEST FUNCTION ====================

def test_analysis():
    """Test the sentiment analysis with sample feedback"""
    test_cases = [
        "The product is very good",
        "The product is not good at all",
        "I love this store!",
        "This is terrible, never buying again",
        "It's okay, nothing special",
        "Not bad for the price",
        "Waste of money, completely useless"
    ]
    
    analyzer = EnhancedFeedbackAnalyzer()
    
    print("🧪 Testing Sentiment Analysis\n")
    print("=" * 60)
    
    for feedback in test_cases:
        result = analyzer.analyze_feedback(feedback)
        print(f"📝 Feedback: {feedback}")
        print(f"   Sentiment: {result['sentiment']}")
        print(f"   Confidence: {result['confidence']:.2f}")
        print(f"   Reasoning: {result['reasoning']}")
        print("-" * 60)


if __name__ == "__main__":
    # Run tests
    test_analysis()