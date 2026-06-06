"""
OpenClaw AI Trading Agent — Core Utilities
"""


def format_signal(signal: dict) -> str:
    """Format ICT signal for logging."""
    return (
        f"[{signal.get('signal_id')}] "
        f"{signal.get('type')} | {signal.get('trading_pair')} | "
        f"{signal.get('direction').upper()} | "
        f"Entry: {signal.get('midpoint')}"
    )


def calculate_position_size(portfolio: float, kelly_fraction: float, win_rate: float, rr_ratio: float) -> float:
    """Calculate position size using Kelly Criterion.
    
    Args:
        portfolio: Total portfolio value
        kelly_fraction: Fraction of Kelly to use (e.g., 0.25 for 1/4 Kelly)
        win_rate: Historical win rate (e.g., 0.64 for 64%)
        rr_ratio: Risk-reward ratio (e.g., 2.0)
    
    Returns:
        Position size in USD
    """
    if rr_ratio <= 0 or win_rate <= 0 or win_rate >= 1:
        return 0
    
    # Kelly formula: f* = (p * b - q) / b
    # where p = win rate, q = 1 - win rate, b = rr ratio
    kelly_pct = (win_rate * rr_ratio - (1 - win_rate)) / rr_ratio
    
    # Apply fractional Kelly
    fractional_kelly = kelly_pct * kelly_fraction
    
    # Cap at 10% of portfolio
    position_pct = min(fractional_kelly, 0.10)
    position_pct = max(position_pct, 0)  # No negative positions
    
    return portfolio * position_pct


def calculate_atr(highs: list, lows: list, closes: list, period: int = 14) -> float:
    """Calculate Average True Range (ATR).
    
    Args:
        highs: List of high prices
        lows: List of low prices
        closes: List of close prices
        period: ATR period (default 14)
    
    Returns:
        ATR value
    """
    if len(closes) < period + 1:
        return 0
    
    true_ranges = []
    for i in range(1, len(closes)):
        high_low = highs[i] - lows[i]
        high_close_prev = abs(highs[i] - closes[i-1])
        low_close_prev = abs(lows[i] - closes[i-1])
        true_range = max(high_low, high_close_prev, low_close_prev)
        true_ranges.append(true_range)
    
    # Simple moving average of true ranges
    if len(true_ranges) < period:
        return sum(true_ranges) / len(true_ranges)
    
    return sum(true_ranges[-period:]) / period
