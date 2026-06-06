#!/usr/bin/env python3
"""
OpenClaw AI Trading Agent — Main Entry Point
=============================================

This is the main entry point for the OpenClaw AI Trading Agent.
It orchestrates the 3-module architecture (Perception → Reasoning → Action)
and connects to the Python ICT Dashboard V2 for signal generation.

Usage:
    python run_agent.py                    # Paper trading mode (default)
    python run_agent.py --mode live        # Live trading (not yet enabled)
    python run_agent.py --config custom.yaml

Author: Saba Yip (yipsaba@polyu-msc.ai)
Programme: PolyU MSc Digital Economics
"""

import argparse
import logging
import sys
import time
from pathlib import Path

import yaml
from dotenv import load_dotenv


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Configure logging for the agent."""
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
        handlers=[
            logging.FileHandler('agent.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger('OpenClaw')


def load_config(config_path: str = "config/agent_config.yaml") -> dict:
    """Load agent configuration from YAML."""
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='OpenClaw AI Trading Agent')
    parser.add_argument(
        '--mode',
        choices=['paper_trading', 'live_trading'],
        default='paper_trading',
        help='Trading mode (default: paper_trading)'
    )
    parser.add_argument(
        '--config',
        default='config/agent_config.yaml',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Logging level'
    )
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    
    # Setup logging
    logger = setup_logging(args.log_level)
    logger.info("=" * 60)
    logger.info("OpenClaw AI Trading Agent — Starting Up")
    logger.info("=" * 60)
    
    # Load configuration
    try:
        config = load_config(args.config)
        logger.info(f"Configuration loaded: {args.config}")
    except FileNotFoundError as e:
        logger.error(f"Failed to load config: {e}")
        sys.exit(1)
    
    # Set trading mode
    config['agent']['mode'] = args.mode
    logger.info(f"Trading mode: {args.mode}")
    
    # TODO: Initialize 3 modules
    # from skills.process_ict_signals import ProcessICTSignals
    # from skills.evaluate_signals import EvaluateSignals
    # from skills.execute_paper_trade import ExecutePaperTrade
    # from skills.fetch_market_data import FetchMarketData
    #
    # perception = ProcessICTSignals(config, logger)
    # reasoning = EvaluateSignals(config, logger)
    # action = ExecutePaperTrade(config, logger)
    # data = FetchMarketData(config, logger)
    
    logger.info("✅ Agent initialised successfully")
    logger.info("📡 Waiting for ICT signals from Python ICT Dashboard V2...")
    logger.info("=" * 60)
    
    # Main loop (placeholder)
    try:
        while True:
            # TODO: Main agent loop
            # 1. Check signals_json/ for new signals
            # 2. Reasoning module validates signals
            # 3. Action module executes paper trades
            # 4. Log to execution_logs/
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Agent stopped by user")


if __name__ == "__main__":
    main()
