# RetroTrade: A Quantitative Trading Strategy Backtester

RetroTrade is a high-performance, command-line backtesting engine designed for the systematic development, testing, and optimization of quantitative trading strategies. Built with a modular and extensible architecture in Java, it provides a robust framework for evaluating strategy performance against historical end-of-day market data.

## Core Features

This engine is built to support a rigorous quantitative research workflow:

*   **Extensible Strategy Interface:** At its core is a `TradingStrategy` interface, allowing for the rapid implementation and testing of new alpha signals and trading logic without altering the engine itself.
*   **Automated Data Caching:** Fetches historical data from financial APIs and intelligently caches it locally in CSV format. Subsequent runs on the same data range are read directly from disk, dramatically accelerating the testing cycle.
*   **Systematic Parameter Optimization:** Includes a brute-force optimizer to systematically iterate through a range of strategy parameters (e.g., moving average windows), identifying the most profitable configurations over the historical period.
*   **Performance Analytics:** Generates a clear performance report for each backtest, including a trade-by-trade log and key metrics like total return and win rate.
*   **Robust Command-Line Interface:** A clean, powerful CLI (powered by Picocli) serves as the primary interface, enabling easy integration into automated scripts and research workflows.

## System Architecture

The engine is designed with a clean separation of concerns, making it maintainable and easy to extend:

*   **`DataFetcher`:** Handles all interaction with external financial data APIs.
*   **`CsvReader` / `CsvWriter`:** Manages the local data cache, abstracting file I/O operations.
*   **`TradingStrategy` Interface:** The contract for all trading logic. This decouples the strategy from the backtesting execution.
*   **`BacktestEngine`:** The core orchestrator. It iterates through historical data, consults the provided strategy for signals, simulates trades, and calculates performance metrics.
*   **`CLI`:** The user-facing entry point that parses arguments and coordinates the workflow.

## Getting Started

### Prerequisites

*   Java JDK 11 or newer
*   Apache Maven
*   A valid API key from a supported financial data provider (e.g., Tiingo).

### Configuration

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/RetroTrade.git
    cd RetroTrade
    ```
2.  Create an environment file named `.env` in the root directory of the project.
3.  Add your API key to the `.env` file:
    ```
    API_TOKEN=your_api_key_here
    ```

### Building the Application

Compile the project and package it into an executable JAR file using Maven:

```bash
mvn clean package
```

This will create a JAR file in the `target/` directory (e.g., `RetroTrade-1.0-SNAPSHOT-jar-with-dependencies.jar`).

### Usage

All commands are run through the packaged JAR file.

**1. Fetch Data & Run a Backtest:**

The engine will automatically look for a local data file. If not found, it will fetch the data from the API and save it before running the backtest.

```bash
java -jar target/RetroTrade-1.0-SNAPSHOT-jar-with-dependencies.jar -s AAPL --start 2022-01-01 --end 2022-12-31
```

**2. Optimize Strategy Parameters:**

The application can also run an optimization loop to find the best-performing parameters for the built-in `MovingAverageStrategy`.

```bash
# This command will test hundreds of moving average combinations
java -jar target/RetroTrade-1.0-SNAPSHOT-jar-with-dependencies.jar -s MSFT --start 2021-01-01 --end 2022-12-31
```

## Extending the Engine: Implementing a Custom Strategy

The framework is designed for easy extension. To create a new strategy:

1.  Create a new class that implements the `TradingStrategy` interface.
2.  Implement the `shouldBuy()` and `shouldSell()` methods with your custom logic.
3.  Instantiate your new strategy class in the `CLI.java` `run()` method to test it.

**Example Strategy Template:**

```java
package com.nakul.retrotrade.strategy;

import com.nakul.retrotrade.Candle;
import java.util.List;

public class MyCustomRSIStrategy implements TradingStrategy {

    @Override
    public boolean shouldBuy(int index, List<Candle> history) {
        // Implement your buy logic here (e.g., RSI < 30)
        return false;
    }

    @Override
    public boolean shouldSell(int index, List<Candle> history) {
        // Implement your sell logic here (e.g., RSI > 70)
        return false;
    }
}
```

## Roadmap & Future Enhancements

This project provides a solid foundation for a more advanced system. Future development could include:

*   **Advanced Performance Metrics:** Implementing Sharpe Ratio, Sortino Ratio, Calmar Ratio, and detailed drawdown analysis.
*   **Portfolio-Level Backtesting:** Managing a portfolio of assets with capital allocation and risk management.
*   **LLM-Powered Signal Generation:** Integrating a Retrieval-Augmented Generation (RAG) model to process unstructured alternative data like financial news, SEC filings (10-K, 8-K), and earnings call transcripts. This would enable the development of sophisticated strategies that incorporate real-time sentiment and event-driven signals alongside traditional price/volume data.
*   **Event-Driven Architecture:** Refactoring to a more sophisticated event-driven model to handle market and signal events for greater realism and to support intraday backtesting.
*   **Support for More Asset Classes:** Adding support for Forex, futures, and options.
*   **Vectorized Backtesting:** Implementing a parallel vectorized backtester in Python/Pandas for significantly faster parameter optimization across large datasets.
