# RetroTrade: A Quantitative AI-Powered Trading Strategy Backtester

**RetroTrade is a high-performance backtesting engine fueled by a state-of-the-art RAG pipeline. It leverages local LLMs to derive trading signals from financial news, providing a powerful framework for developing and evaluating news-driven alpha strategies.**

![Java](https://img.shields.io/badge/Java-17+-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-29AAE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgdmlld0JveD0iMCAwIDI1NiAyNTYiPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNzIgMTI4YTQ0IDQ0IDAgMSAxLTQ0LTQ0YTQ0IDQ0IDAgMCAxIDQ0IDQ0Ii8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTg0IDEyOGE0NCA0NCAwIDEgMSA0NCA0NGE0NCA0NCAwIDAgMS00NC00NG0xMjggNDR2LTguNThhNjAgNjAgMCAwIDAtMjEuNDYtNDYuMDdsLTMuNjEtMy42MWExMiAxMiAwIDAgMC0xNi45NyAxNjk3bDMuNjEgMy42MUEzNiAzNiAwIDAgMSAxOTYgMTcyVjE2OGExMiAxMiAwIDEgMCAyNCAwbTI4LTEwMGE2MCA2MCAwIDAgMC01MS40Mi0yOS40OWbC0zLjYxLTMuNjFhMTIgMTIgMCAwIDAtMTYuOTggMTYuOTdsMy42MSAzLjYxQTM2IDM2IDAgMCAxIDE5NiA4NFY4MGExMiAxMiAwIDEgMCAyNCAwVjg0YTEyIDEyIDAgMCAwIDEyLTEyYTg0IDg0IDAgMCAwLTE2OCAwYTEyIDEyIDAgMCAwIDEyIDEydjRhMzYgMzYgMCAwIDEgMTUuNDYgMzAuNTFsMy42MSAzLjYxYTEyIDEyIDAgMSAwIDE2Ljk4LTE2Ljk4bC0zLjYxLTMuNjFBNjAgNjAgMCAwIDAgNjAgODRWODBhMTIgMTIgMCAxIDAtMjQgMHY0YTg0IDg0IDAgMCAwIDE2OCAwYTEyIDEyIDAgMSAwLTI0IDBaTTI4IDg0YTYwIDYwIDAgMCAwIDUxLjQyIDI5LjQ5bDMuNjEgMy42MWExMiAxMiAwIDEgMCAxNi45OC0xNi45N2wtMy42MS0zLjYxQTM2IDM2IDAgMCAxIDYwIDg0VjgwYTEyIDEyIDAgMSAwLTI0IDB2NGE4NCA4NCAwIDAgMCAwIDE2OGExMiAxMiAwIDEgMCAyNCAwdi00YTM2IDM2IDAgMCAxLTE1Ljk1LTMwLjkzbC0zLjYxLTMuNjFhMTIgMTIgMCAxIDAtMTYuOTggMTYuOTdsMy42MSAzLjYxQTYwIDYwIDAgMCAwIDYwIDE3MnY4YTEyIDEyIDAgMSAwIDI0IDB2LThhMzYgMzYgMCAwIDEgMjEuNDYtMzQuMDdsMy42MS0zLjYxYTEyIDEyIDAgMSAwLTE2Ljk3LTE2Ljk4bC0zLjYxIDMuNjFBNjAgNjAgMCAwIDAgODQgMTI4YTg0IDg0IDAgMCAwIDAtMTY4YTEyIDEyIDAgMSAwLTI0IDBaIi8+PC9zdmc+)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)

## Key Features & Architecture

-   **AI-Powered Signal Generation**: Leverages a **Retrieval-Augmented Generation (RAG)** pipeline to derive `BUY/SELL/HOLD` signals from unstructured financial news.
-   **State-Aware Logic**: Uses distinct prompts for entering a new position vs. managing an existing one, enabling more nuanced, context-aware trading decisions.
-   **Hybrid & Local-First AI**: Combines cloud-based **Google AI** for high-quality embeddings with a local **Ollama-served LLM** (e.g., Gemma) for fast, private, and cost-effective inference.
-   **High-Performance Java Backtester**: A robust, event-driven engine calculates key quantitative metrics including **Sharpe Ratio** and **Maximum Drawdown**.
-   **Decoupled Microservices**: A Python **FastAPI** service for AI inference communicates with the Java backtester via a clean REST API, ensuring modularity and scalability.

## Example Backtest Results

The following results were generated from a backtest on **AAPL** stock from **January 2019 to August 2025**.

```
---Backtest Result---
Total Return Percentage: 196.99
Sharpe Ratio: 0.96
Max Drawdown: -0.27
Win Rate: 54.47
```

<details>
<summary><strong>Click to view full trade log (593 trades)</strong></summary>

```
---Trade log---
Entry: 2020-05-11 @ 308.10, Exit: 2020-05-12 @ 317.83, Return: 3.16
Entry: 2020-05-13 @ 312.15, Exit: 2020-05-14 @ 304.51, Return: -2.45
Entry: 2020-05-15 @ 300.35, Exit: 2020-05-18 @ 313.17, Return: 4.27
Entry: 2020-05-19 @ 315.03, Exit: 2020-05-20 @ 316.68, Return: 0.52
Entry: 2020-05-21 @ 318.66, Exit: 2020-05-22 @ 315.77, Return: -0.91
Entry: 2020-05-26 @ 323.50, Exit: 2020-05-28 @ 316.77, Return: -2.08
Entry: 2020-05-29 @ 319.25, Exit: 2020-06-01 @ 317.75, Return: -0.47
Entry: 2020-06-02 @ 320.75, Exit: 2020-06-03 @ 324.66, Return: 1.22
Entry: 2020-06-04 @ 324.39, Exit: 2020-06-05 @ 323.35, Return: -0.32
Entry: 2020-06-08 @ 330.25, Exit: 2020-06-10 @ 347.90, Return: 5.34
Entry: 2020-06-11 @ 349.31, Exit: 2020-06-12 @ 344.72, Return: -1.31
Entry: 2020-06-15 @ 333.25, Exit: 2020-06-16 @ 351.46, Return: 5.46
Entry: 2020-06-17 @ 355.15, Exit: 2020-06-18 @ 351.41, Return: -1.05
Entry: 2020-06-19 @ 354.64, Exit: 2020-06-22 @ 351.34, Return: -0.93
Entry: 2020-06-23 @ 364.00, Exit: 2020-06-24 @ 365.00, Return: 0.27
Entry: 2020-06-25 @ 360.70, Exit: 2020-06-26 @ 364.41, Return: 1.03
Entry: 2020-06-29 @ 353.25, Exit: 2020-06-30 @ 360.08, Return: 1.93
Entry: 2020-07-01 @ 365.12, Exit: 2020-07-06 @ 370.00, Return: 1.34
Entry: 2020-07-07 @ 375.41, Exit: 2020-07-08 @ 376.72, Return: 0.35
Entry: 2020-07-09 @ 385.05, Exit: 2020-07-10 @ 381.34, Return: -0.96
Entry: 2020-07-13 @ 389.06, Exit: 2020-07-14 @ 379.36, Return: -2.49
Entry: 2020-07-15 @ 395.96, Exit: 2020-07-16 @ 386.25, Return: -2.45
Entry: 2020-07-17 @ 387.95, Exit: 2020-07-20 @ 385.67, Return: -0.59
Entry: 2020-07-21 @ 396.69, Exit: 2020-07-22 @ 386.77, Return: -2.50
Entry: 2020-07-23 @ 387.99, Exit: 2020-07-24 @ 363.95, Return: -6.20
Entry: 2020-07-27 @ 374.84, Exit: 2020-07-28 @ 377.47, Return: 0.70
Entry: 2020-07-29 @ 375.00, Exit: 2020-07-30 @ 376.75, Return: 0.47
Entry: 2020-07-31 @ 411.54, Exit: 2020-08-03 @ 432.80, Return: 5.17
Entry: 2020-08-04 @ 436.53, Exit: 2020-08-05 @ 437.51, Return: 0.22
Entry: 2020-08-06 @ 441.62, Exit: 2020-08-07 @ 452.82, Return: 2.54
Entry: 2020-08-10 @ 450.40, Exit: 2020-08-11 @ 447.88, Return: -0.56
Entry: 2020-08-12 @ 441.99, Exit: 2020-08-13 @ 457.72, Return: 3.56
Entry: 2020-08-14 @ 459.32, Exit: 2020-08-18 @ 457.41, Return: -0.41
Entry: 2020-08-19 @ 463.93, Exit: 2020-08-20 @ 463.00, Return: -0.20
Entry: 2020-08-21 @ 477.05, Exit: 2020-08-24 @ 514.79, Return: 7.91
Entry: 2020-08-25 @ 498.79, Exit: 2020-08-26 @ 504.72, Return: 1.19
Entry: 2020-08-27 @ 508.57, Exit: 2020-08-28 @ 504.05, Return: -0.89
Entry: 2020-08-31 @ 127.58, Exit: 2020-09-01 @ 132.76, Return: 4.06
Entry: 2020-09-02 @ 137.59, Exit: 2020-09-04 @ 120.07, Return: -12.73
Entry: 2020-09-08 @ 113.95, Exit: 2020-09-09 @ 117.26, Return: 2.90
Entry: 2020-09-10 @ 120.36, Exit: 2020-09-11 @ 114.57, Return: -4.81
Entry: 2020-09-14 @ 114.72, Exit: 2020-09-15 @ 118.33, Return: 3.15
Entry: 2020-09-16 @ 115.23, Exit: 2020-09-18 @ 110.40, Return: -4.19
Entry: 2020-09-21 @ 104.54, Exit: 2020-09-23 @ 111.62, Return: 6.77
Entry: 2020-09-24 @ 105.17, Exit: 2020-09-25 @ 108.43, Return: 3.10
Entry: 2020-09-28 @ 115.01, Exit: 2020-09-29 @ 114.55, Return: -0.40
Entry: 2020-09-30 @ 113.79, Exit: 2020-10-01 @ 117.64, Return: 3.38
Entry: 2020-10-02 @ 112.89, Exit: 2020-10-05 @ 113.91, Return: 0.90
Entry: 2020-10-06 @ 115.70, Exit: 2020-10-07 @ 114.62, Return: -0.93
Entry: 2020-10-08 @ 116.25, Exit: 2020-10-12 @ 120.06, Return: 3.28
Entry: 2020-10-13 @ 125.27, Exit: 2020-10-14 @ 121.00, Return: -3.41
Entry: 2020-10-15 @ 118.72, Exit: 2020-10-16 @ 121.28, Return: 2.16
Entry: 2020-10-19 @ 119.96, Exit: 2020-10-20 @ 116.20, Return: -3.13
Entry: 2020-10-21 @ 116.67, Exit: 2020-10-22 @ 117.45, Return: 0.67
Entry: 2020-10-23 @ 116.39, Exit: 2020-10-26 @ 114.01, Return: -2.04
Entry: 2020-10-27 @ 115.49, Exit: 2020-10-29 @ 112.37, Return: -2.70
Entry: 2020-10-30 @ 111.06, Exit: 2020-11-02 @ 109.11, Return: -1.76
Entry: 2020-11-03 @ 109.66, Exit: 2020-11-05 @ 117.95, Return: 7.56
Entry: 2020-11-06 @ 118.32, Exit: 2020-11-10 @ 115.55, Return: -2.34
Entry: 2020-11-11 @ 117.19, Exit: 2020-11-12 @ 119.62, Return: 2.07
Entry: 2020-11-13 @ 119.44, Exit: 2020-11-16 @ 118.92, Return: -0.44
Entry: 2020-11-17 @ 119.55, Exit: 2020-11-18 @ 118.61, Return: -0.79
Entry: 2020-11-19 @ 117.59, Exit: 2020-11-23 @ 117.18, Return: -0.35
Entry: 2020-11-24 @ 113.91, Exit: 2020-11-27 @ 116.57, Return: 2.34
Entry: 2020-11-30 @ 116.97, Exit: 2020-12-01 @ 121.01, Return: 3.45
Entry: 2020-12-02 @ 122.02, Exit: 2020-12-03 @ 123.52, Return: 1.23
Entry: 2020-12-04 @ 122.60, Exit: 2020-12-07 @ 122.31, Return: -0.24
Entry: 2020-12-08 @ 124.37, Exit: 2020-12-09 @ 124.53, Return: 0.13
Entry: 2020-12-10 @ 120.50, Exit: 2020-12-15 @ 124.34, Return: 3.19
Entry: 2020-12-16 @ 127.41, Exit: 2020-12-17 @ 128.90, Return: 1.17
Entry: 2020-12-18 @ 128.96, Exit: 2020-12-24 @ 131.32, Return: 1.83
Entry: 2020-12-28 @ 133.99, Exit: 2020-12-29 @ 138.05, Return: 3.03
Entry: 2020-12-30 @ 135.58, Exit: 2020-12-31 @ 134.08, Return: -1.11
Entry: 2021-01-07 @ 128.36, Exit: 2021-04-05 @ 123.87, Return: -3.50
Entry: 2021-04-07 @ 125.83, Exit: 2021-04-08 @ 128.95, Return: 2.48
Entry: 2021-04-12 @ 132.52, Exit: 2021-04-13 @ 132.44, Return: -0.06
Entry: 2021-04-14 @ 134.94, Exit: 2021-04-15 @ 133.82, Return: -0.83
Entry: 2021-04-16 @ 134.30, Exit: 2021-04-19 @ 133.51, Return: -0.59
Entry: 2021-04-21 @ 132.36, Exit: 2021-04-22 @ 133.04, Return: 0.51
Entry: 2021-04-23 @ 132.16, Exit: 2021-04-26 @ 134.83, Return: 2.02
Entry: 2021-04-28 @ 134.31, Exit: 2021-04-29 @ 136.47, Return: 1.61
Entry: 2021-05-03 @ 132.04, Exit: 2021-05-04 @ 131.19, Return: -0.64
Entry: 2021-05-13 @ 124.58, Exit: 2021-05-14 @ 126.25, Return: 1.34
Entry: 2021-05-17 @ 126.82, Exit: 2021-05-18 @ 126.56, Return: -0.21
Entry: 2021-05-24 @ 126.01, Exit: 2021-05-25 @ 127.82, Return: 1.44
Entry: 2021-05-27 @ 126.44, Exit: 2021-05-28 @ 125.57, Return: -0.69
Entry: 2021-06-01 @ 125.08, Exit: 2021-06-02 @ 124.28, Return: -0.64
Entry: 2021-06-03 @ 124.68, Exit: 2021-06-04 @ 124.07, Return: -0.49
Entry: 2021-06-07 @ 126.17, Exit: 2021-06-08 @ 126.60, Return: 0.34
Entry: 2021-06-09 @ 127.21, Exit: 2021-06-10 @ 127.02, Return: -0.15
Entry: 2021-06-11 @ 126.53, Exit: 2021-06-14 @ 127.82, Return: 1.02
Entry: 2021-06-15 @ 129.94, Exit: 2021-06-16 @ 130.37, Return: 0.33
Entry: 2021-06-17 @ 129.80, Exit: 2021-06-18 @ 130.71, Return: 0.70
Entry: 2021-06-21 @ 130.30, Exit: 2021-06-22 @ 132.13, Return: 1.40
Entry: 2021-06-23 @ 133.77, Exit: 2021-06-24 @ 134.45, Return: 0.51
Entry: 2021-06-25 @ 133.46, Exit: 2021-06-28 @ 133.41, Return: -0.04
Entry: 2021-06-29 @ 134.80, Exit: 2021-06-30 @ 136.17, Return: 1.02
Entry: 2021-07-01 @ 136.60, Exit: 2021-07-02 @ 137.90, Return: 0.95
Entry: 2021-07-06 @ 140.07, Exit: 2021-07-07 @ 143.54, Return: 2.47
Entry: 2021-07-08 @ 141.58, Exit: 2021-07-09 @ 142.75, Return: 0.83
Entry: 2021-07-12 @ 146.21, Exit: 2021-07-13 @ 144.03, Return: -1.49
Entry: 2021-07-14 @ 148.10, Exit: 2021-07-15 @ 149.24, Return: 0.77
Entry: 2021-07-16 @ 148.46, Exit: 2021-07-19 @ 143.75, Return: -3.17
Entry: 2021-07-20 @ 143.46, Exit: 2021-07-21 @ 145.53, Return: 1.44
Entry: 2021-07-22 @ 145.94, Exit: 2021-07-23 @ 147.55, Return: 1.11
Entry: 2021-07-26 @ 148.27, Exit: 2021-07-27 @ 149.12, Return: 0.57
Entry: 2021-07-28 @ 144.81, Exit: 2021-07-29 @ 144.69, Return: -0.09
Entry: 2021-07-30 @ 144.38, Exit: 2021-08-02 @ 146.36, Return: 1.37
Entry: 2021-08-03 @ 145.81, Exit: 2021-08-04 @ 147.27, Return: 1.00
Entry: 2021-08-05 @ 146.98, Exit: 2021-08-06 @ 146.35, Return: -0.43
Entry: 2021-08-09 @ 146.20, Exit: 2021-08-10 @ 146.44, Return: 0.16
Entry: 2021-08-11 @ 146.05, Exit: 2021-08-12 @ 146.19, Return: 0.10
Entry: 2021-08-13 @ 148.97, Exit: 2021-08-16 @ 148.54, Return: -0.29
Entry: 2021-08-17 @ 150.23, Exit: 2021-08-18 @ 149.80, Return: -0.29
Entry: 2021-08-19 @ 145.03, Exit: 2021-08-20 @ 147.44, Return: 1.66
Entry: 2021-08-23 @ 148.31, Exit: 2021-08-24 @ 149.45, Return: 0.77
Entry: 2021-08-25 @ 149.81, Exit: 2021-08-26 @ 148.35, Return: -0.97
Entry: 2021-08-27 @ 147.48, Exit: 2021-08-30 @ 149.00, Return: 1.03
Entry: 2021-08-31 @ 152.66, Exit: 2021-09-01 @ 152.83, Return: 0.11
Entry: 2021-09-02 @ 153.87, Exit: 2021-09-03 @ 153.76, Return: -0.07
Entry: 2021-09-07 @ 154.97, Exit: 2021-09-08 @ 156.98, Return: 1.30
Entry: 2021-09-09 @ 155.49, Exit: 2021-09-10 @ 155.00, Return: -0.32
Entry: 2021-09-13 @ 150.63, Exit: 2021-09-14 @ 150.35, Return: -0.19
Entry: 2021-09-15 @ 148.56, Exit: 2021-09-16 @ 148.44, Return: -0.08
Entry: 2021-09-17 @ 148.82, Exit: 2021-09-20 @ 143.80, Return: -3.37
Entry: 2021-09-21 @ 143.93, Exit: 2021-09-22 @ 144.45, Return: 0.36
Entry: 2021-09-23 @ 146.65, Exit: 2021-09-24 @ 145.66, Return: -0.68
Entry: 2021-09-27 @ 145.47, Exit: 2021-09-28 @ 143.25, Return: -1.53
Entry: 2021-09-29 @ 142.47, Exit: 2021-09-30 @ 143.66, Return: 0.84
Entry: 2021-10-01 @ 141.90, Exit: 2021-10-04 @ 141.76, Return: -0.10
Entry: 2021-10-05 @ 139.49, Exit: 2021-10-06 @ 139.47, Return: -0.01
Entry: 2021-10-07 @ 143.06, Exit: 2021-10-08 @ 144.03, Return: 0.68
Entry: 2021-10-11 @ 142.27, Exit: 2021-10-12 @ 143.23, Return: 0.67
Entry: 2021-10-13 @ 141.24, Exit: 2021-10-14 @ 142.11, Return: 0.62
Entry: 2021-10-15 @ 143.77, Exit: 2021-10-18 @ 143.45, Return: -0.23
Entry: 2021-10-19 @ 147.01, Exit: 2021-10-20 @ 148.70, Return: 1.15
Entry: 2021-10-21 @ 148.81, Exit: 2021-10-22 @ 149.69, Return: 0.59
Entry: 2021-10-25 @ 148.68, Exit: 2021-10-26 @ 149.33, Return: 0.44
Entry: 2021-10-27 @ 149.36, Exit: 2021-10-28 @ 149.82, Return: 0.31
Entry: 2021-10-29 @ 147.22, Exit: 2021-11-01 @ 148.99, Return: 1.20
Entry: 2021-11-02 @ 148.66, Exit: 2021-11-03 @ 150.39, Return: 1.16
Entry: 2021-11-04 @ 151.58, Exit: 2021-11-05 @ 151.89, Return: 0.20
Entry: 2021-11-08 @ 151.41, Exit: 2021-11-09 @ 150.20, Return: -0.80
Entry: 2021-11-10 @ 150.02, Exit: 2021-11-11 @ 148.96, Return: -0.71
Entry: 2021-11-12 @ 148.43, Exit: 2021-11-15 @ 150.37, Return: 1.31
Entry: 2021-11-16 @ 149.94, Exit: 2021-11-17 @ 151.00, Return: 0.70
Entry: 2021-11-18 @ 153.71, Exit: 2021-11-19 @ 157.65, Return: 2.56
Entry: 2021-11-22 @ 161.68, Exit: 2021-11-23 @ 161.12, Return: -0.35
Entry: 2021-11-24 @ 160.75, Exit: 2021-11-26 @ 159.57, Return: -0.74
Entry: 2021-11-29 @ 159.37, Exit: 2021-11-30 @ 159.99, Return: 0.39
Entry: 2021-12-01 @ 167.48, Exit: 2021-12-02 @ 158.74, Return: -5.22
Entry: 2021-12-03 @ 164.02, Exit: 2021-12-06 @ 164.29, Return: 0.16
Entry: 2021-12-07 @ 169.08, Exit: 2021-12-08 @ 172.13, Return: 1.80
Entry: 2021-12-09 @ 174.91, Exit: 2021-12-10 @ 175.21, Return: 0.17
Entry: 2021-12-13 @ 181.12, Exit: 2021-12-14 @ 175.25, Return: -3.24
Entry: 2021-12-15 @ 175.11, Exit: 2021-12-16 @ 179.28, Return: 2.38
Entry: 2021-12-17 @ 169.93, Exit: 2021-12-20 @ 168.28, Return: -0.97
Entry: 2021-12-21 @ 171.56, Exit: 2021-12-22 @ 173.04, Return: 0.87
Entry: 2021-12-23 @ 175.85, Exit: 2021-12-27 @ 177.09, Return: 0.70
Entry: 2021-12-28 @ 180.16, Exit: 2021-12-29 @ 179.33, Return: -0.46
Entry: 2021-12-30 @ 179.47, Exit: 2021-12-31 @ 178.09, Return: -0.77
Entry: 2022-01-04 @ 182.63, Exit: 2022-01-05 @ 179.61, Return: -1.65
Entry: 2022-01-06 @ 172.70, Exit: 2022-01-07 @ 172.89, Return: 0.11
Entry: 2022-01-10 @ 169.08, Exit: 2022-01-11 @ 172.32, Return: 1.92
Entry: 2022-01-12 @ 176.12, Exit: 2022-01-13 @ 175.78, Return: -0.19
Entry: 2022-01-14 @ 171.34, Exit: 2022-01-18 @ 171.51, Return: 0.10
Entry: 2022-01-19 @ 170.00, Exit: 2022-01-20 @ 166.98, Return: -1.78
Entry: 2022-01-21 @ 164.42, Exit: 2022-01-24 @ 160.02, Return: -2.67
Entry: 2022-01-25 @ 158.98, Exit: 2022-01-28 @ 165.71, Return: 4.23
Entry: 2022-01-31 @ 170.16, Exit: 2022-02-01 @ 174.01, Return: 2.26
Entry: 2022-02-02 @ 174.75, Exit: 2022-02-03 @ 174.48, Return: -0.15
Entry: 2022-02-04 @ 171.68, Exit: 2022-02-07 @ 172.86, Return: 0.69
Entry: 2022-02-08 @ 171.73, Exit: 2022-02-09 @ 176.05, Return: 2.52
Entry: 2022-02-10 @ 174.14, Exit: 2022-02-11 @ 172.33, Return: -1.04
Entry: 2022-02-14 @ 167.37, Exit: 2022-02-15 @ 170.97, Return: 2.15
Entry: 2022-02-16 @ 171.85, Exit: 2022-02-17 @ 171.03, Return: -0.48
Entry: 2022-02-18 @ 169.82, Exit: 2022-02-23 @ 165.54, Return: -2.52
Entry: 2022-02-24 @ 152.58, Exit: 2022-03-01 @ 164.70, Return: 7.94
Entry: 2022-03-02 @ 164.39, Exit: 2022-03-03 @ 168.47, Return: 2.48
Entry: 2022-03-04 @ 164.49, Exit: 2022-03-07 @ 163.36, Return: -0.69
Entry: 2022-03-08 @ 158.82, Exit: 2022-03-09 @ 161.48, Return: 1.67
Entry: 2022-03-10 @ 160.20, Exit: 2022-03-11 @ 158.93, Return: -0.79
Entry: 2022-03-14 @ 151.45, Exit: 2022-03-15 @ 150.90, Return: -0.36
Entry: 2022-03-16 @ 157.05, Exit: 2022-03-17 @ 158.61, Return: 0.99
Entry: 2022-03-18 @ 160.51, Exit: 2022-03-21 @ 163.51, Return: 1.87
Entry: 2022-03-22 @ 165.51, Exit: 2022-03-23 @ 167.99, Return: 1.50
Entry: 2022-03-24 @ 171.06, Exit: 2022-03-25 @ 173.88, Return: 1.65
Entry: 2022-03-28 @ 172.17, Exit: 2022-03-29 @ 176.69, Return: 2.63
Entry: 2022-03-30 @ 178.55, Exit: 2022-03-31 @ 177.84, Return: -0.40
Entry: 2022-04-01 @ 174.03, Exit: 2022-04-04 @ 174.57, Return: 0.31
Entry: 2022-04-05 @ 177.50, Exit: 2022-04-06 @ 172.36, Return: -2.90
Entry: 2022-04-07 @ 171.16, Exit: 2022-04-08 @ 171.78, Return: 0.36
Entry: 2022-04-11 @ 168.71, Exit: 2022-04-12 @ 168.02, Return: -0.41
Entry: 2022-04-13 @ 167.39, Exit: 2022-04-14 @ 170.62, Return: 1.93
Entry: 2022-04-18 @ 163.92, Exit: 2022-04-19 @ 165.02, Return: 0.67
Entry: 2022-04-20 @ 168.76, Exit: 2022-04-21 @ 168.91, Return: 0.09
Entry: 2022-04-22 @ 166.46, Exit: 2022-04-25 @ 161.12, Return: -3.21
Entry: 2022-04-26 @ 162.25, Exit: 2022-04-28 @ 159.25, Return: -1.85
Entry: 2022-04-29 @ 161.84, Exit: 2022-05-02 @ 156.71, Return: -3.17
Entry: 2022-05-04 @ 159.67, Exit: 2022-05-05 @ 163.85, Return: 2.62
Entry: 2022-05-06 @ 156.01, Exit: 2022-05-09 @ 154.93, Return: -0.70
Entry: 2022-05-11 @ 153.50, Exit: 2022-05-12 @ 142.77, Return: -6.99
Entry: 2022-05-13 @ 144.59, Exit: 2022-05-16 @ 145.55, Return: 0.66
Entry: 2022-05-17 @ 148.86, Exit: 2022-05-19 @ 139.88, Return: -6.03
Entry: 2022-05-20 @ 139.09, Exit: 2022-05-23 @ 137.79, Return: -0.93
Entry: 2022-05-26 @ 137.39, Exit: 2022-05-27 @ 145.39, Return: 5.82
Entry: 2022-05-31 @ 149.07, Exit: 2022-06-01 @ 149.90, Return: 0.56
Entry: 2022-06-02 @ 147.83, Exit: 2022-06-03 @ 146.90, Return: -0.63
Entry: 2022-06-06 @ 147.03, Exit: 2022-06-07 @ 144.35, Return: -1.83
Entry: 2022-06-09 @ 147.08, Exit: 2022-06-10 @ 140.28, Return: -4.62
Entry: 2022-06-13 @ 132.87, Exit: 2022-06-14 @ 133.13, Return: 0.20
Entry: 2022-06-15 @ 134.29, Exit: 2022-06-16 @ 132.08, Return: -1.65
Entry: 2022-06-17 @ 130.07, Exit: 2022-06-21 @ 133.42, Return: 2.58
Entry: 2022-06-22 @ 134.79, Exit: 2022-06-23 @ 136.82, Return: 1.51
Entry: 2022-06-24 @ 139.90, Exit: 2022-06-27 @ 142.70, Return: 2.00
Entry: 2022-06-28 @ 142.13, Exit: 2022-06-29 @ 137.46, Return: -3.29
Entry: 2022-06-30 @ 137.25, Exit: 2022-07-01 @ 136.04, Return: -0.88
Entry: 2022-07-05 @ 137.77, Exit: 2022-07-06 @ 141.36, Return: 2.60
Entry: 2022-07-07 @ 143.29, Exit: 2022-07-08 @ 145.27, Return: 1.38
Entry: 2022-07-11 @ 145.67, Exit: 2022-07-12 @ 145.76, Return: 0.06
Entry: 2022-07-13 @ 142.99, Exit: 2022-07-14 @ 144.08, Return: 0.76
Entry: 2022-07-15 @ 149.78, Exit: 2022-07-18 @ 150.74, Return: 0.64
Entry: 2022-07-19 @ 147.92, Exit: 2022-07-20 @ 151.12, Return: 2.16
Entry: 2022-07-21 @ 154.50, Exit: 2022-07-22 @ 155.39, Return: 0.58
Entry: 2022-07-25 @ 154.01, Exit: 2022-07-26 @ 152.27, Return: -1.13
Entry: 2022-07-27 @ 152.58, Exit: 2022-07-28 @ 156.98, Return: 2.88
Entry: 2022-07-29 @ 161.24, Exit: 2022-08-01 @ 161.01, Return: -0.14
Entry: 2022-08-02 @ 160.10, Exit: 2022-08-03 @ 160.84, Return: 0.46
Entry: 2022-08-04 @ 166.01, Exit: 2022-08-05 @ 163.21, Return: -1.68
Entry: 2022-08-08 @ 166.37, Exit: 2022-08-09 @ 164.02, Return: -1.41
Entry: 2022-08-10 @ 167.68, Exit: 2022-08-11 @ 170.06, Return: 1.42
Entry: 2022-08-12 @ 169.82, Exit: 2022-08-15 @ 171.52, Return: 1.00
Entry: 2022-08-16 @ 172.78, Exit: 2022-08-17 @ 172.77, Return: -0.01
Entry: 2022-08-18 @ 173.75, Exit: 2022-08-19 @ 173.03, Return: -0.41
Entry: 2022-08-22 @ 169.69, Exit: 2022-08-23 @ 167.08, Return: -1.54
Entry: 2022-08-24 @ 167.32, Exit: 2022-08-25 @ 168.78, Return: 0.87
Entry: 2022-08-26 @ 170.57, Exit: 2022-08-29 @ 161.15, Return: -5.53
Entry: 2022-08-30 @ 162.13, Exit: 2022-08-31 @ 160.31, Return: -1.13
Entry: 2022-09-01 @ 156.64, Exit: 2022-09-02 @ 159.75, Return: 1.99
Entry: 2022-09-06 @ 156.47, Exit: 2022-09-07 @ 154.83, Return: -1.05
Entry: 2022-09-08 @ 154.64, Exit: 2022-09-09 @ 155.47, Return: 0.54
Entry: 2022-09-12 @ 159.59, Exit: 2022-09-13 @ 159.90, Return: 0.19
Entry: 2022-09-14 @ 154.79, Exit: 2022-09-15 @ 154.65, Return: -0.09
Entry: 2022-09-16 @ 151.21, Exit: 2022-09-19 @ 149.31, Return: -1.26
Entry: 2022-09-20 @ 153.40, Exit: 2022-09-21 @ 157.34, Return: 2.57
Entry: 2022-09-22 @ 152.38, Exit: 2022-09-23 @ 151.19, Return: -0.78
Entry: 2022-09-26 @ 149.66, Exit: 2022-09-27 @ 152.74, Return: 2.06
Entry: 2022-09-28 @ 147.64, Exit: 2022-09-29 @ 146.10, Return: -1.04
Entry: 2022-09-30 @ 141.28, Exit: 2022-10-03 @ 138.21, Return: -2.17
Entry: 2022-10-04 @ 145.03, Exit: 2022-10-05 @ 144.08, Return: -0.66
Entry: 2022-10-06 @ 145.81, Exit: 2022-10-07 @ 142.54, Return: -2.24
Entry: 2022-10-10 @ 140.42, Exit: 2022-10-11 @ 139.90, Return: -0.37
Entry: 2022-10-12 @ 139.13, Exit: 2022-10-13 @ 134.99, Return: -2.98
Entry: 2022-10-14 @ 144.31, Exit: 2022-10-17 @ 141.07, Return: -2.25
Entry: 2022-10-18 @ 145.49, Exit: 2022-10-19 @ 141.69, Return: -2.61
Entry: 2022-10-20 @ 143.02, Exit: 2022-10-21 @ 142.87, Return: -0.10
Entry: 2022-10-24 @ 147.19, Exit: 2022-10-25 @ 150.09, Return: 1.97
Entry: 2022-10-26 @ 150.96, Exit: 2022-10-27 @ 148.07, Return: -1.91
Entry: 2022-10-28 @ 148.20, Exit: 2022-10-31 @ 153.16, Return: 3.34
Entry: 2022-11-01 @ 155.08, Exit: 2022-11-02 @ 148.95, Return: -3.96
Entry: 2022-11-03 @ 142.06, Exit: 2022-11-04 @ 142.09, Return: 0.02
Entry: 2022-11-07 @ 137.11, Exit: 2022-11-08 @ 140.41, Return: 2.41
Entry: 2022-11-09 @ 138.50, Exit: 2022-11-10 @ 141.24, Return: 1.98
Entry: 2022-11-11 @ 145.82, Exit: 2022-11-14 @ 148.97, Return: 2.16
Entry: 2022-11-15 @ 152.22, Exit: 2022-11-16 @ 149.13, Return: -2.03
Entry: 2022-11-17 @ 146.43, Exit: 2022-11-18 @ 152.31, Return: 4.01
Entry: 2022-11-21 @ 150.16, Exit: 2022-11-22 @ 148.13, Return: -1.35
Entry: 2022-11-23 @ 149.45, Exit: 2022-11-25 @ 148.31, Return: -0.77
Entry: 2022-11-28 @ 145.14, Exit: 2022-11-29 @ 144.29, Return: -0.59
Entry: 2022-11-30 @ 141.40, Exit: 2022-12-01 @ 148.21, Return: 4.82
Entry: 2022-12-02 @ 145.96, Exit: 2022-12-05 @ 147.77, Return: 1.24
Entry: 2022-12-06 @ 147.08, Exit: 2022-12-07 @ 142.19, Return: -3.32
Entry: 2022-12-08 @ 142.36, Exit: 2022-12-09 @ 142.34, Return: -0.01
Entry: 2022-12-12 @ 142.70, Exit: 2022-12-13 @ 149.50, Return: 4.77
Entry: 2022-12-14 @ 145.35, Exit: 2022-12-15 @ 141.11, Return: -2.92
Entry: 2022-12-16 @ 136.69, Exit: 2022-12-19 @ 135.11, Return: -1.15
Entry: 2022-12-20 @ 131.39, Exit: 2022-12-21 @ 132.98, Return: 1.21
Entry: 2022-12-22 @ 134.35, Exit: 2022-12-23 @ 130.92, Return: -2.55
Entry: 2022-12-27 @ 131.38, Exit: 2022-12-28 @ 129.67, Return: -1.30
Entry: 2022-12-29 @ 127.99, Exit: 2022-12-30 @ 128.41, Return: 0.33
Entry: 2023-01-03 @ 130.28, Exit: 2023-01-04 @ 126.89, Return: -2.60
Entry: 2023-01-05 @ 127.13, Exit: 2023-01-06 @ 126.01, Return: -0.88
Entry: 2023-01-09 @ 130.47, Exit: 2023-01-10 @ 130.26, Return: -0.16
Entry: 2023-01-11 @ 131.25, Exit: 2023-01-12 @ 133.88, Return: 2.00
Entry: 2023-01-13 @ 132.03, Exit: 2023-01-17 @ 134.83, Return: 2.12
Entry: 2023-01-18 @ 136.82, Exit: 2023-01-19 @ 134.08, Return: -2.00
Entry: 2023-01-20 @ 135.28, Exit: 2023-01-23 @ 138.12, Return: 2.10
Entry: 2023-01-24 @ 140.31, Exit: 2023-01-25 @ 140.89, Return: 0.42
Entry: 2023-01-26 @ 143.17, Exit: 2023-01-27 @ 143.16, Return: -0.01
Entry: 2023-01-30 @ 144.96, Exit: 2023-02-02 @ 148.90, Return: 2.72
Entry: 2023-02-03 @ 148.03, Exit: 2023-02-07 @ 150.64, Return: 1.76
Entry: 2023-02-08 @ 153.88, Exit: 2023-02-09 @ 153.78, Return: -0.07
Entry: 2023-02-10 @ 149.46, Exit: 2023-02-13 @ 150.95, Return: 1.00
Entry: 2023-02-14 @ 152.12, Exit: 2023-02-16 @ 153.51, Return: 0.91
Entry: 2023-02-17 @ 152.35, Exit: 2023-02-21 @ 150.20, Return: -1.41
Entry: 2023-02-22 @ 148.87, Exit: 2023-02-23 @ 150.09, Return: 0.82
Entry: 2023-02-24 @ 147.11, Exit: 2023-02-27 @ 147.71, Return: 0.41
Entry: 2023-02-28 @ 147.05, Exit: 2023-03-01 @ 146.83, Return: -0.15
Entry: 2023-03-02 @ 144.38, Exit: 2023-03-06 @ 153.79, Return: 6.51
Entry: 2023-03-07 @ 153.70, Exit: 2023-03-09 @ 153.56, Return: -0.09
Entry: 2023-03-16 @ 152.16, Exit: 2023-03-22 @ 159.30, Return: 4.69
Entry: 2023-03-23 @ 158.83, Exit: 2023-03-28 @ 157.97, Return: -0.54
Entry: 2023-03-29 @ 159.37, Exit: 2023-03-30 @ 161.53, Return: 1.36
Entry: 2023-04-03 @ 164.27, Exit: 2023-04-04 @ 166.60, Return: 1.42
Entry: 2023-04-05 @ 164.74, Exit: 2023-04-06 @ 162.43, Return: -1.40
Entry: 2023-04-10 @ 161.42, Exit: 2023-04-11 @ 162.35, Return: 0.58
Entry: 2023-04-12 @ 161.22, Exit: 2023-04-13 @ 161.63, Return: 0.25
Entry: 2023-04-14 @ 164.59, Exit: 2023-04-17 @ 165.09, Return: 0.30
Entry: 2023-04-18 @ 166.10, Exit: 2023-04-19 @ 165.80, Return: -0.18
Entry: 2023-04-20 @ 166.09, Exit: 2023-04-21 @ 165.05, Return: -0.63
Entry: 2023-04-24 @ 165.00, Exit: 2023-04-25 @ 165.19, Return: 0.12
Entry: 2023-04-26 @ 163.06, Exit: 2023-04-27 @ 165.19, Return: 1.31
Entry: 2023-04-28 @ 168.49, Exit: 2023-05-01 @ 169.28, Return: 0.47
Entry: 2023-05-02 @ 170.09, Exit: 2023-05-03 @ 169.50, Return: -0.35
Entry: 2023-05-04 @ 164.89, Exit: 2023-05-05 @ 170.98, Return: 3.69
Entry: 2023-05-08 @ 172.48, Exit: 2023-05-09 @ 173.05, Return: 0.33
Entry: 2023-05-10 @ 173.02, Exit: 2023-05-11 @ 173.85, Return: 0.48
Entry: 2023-05-12 @ 173.62, Exit: 2023-05-15 @ 173.16, Return: -0.26
Entry: 2023-05-16 @ 171.99, Exit: 2023-05-17 @ 171.71, Return: -0.16
Entry: 2023-05-18 @ 173.00, Exit: 2023-05-19 @ 176.39, Return: 1.96
Entry: 2023-05-22 @ 173.98, Exit: 2023-05-23 @ 173.13, Return: -0.49
Entry: 2023-05-24 @ 171.09, Exit: 2023-05-25 @ 172.41, Return: 0.77
Entry: 2023-05-26 @ 173.32, Exit: 2023-05-30 @ 176.96, Return: 2.10
Entry: 2023-05-31 @ 177.33, Exit: 2023-06-01 @ 177.70, Return: 0.21
Entry: 2023-06-02 @ 181.03, Exit: 2023-06-05 @ 182.63, Return: 0.88
Entry: 2023-06-06 @ 179.97, Exit: 2023-06-07 @ 178.44, Return: -0.85
Entry: 2023-06-08 @ 177.90, Exit: 2023-06-09 @ 181.50, Return: 2.03
Entry: 2023-06-12 @ 181.27, Exit: 2023-06-13 @ 182.80, Return: 0.84
Entry: 2023-06-14 @ 183.37, Exit: 2023-06-15 @ 183.96, Return: 0.32
Entry: 2023-06-16 @ 186.73, Exit: 2023-06-20 @ 184.41, Return: -1.24
Entry: 2023-06-21 @ 184.90, Exit: 2023-06-22 @ 183.74, Return: -0.63
Entry: 2023-06-23 @ 185.55, Exit: 2023-06-26 @ 186.83, Return: 0.69
Entry: 2023-06-27 @ 185.89, Exit: 2023-06-28 @ 187.93, Return: 1.10
Entry: 2023-06-29 @ 189.08, Exit: 2023-06-30 @ 191.63, Return: 1.35
Entry: 2023-07-03 @ 193.78, Exit: 2023-07-05 @ 191.57, Return: -1.14
Entry: 2023-07-06 @ 189.84, Exit: 2023-07-07 @ 191.41, Return: 0.83
Entry: 2023-07-10 @ 189.26, Exit: 2023-07-11 @ 189.16, Return: -0.05
Entry: 2023-07-12 @ 189.68, Exit: 2023-07-13 @ 190.50, Return: 0.43
Entry: 2023-07-14 @ 190.23, Exit: 2023-07-17 @ 191.90, Return: 0.88
Entry: 2023-07-18 @ 193.35, Exit: 2023-07-19 @ 193.10, Return: -0.13
Entry: 2023-07-20 @ 195.09, Exit: 2023-07-21 @ 194.10, Return: -0.51
Entry: 2023-07-24 @ 193.41, Exit: 2023-07-25 @ 193.33, Return: -0.04
Entry: 2023-07-26 @ 193.67, Exit: 2023-07-27 @ 196.02, Return: 1.21
Entry: 2023-07-28 @ 194.67, Exit: 2023-07-31 @ 196.06, Return: 0.71
Entry: 2023-08-01 @ 196.24, Exit: 2023-08-02 @ 195.04, Return: -0.61
Entry: 2023-08-03 @ 191.57, Exit: 2023-08-04 @ 185.52, Return: -3.16
Entry: 2023-08-07 @ 182.13, Exit: 2023-08-08 @ 179.69, Return: -1.34
Entry: 2023-08-09 @ 180.87, Exit: 2023-08-10 @ 179.48, Return: -0.77
Entry: 2023-08-11 @ 177.32, Exit: 2023-08-14 @ 177.97, Return: 0.37
Entry: 2023-08-15 @ 178.88, Exit: 2023-08-16 @ 177.13, Return: -0.98
Entry: 2023-08-17 @ 177.14, Exit: 2023-08-18 @ 172.30, Return: -2.73
Entry: 2023-08-21 @ 175.07, Exit: 2023-08-22 @ 177.06, Return: 1.14
Entry: 2023-08-23 @ 178.52, Exit: 2023-08-24 @ 180.67, Return: 1.21
Entry: 2023-08-25 @ 177.38, Exit: 2023-08-28 @ 180.09, Return: 1.53
Entry: 2023-08-29 @ 179.70, Exit: 2023-08-30 @ 184.94, Return: 2.92
Entry: 2023-08-31 @ 187.84, Exit: 2023-09-01 @ 189.49, Return: 0.88
Entry: 2023-09-05 @ 188.28, Exit: 2023-09-06 @ 188.40, Return: 0.06
Entry: 2023-09-07 @ 175.18, Exit: 2023-09-08 @ 178.35, Return: 1.81
Entry: 2023-09-11 @ 180.07, Exit: 2023-09-12 @ 179.49, Return: -0.32
Entry: 2023-09-13 @ 176.51, Exit: 2023-09-14 @ 174.00, Return: -1.42
Entry: 2023-09-15 @ 176.48, Exit: 2023-09-18 @ 176.48, Return: 0.00
Entry: 2023-09-19 @ 177.52, Exit: 2023-09-20 @ 179.26, Return: 0.98
Entry: 2023-09-21 @ 174.55, Exit: 2023-09-22 @ 174.67, Return: 0.07
Entry: 2023-09-25 @ 174.20, Exit: 2023-09-26 @ 174.82, Return: 0.36
Entry: 2023-09-27 @ 172.62, Exit: 2023-09-28 @ 169.34, Return: -1.90
Entry: 2023-09-29 @ 172.02, Exit: 2023-10-02 @ 171.22, Return: -0.47
Entry: 2023-10-03 @ 172.26, Exit: 2023-10-04 @ 171.09, Return: -0.68
Entry: 2023-10-05 @ 173.79, Exit: 2023-10-06 @ 173.80, Return: 0.01
Entry: 2023-10-09 @ 176.81, Exit: 2023-10-10 @ 178.10, Return: 0.73
Entry: 2023-10-11 @ 178.20, Exit: 2023-10-12 @ 180.07, Return: 1.05
Entry: 2023-10-13 @ 181.42, Exit: 2023-10-16 @ 176.75, Return: -2.57
Entry: 2023-10-17 @ 176.65, Exit: 2023-10-18 @ 175.58, Return: -0.60
Entry: 2023-10-19 @ 176.04, Exit: 2023-10-20 @ 175.31, Return: -0.41
Entry: 2023-10-23 @ 170.91, Exit: 2023-10-24 @ 173.05, Return: 1.25
Entry: 2023-10-25 @ 171.88, Exit: 2023-10-26 @ 170.37, Return: -0.88
Entry: 2023-10-27 @ 166.91, Exit: 2023-10-31 @ 169.35, Return: 1.46
Entry: 2023-11-01 @ 171.00, Exit: 2023-11-02 @ 175.52, Return: 2.64
Entry: 2023-11-03 @ 174.24, Exit: 2023-11-06 @ 176.38, Return: 1.23
Entry: 2023-11-07 @ 179.18, Exit: 2023-11-08 @ 182.35, Return: 1.77
Entry: 2023-11-09 @ 182.96, Exit: 2023-11-10 @ 183.97, Return: 0.55
Entry: 2023-11-13 @ 185.82, Exit: 2023-11-14 @ 187.70, Return: 1.01
Entry: 2023-11-15 @ 187.85, Exit: 2023-11-16 @ 189.57, Return: 0.92
Entry: 2023-11-17 @ 190.25, Exit: 2023-11-20 @ 189.89, Return: -0.19
Entry: 2023-11-21 @ 191.41, Exit: 2023-11-22 @ 191.49, Return: 0.04
Entry: 2023-11-24 @ 190.87, Exit: 2023-11-27 @ 189.92, Return: -0.50
Entry: 2023-11-28 @ 189.78, Exit: 2023-11-29 @ 190.90, Return: 0.59
Entry: 2023-11-30 @ 189.84, Exit: 2023-12-01 @ 190.33, Return: 0.26
Entry: 2023-12-04 @ 189.98, Exit: 2023-12-05 @ 190.21, Return: 0.12
Entry: 2023-12-06 @ 194.45, Exit: 2023-12-07 @ 193.63, Return: -0.42
Entry: 2023-12-08 @ 194.20, Exit: 2023-12-11 @ 193.11, Return: -0.56
Entry: 2023-12-12 @ 193.08, Exit: 2023-12-13 @ 195.09, Return: 1.04
Entry: 2023-12-14 @ 198.02, Exit: 2023-12-15 @ 197.53, Return: -0.25
Entry: 2023-12-18 @ 196.09, Exit: 2023-12-19 @ 196.16, Return: 0.04
Entry: 2023-12-20 @ 196.90, Exit: 2023-12-21 @ 196.10, Return: -0.41
Entry: 2023-12-22 @ 195.18, Exit: 2023-12-26 @ 193.61, Return: -0.80
Entry: 2023-12-27 @ 192.49, Exit: 2023-12-28 @ 194.14, Return: 0.86
Entry: 2023-12-29 @ 193.90, Exit: 2024-01-02 @ 187.15, Return: -3.48
Entry: 2024-01-03 @ 184.22, Exit: 2024-01-04 @ 182.15, Return: -1.12
Entry: 2024-01-05 @ 181.99, Exit: 2024-01-08 @ 182.09, Return: 0.05
Entry: 2024-01-09 @ 183.92, Exit: 2024-01-10 @ 184.35, Return: 0.23
Entry: 2024-01-11 @ 186.54, Exit: 2024-01-16 @ 182.16, Return: -2.35
Entry: 2024-01-17 @ 181.27, Exit: 2024-01-18 @ 186.09, Return: 2.66
Entry: 2024-01-19 @ 189.33, Exit: 2024-01-22 @ 192.30, Return: 1.57
Entry: 2024-01-23 @ 195.02, Exit: 2024-01-24 @ 195.42, Return: 0.21
Entry: 2024-01-25 @ 195.22, Exit: 2024-01-26 @ 194.27, Return: -0.49
Entry: 2024-01-29 @ 192.01, Exit: 2024-01-30 @ 190.94, Return: -0.56
Entry: 2024-01-31 @ 187.04, Exit: 2024-02-01 @ 183.99, Return: -1.63
Entry: 2024-02-02 @ 179.86, Exit: 2024-02-05 @ 188.15, Return: 4.61
Entry: 2024-02-06 @ 186.86, Exit: 2024-02-07 @ 190.64, Return: 2.02
Entry: 2024-02-08 @ 189.39, Exit: 2024-02-09 @ 188.65, Return: -0.39
Entry: 2024-02-12 @ 188.42, Exit: 2024-02-13 @ 185.77, Return: -1.40
Entry: 2024-02-14 @ 185.32, Exit: 2024-02-15 @ 183.55, Return: -0.96
Entry: 2024-02-16 @ 183.42, Exit: 2024-02-20 @ 181.79, Return: -0.89
Entry: 2024-02-21 @ 181.94, Exit: 2024-02-23 @ 185.01, Return: 1.69
Entry: 2024-02-26 @ 182.24, Exit: 2024-02-27 @ 181.10, Return: -0.63
Entry: 2024-02-28 @ 182.51, Exit: 2024-02-29 @ 181.27, Return: -0.68
Entry: 2024-03-01 @ 179.55, Exit: 2024-03-04 @ 176.15, Return: -1.89
Entry: 2024-03-05 @ 170.76, Exit: 2024-03-07 @ 169.15, Return: -0.94
Entry: 2024-03-08 @ 169.00, Exit: 2024-03-11 @ 172.94, Return: 2.33
Entry: 2024-03-12 @ 173.15, Exit: 2024-03-13 @ 172.77, Return: -0.22
Entry: 2024-03-14 @ 172.91, Exit: 2024-03-15 @ 171.17, Return: -1.01
Entry: 2024-03-18 @ 175.57, Exit: 2024-03-19 @ 174.34, Return: -0.70
Entry: 2024-03-20 @ 175.72, Exit: 2024-03-21 @ 177.05, Return: 0.76
Entry: 2024-03-22 @ 171.76, Exit: 2024-03-25 @ 170.57, Return: -0.70
Entry: 2024-03-26 @ 170.00, Exit: 2024-03-27 @ 170.41, Return: 0.24
Entry: 2024-03-28 @ 171.75, Exit: 2024-04-01 @ 171.19, Return: -0.33
Entry: 2024-04-02 @ 169.08, Exit: 2024-04-03 @ 168.79, Return: -0.17
Entry: 2024-04-04 @ 170.29, Exit: 2024-04-05 @ 169.59, Return: -0.41
Entry: 2024-04-08 @ 169.03, Exit: 2024-04-09 @ 168.70, Return: -0.20
Entry: 2024-04-10 @ 168.80, Exit: 2024-04-11 @ 168.34, Return: -0.27
Entry: 2024-04-12 @ 174.26, Exit: 2024-04-15 @ 175.36, Return: 0.63
Entry: 2024-04-16 @ 171.75, Exit: 2024-04-17 @ 169.61, Return: -1.25
Entry: 2024-04-18 @ 168.03, Exit: 2024-04-19 @ 166.21, Return: -1.08
Entry: 2024-04-22 @ 165.52, Exit: 2024-04-23 @ 165.35, Return: -0.10
Entry: 2024-04-24 @ 166.54, Exit: 2024-04-25 @ 169.53, Return: 1.79
Entry: 2024-04-26 @ 169.88, Exit: 2024-04-29 @ 173.37, Return: 2.05
Entry: 2024-04-30 @ 173.33, Exit: 2024-05-01 @ 169.58, Return: -2.16
Entry: 2024-05-02 @ 172.51, Exit: 2024-05-03 @ 186.65, Return: 8.19
Entry: 2024-05-06 @ 182.35, Exit: 2024-05-07 @ 183.45, Return: 0.60
Entry: 2024-05-08 @ 182.85, Exit: 2024-05-09 @ 182.56, Return: -0.16
Entry: 2024-05-10 @ 184.90, Exit: 2024-05-13 @ 185.44, Return: 0.29
Entry: 2024-05-14 @ 187.51, Exit: 2024-05-15 @ 187.91, Return: 0.21
Entry: 2024-05-16 @ 190.47, Exit: 2024-05-17 @ 189.51, Return: -0.50
Entry: 2024-05-20 @ 189.33, Exit: 2024-05-21 @ 191.09, Return: 0.93
Entry: 2024-05-22 @ 192.27, Exit: 2024-05-23 @ 190.98, Return: -0.67
Entry: 2024-05-24 @ 188.82, Exit: 2024-05-28 @ 191.51, Return: 1.42
Entry: 2024-05-29 @ 189.61, Exit: 2024-05-30 @ 190.76, Return: 0.61
Entry: 2024-05-31 @ 191.44, Exit: 2024-06-03 @ 192.90, Return: 0.76
Entry: 2024-06-04 @ 194.64, Exit: 2024-06-05 @ 195.40, Return: 0.39
Entry: 2024-06-06 @ 195.69, Exit: 2024-06-07 @ 194.65, Return: -0.53
Entry: 2024-06-10 @ 196.90, Exit: 2024-06-11 @ 193.65, Return: -1.65
Entry: 2024-06-12 @ 207.37, Exit: 2024-06-13 @ 214.74, Return: 3.55
Entry: 2024-06-14 @ 213.85, Exit: 2024-06-17 @ 213.37, Return: -0.22
Entry: 2024-06-18 @ 217.59, Exit: 2024-06-20 @ 213.93, Return: -1.68
Entry: 2024-06-21 @ 210.39, Exit: 2024-06-24 @ 207.72, Return: -1.27
Entry: 2024-06-25 @ 209.15, Exit: 2024-06-26 @ 211.50, Return: 1.12
Entry: 2024-06-27 @ 214.69, Exit: 2024-06-28 @ 215.77, Return: 0.50
Entry: 2024-07-01 @ 212.09, Exit: 2024-07-02 @ 216.15, Return: 1.91
Entry: 2024-07-03 @ 220.00, Exit: 2024-07-05 @ 221.65, Return: 0.75
Entry: 2024-07-08 @ 227.09, Exit: 2024-07-09 @ 227.93, Return: 0.37
Entry: 2024-07-10 @ 229.30, Exit: 2024-07-11 @ 231.39, Return: 0.91
Entry: 2024-07-12 @ 228.92, Exit: 2024-07-15 @ 236.48, Return: 3.30
Entry: 2024-07-16 @ 235.00, Exit: 2024-07-17 @ 229.45, Return: -2.36
Entry: 2024-07-18 @ 230.28, Exit: 2024-07-19 @ 224.82, Return: -2.37
Entry: 2024-07-22 @ 227.01, Exit: 2024-07-23 @ 224.37, Return: -1.17
Entry: 2024-07-24 @ 224.00, Exit: 2024-07-25 @ 218.93, Return: -2.26
Entry: 2024-07-26 @ 218.70, Exit: 2024-07-29 @ 216.96, Return: -0.80
Entry: 2024-07-30 @ 219.19, Exit: 2024-07-31 @ 221.44, Return: 1.03
Entry: 2024-08-01 @ 224.37, Exit: 2024-08-02 @ 219.15, Return: -2.33
Entry: 2024-08-05 @ 199.09, Exit: 2024-08-06 @ 205.30, Return: 3.12
Entry: 2024-08-07 @ 206.90, Exit: 2024-08-08 @ 213.11, Return: 3.00
Entry: 2024-08-09 @ 212.10, Exit: 2024-08-12 @ 216.07, Return: 1.87
Entry: 2024-08-13 @ 219.01, Exit: 2024-08-14 @ 220.57, Return: 0.71
Entry: 2024-08-15 @ 224.60, Exit: 2024-08-16 @ 223.92, Return: -0.30
Entry: 2024-08-19 @ 225.72, Exit: 2024-08-20 @ 225.77, Return: 0.02
Entry: 2024-08-21 @ 226.52, Exit: 2024-08-22 @ 227.79, Return: 0.56
Entry: 2024-08-23 @ 225.66, Exit: 2024-08-26 @ 226.76, Return: 0.49
Entry: 2024-08-27 @ 226.00, Exit: 2024-08-28 @ 227.92, Return: 0.85
Entry: 2024-08-29 @ 230.10, Exit: 2024-08-30 @ 230.19, Return: 0.04
Entry: 2024-09-03 @ 228.55, Exit: 2024-09-04 @ 221.66, Return: -3.01
Entry: 2024-09-05 @ 221.63, Exit: 2024-09-06 @ 223.95, Return: 1.05
Entry: 2024-09-09 @ 220.82, Exit: 2024-09-10 @ 218.92, Return: -0.86
Entry: 2024-09-11 @ 221.46, Exit: 2024-09-12 @ 222.50, Return: 0.47
Entry: 2024-09-13 @ 223.58, Exit: 2024-09-16 @ 216.54, Return: -3.15
Entry: 2024-09-17 @ 215.75, Exit: 2024-09-18 @ 217.55, Return: 0.83
Entry: 2024-09-19 @ 224.99, Exit: 2024-09-20 @ 229.97, Return: 2.21
Entry: 2024-09-23 @ 227.34, Exit: 2024-09-24 @ 228.65, Return: 0.57
Entry: 2024-09-25 @ 224.93, Exit: 2024-09-26 @ 227.30, Return: 1.05
Entry: 2024-09-27 @ 228.46, Exit: 2024-09-30 @ 230.04, Return: 0.69
Entry: 2024-10-01 @ 229.52, Exit: 2024-10-02 @ 225.89, Return: -1.58
Entry: 2024-10-03 @ 225.14, Exit: 2024-10-04 @ 227.90, Return: 1.23
Entry: 2024-10-07 @ 224.50, Exit: 2024-10-08 @ 224.30, Return: -0.09
Entry: 2024-10-09 @ 225.23, Exit: 2024-10-10 @ 227.78, Return: 1.13
Entry: 2024-10-11 @ 229.30, Exit: 2024-10-14 @ 228.70, Return: -0.26
Entry: 2024-10-15 @ 233.61, Exit: 2024-10-16 @ 231.60, Return: -0.86
Entry: 2024-10-17 @ 233.43, Exit: 2024-10-18 @ 236.18, Return: 1.18
Entry: 2024-10-21 @ 234.45, Exit: 2024-10-22 @ 233.89, Return: -0.24
Entry: 2024-10-23 @ 234.08, Exit: 2024-10-24 @ 229.98, Return: -1.75
Entry: 2024-10-25 @ 229.74, Exit: 2024-10-28 @ 233.32, Return: 1.56
Entry: 2024-10-29 @ 233.10, Exit: 2024-10-30 @ 232.61, Return: -0.21
Entry: 2024-10-31 @ 229.34, Exit: 2024-11-01 @ 220.97, Return: -3.65
Entry: 2024-11-04 @ 220.99, Exit: 2024-11-05 @ 221.80, Return: 0.36
Entry: 2024-11-06 @ 222.61, Exit: 2024-11-07 @ 224.63, Return: 0.91
Entry: 2024-11-08 @ 227.17, Exit: 2024-11-11 @ 225.00, Return: -0.96
Entry: 2024-11-12 @ 224.55, Exit: 2024-11-13 @ 224.01, Return: -0.24
Entry: 2024-11-14 @ 225.02, Exit: 2024-11-15 @ 226.40, Return: 0.61
Entry: 2024-11-18 @ 225.25, Exit: 2024-11-19 @ 226.98, Return: 0.77
Entry: 2024-11-20 @ 228.06, Exit: 2024-11-21 @ 228.88, Return: 0.36
Entry: 2024-11-22 @ 228.06, Exit: 2024-11-25 @ 231.46, Return: 1.49
Entry: 2024-11-26 @ 233.33, Exit: 2024-11-27 @ 234.47, Return: 0.49
Entry: 2024-11-29 @ 234.81, Exit: 2024-12-02 @ 237.27, Return: 1.05
Entry: 2024-12-03 @ 239.81, Exit: 2024-12-04 @ 242.87, Return: 1.28
Entry: 2024-12-05 @ 243.99, Exit: 2024-12-06 @ 242.91, Return: -0.44
Entry: 2024-12-09 @ 241.83, Exit: 2024-12-10 @ 246.89, Return: 2.09
Entry: 2024-12-11 @ 247.96, Exit: 2024-12-12 @ 246.89, Return: -0.43
Entry: 2024-12-13 @ 247.82, Exit: 2024-12-16 @ 247.99, Return: 0.07
Entry: 2024-12-17 @ 250.08, Exit: 2024-12-18 @ 252.16, Return: 0.83
Entry: 2024-12-19 @ 247.50, Exit: 2024-12-20 @ 248.04, Return: 0.22
Entry: 2024-12-23 @ 254.77, Exit: 2024-12-24 @ 255.49, Return: 0.28
Entry: 2024-12-26 @ 258.19, Exit: 2024-12-27 @ 257.83, Return: -0.14
Entry: 2024-12-30 @ 252.23, Exit: 2024-12-31 @ 252.44, Return: 0.08
Entry: 2025-01-02 @ 248.93, Exit: 2025-01-03 @ 243.36, Return: -2.24
Entry: 2025-01-06 @ 244.31, Exit: 2025-01-07 @ 242.98, Return: -0.54
Entry: 2025-01-08 @ 241.92, Exit: 2025-01-10 @ 240.01, Return: -0.79
Entry: 2025-01-13 @ 233.53, Exit: 2025-01-14 @ 234.75, Return: 0.52
Entry: 2025-01-15 @ 234.64, Exit: 2025-01-16 @ 237.35, Return: 1.16
Entry: 2025-01-17 @ 232.12, Exit: 2025-01-21 @ 224.00, Return: -3.50
Entry: 2025-01-22 @ 219.79, Exit: 2025-01-23 @ 224.74, Return: 2.25
Entry: 2025-01-24 @ 224.78, Exit: 2025-01-27 @ 224.02, Return: -0.34
Entry: 2025-01-28 @ 230.85, Exit: 2025-01-29 @ 234.12, Return: 1.42
Entry: 2025-01-30 @ 238.67, Exit: 2025-01-31 @ 247.19, Return: 3.57
Entry: 2025-02-03 @ 229.99, Exit: 2025-02-04 @ 227.25, Return: -1.19
Entry: 2025-02-05 @ 228.53, Exit: 2025-02-06 @ 231.29, Return: 1.21
Entry: 2025-02-07 @ 232.60, Exit: 2025-02-10 @ 229.57, Return: -1.30
Entry: 2025-02-11 @ 228.20, Exit: 2025-02-12 @ 231.20, Return: 1.31
Entry: 2025-02-13 @ 236.91, Exit: 2025-02-14 @ 241.25, Return: 1.83
Entry: 2025-02-18 @ 244.15, Exit: 2025-02-19 @ 244.66, Return: 0.21
Entry: 2025-02-20 @ 244.94, Exit: 2025-02-21 @ 245.95, Return: 0.41
Entry: 2025-02-24 @ 244.93, Exit: 2025-02-25 @ 248.00, Return: 1.26
Entry: 2025-02-26 @ 244.33, Exit: 2025-02-27 @ 239.41, Return: -2.01
Entry: 2025-02-28 @ 236.95, Exit: 2025-03-03 @ 241.79, Return: 2.04
Entry: 2025-03-04 @ 237.71, Exit: 2025-03-05 @ 235.42, Return: -0.96
Entry: 2025-03-06 @ 234.44, Exit: 2025-03-07 @ 235.11, Return: 0.29
Entry: 2025-03-10 @ 235.54, Exit: 2025-03-11 @ 223.81, Return: -4.98
Entry: 2025-03-12 @ 220.14, Exit: 2025-03-13 @ 215.95, Return: -1.90
Entry: 2025-03-14 @ 211.25, Exit: 2025-03-17 @ 213.31, Return: 0.98
Entry: 2025-03-18 @ 214.16, Exit: 2025-03-19 @ 214.22, Return: 0.03
Entry: 2025-03-20 @ 213.99, Exit: 2025-03-21 @ 211.56, Return: -1.14
Entry: 2025-03-24 @ 221.00, Exit: 2025-03-25 @ 220.77, Return: -0.10
Entry: 2025-03-26 @ 223.51, Exit: 2025-03-27 @ 221.39, Return: -0.95
Entry: 2025-03-28 @ 221.67, Exit: 2025-03-31 @ 217.01, Return: -2.10
Entry: 2025-04-01 @ 219.81, Exit: 2025-04-02 @ 221.32, Return: 0.69
Entry: 2025-04-03 @ 205.54, Exit: 2025-04-04 @ 193.89, Return: -5.67
Entry: 2025-04-07 @ 177.20, Exit: 2025-04-08 @ 186.70, Return: 5.36
Entry: 2025-04-09 @ 171.95, Exit: 2025-04-10 @ 189.07, Return: 9.95
Entry: 2025-04-11 @ 186.10, Exit: 2025-04-14 @ 211.44, Return: 13.62
Entry: 2025-04-15 @ 201.86, Exit: 2025-04-16 @ 198.36, Return: -1.73
Entry: 2025-04-17 @ 197.20, Exit: 2025-04-21 @ 193.27, Return: -2.00
Entry: 2025-04-22 @ 196.12, Exit: 2025-04-23 @ 206.00, Return: 5.04
Entry: 2025-04-24 @ 204.89, Exit: 2025-04-25 @ 206.37, Return: 0.72
Entry: 2025-04-28 @ 210.00, Exit: 2025-04-29 @ 208.69, Return: -0.62
Entry: 2025-04-30 @ 209.30, Exit: 2025-05-01 @ 209.08, Return: -0.11
Entry: 2025-05-02 @ 206.09, Exit: 2025-05-05 @ 203.10, Return: -1.45
Entry: 2025-05-06 @ 198.21, Exit: 2025-05-07 @ 199.17, Return: 0.48
Entry: 2025-05-08 @ 197.72, Exit: 2025-05-09 @ 199.00, Return: 0.65
Entry: 2025-05-12 @ 210.97, Exit: 2025-05-13 @ 210.43, Return: -0.26
Entry: 2025-05-14 @ 212.43, Exit: 2025-05-15 @ 210.95, Return: -0.70
Entry: 2025-05-16 @ 212.36, Exit: 2025-05-19 @ 207.91, Return: -2.10
Entry: 2025-05-20 @ 207.67, Exit: 2025-05-21 @ 205.17, Return: -1.20
Entry: 2025-05-22 @ 200.71, Exit: 2025-05-23 @ 193.67, Return: -3.51
Entry: 2025-05-27 @ 198.30, Exit: 2025-05-28 @ 200.59, Return: 1.15
Entry: 2025-05-29 @ 203.58, Exit: 2025-05-30 @ 199.37, Return: -2.07
Entry: 2025-06-02 @ 200.28, Exit: 2025-06-03 @ 201.35, Return: 0.53
Entry: 2025-06-04 @ 202.91, Exit: 2025-06-05 @ 203.50, Return: 0.29
Entry: 2025-06-06 @ 203.00, Exit: 2025-06-09 @ 204.39, Return: 0.68
Entry: 2025-06-10 @ 200.60, Exit: 2025-06-11 @ 203.50, Return: 1.45
Entry: 2025-06-12 @ 199.08, Exit: 2025-06-13 @ 199.73, Return: 0.33
Entry: 2025-06-16 @ 197.30, Exit: 2025-06-17 @ 197.20, Return: -0.05
Entry: 2025-06-18 @ 195.94, Exit: 2025-06-20 @ 198.24, Return: 1.17
Entry: 2025-06-23 @ 201.63, Exit: 2025-06-24 @ 202.59, Return: 0.48
Entry: 2025-06-25 @ 201.45, Exit: 2025-06-26 @ 201.43, Return: -0.01
Entry: 2025-06-27 @ 201.89, Exit: 2025-06-30 @ 202.01, Return: 0.06
Entry: 2025-07-01 @ 206.67, Exit: 2025-07-02 @ 208.91, Return: 1.09
Entry: 2025-07-03 @ 212.15, Exit: 2025-07-07 @ 212.68, Return: 0.25
Entry: 2025-07-08 @ 210.10, Exit: 2025-07-09 @ 209.53, Return: -0.27
Entry: 2025-07-10 @ 210.51, Exit: 2025-07-11 @ 210.57, Return: 0.03
Entry: 2025-07-14 @ 209.93, Exit: 2025-07-15 @ 209.22, Return: -0.34
Entry: 2025-07-16 @ 210.30, Exit: 2025-07-17 @ 210.57, Return: 0.13
Entry: 2025-07-18 @ 210.87, Exit: 2025-07-21 @ 212.10, Return: 0.58
Entry: 2025-07-22 @ 213.14, Exit: 2025-07-23 @ 215.00, Return: 0.87
Entry: 2025-07-24 @ 213.90, Exit: 2025-07-25 @ 214.70, Return: 0.37
Entry: 2025-07-28 @ 214.03, Exit: 2025-07-29 @ 214.18, Return: 0.07
Entry: 2025-07-30 @ 211.90, Exit: 2025-07-31 @ 208.49, Return: -1.61
```

</details>

## Tech Stack

-   **AI & Python Service**: Python, LangChain, FastAPI, Ollama, ChromaDB, Google AI Embeddings
-   **Backtesting Engine**: Java 17+, Picocli, Maven
-   **Data APIs**: Polygon.io (News), EODHD/CSV (Prices)

## Potential Use Cases

-   **Strategy Prototyping**: Rapidly test and validate new trading ideas based on news sentiment without writing complex, rule-based parsers.
-   **Alpha Factor Research**: Use the AI-generated signal as a novel "alpha factor" that can be integrated into more complex quantitative models.
-   **LLM & Prompt Benchmarking**: The system serves as a realistic testbed for comparing the performance of different LLMs and prompt engineering techniques on a financial task.
-   **Educational Tool**: Demonstrates a practical, end-to-end application of RAG, event-driven systems, and quantitative finance principles.
-   **Foundation for Live Trading**: The modular architecture allows the historical backtester to be adapted for real-time paper or live trading by connecting to a live data stream.

## Quick Start

1.  **Clone & Setup Python**:
    ```bash
    git clone https://github.com/thenakulmistry/RetroTrade.git
    cd RetroTrade/rag_service
    pip install -r requirements.txt
    ```
2.  **Configure**: Add API keys to `.env` files in `rag_service/` and the project root directory.

3.  **Run Services**:
    ```bash
    # Pull the local LLM + (optional) local embedding model
    ollama pull gemma3:1b
    ollama pull nomic-embed-text

    # Start Ollama runtime
    ollama serve

    # Ingest news data (re-run when ingestion settings/model/provider change)
    python ingest_data.py

    # Start the AI service
    uvicorn rag_service:app --host 127.0.0.1 --port 8000 --reload
    ```
4.  **Run Backtest**: In a new terminal, run the compiled Java application.
    ```bash
    mvn clean package -DskipTests
    java -jar target/retrotrade-1.0.jar --symbol=AAPL --start=2020-01-01 --end=2022-08-12 --file=apple_data.csv
    ```

## Future Enhancements

-   Multi-asset portfolio backtesting.
-   Implement more advanced position sizing models.
-   Develop a web-based dashboard for interactive analysis.

## Point-in-Time Retrieval Note

-   The RAG service is configured to retrieve only news published on or before the **previous day** of the signal date.
-   To use this behavior correctly, re-run `python ingest_data.py` so Chroma stores article metadata like `published_date`.
-   Re-ingestion now rebuilds `chroma_db_full` to avoid stale or duplicate vectors.
-   News is indexed per ticker symbol, so retrieval by symbol is more accurate when one article mentions multiple companies.

## Embedding Provider Selection

-   You can choose embeddings provider via `.env`:
    -   `EMBEDDING_PROVIDER=google` and `GOOGLE_EMBEDDING_MODEL=models/gemini-embedding-001`
    -   `EMBEDDING_PROVIDER=ollama` and `OLLAMA_EMBEDDING_MODEL=nomic-embed-text`
-   Use the same provider/model for both ingestion and service startup to keep vector search compatible.
-   If you want to try `gemma3:1b` for local embeddings, set `OLLAMA_EMBEDDING_MODEL=gemma3:1b` (but a dedicated embedding model like `nomic-embed-text` is usually more reliable for retrieval quality).