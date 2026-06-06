"""
Evaluate Signals
=================

Apply ICT trading rules to determine if a signal is valid and should
trigger a trade.
"""

import logging
from typing import Dict, List


logger = logging.getLogger('OpenClaw.skills.evaluate_signals')


class EvaluateSignals:
    """Evaluate ICT signals against trading rules."""
    
    def __init__(self, config: dict):
        self.config = config
        self.min_rr_ratio = config.get('reasoning', {}).get('entry_conditions', {}).get('min_risk_reward', 2.0)
    
    def evaluate(self, signal: Dict) -> Dict:
        """Evaluate a signal and return trade decision.
        
        Args:
            signal: ICT signal dictionary
        
        Returns:
            Decision dictionary with VALID/INVALID + reasoning
        """
        decision = {
            'signal_id': signal.get('signal_id'),
            'decision': 'INVALID',
            'reasoning': [],
            'entry_price': None,
            'stop_loss': None,
            'take_profit': [],
            'risk_reward_ratio': None
        }
        
        # 1. Check signal type
        if signal.get('type') not in ['FVG', 'OB', 'LIQUIDITY_SWEEP']:
            decision['reasoning'].append(f"Unsupported signal type: {signal.get('type')}")
            return decision
        
        # 2. Check FVG + OB confluence (if both present)
        # (This would require checking other recent signals)
        
        # 3. Check HTF context
        htf_context = signal.get('htf_context', 'neutral')
        if signal.get('direction') == 'bullish' and htf_context != 'discount':
            decision['reasoning'].append(f"Bullish signal but HTF context is {htf_context}, not discount")
            return decision
        
        # 4. Calculate entry, SL, TP
        midpoint = signal.get('midpoint')
        if midpoint is None:
            decision['reasoning'].append("Missing midpoint for entry price")
            return decision
        
        decision['entry_price'] = midpoint
        
        # Simplified SL/TP (1.5 ATR away for SL, 2R for TP)
        # In production, would use actual ATR and OB levels
        decision['stop_loss'] = midpoint * 0.97  # 3% below
        decision['take_profit'] = [midpoint * 1.03, midpoint * 1.06, midpoint * 1.09]  # 3%, 6%, 9%
        
        # 5. Calculate R:R ratio
        risk = abs(decision['entry_price'] - decision['stop_loss'])
        reward = abs(decision['take_profit'][1] - decision['entry_price'])
        rr = reward / risk if risk > 0 else 0
        decision['risk_reward_ratio'] = round(rr, 2)
        
        # 6. Validate R:R
        if rr < self.min_rr_ratio:
            decision['reasoning'].append(f"R:R ratio {rr} < minimum {self.min_rr_ratio}")
            return decision
        
        # All checks passed
        decision['decision'] = 'VALID'
        decision['reasoning'].append("All ICT rules passed")
        decision['reasoning'].append(f"R:R ratio: {rr}")
        
        return decision


# Example usage
if __name__ == '__main__':
    config = {
        'reasoning': {
            'entry_conditions': {
                'min_risk_reward': 2.0
            }
        }
    }
    
    evaluator = EvaluateSignals(config)
    
    # Test signal
    signal = {
        'signal_id': 'test_001',
        'type': 'FVG',
        'direction': 'bullish',
        'trading_pair': 'BTC-USD',
        'timeframe': '15m',
        'midpoint': 68350.25,
        'htf_context': 'discount'
    }
    
    decision = evaluator.evaluate(signal)
    print(f"Decision: {decision['decision']}")
    print(f"Reasoning: {decision['reasoning']}")
