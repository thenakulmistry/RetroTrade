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
Total Return: 435.10%
Sharpe Ratio: 1.06
Max Drawdown: -19.60%
Win Rate: 54.88%
```

<details>
<summary><strong>Click to view full trade log (257 trades)</strong></summary>

```
---Trade log---
Entry: 2019-01-02 @ 154.89, Exit: 2019-02-07 @ 172.40, Return: 11.30
Entry: 2019-02-08 @ 168.99, Exit: 2019-04-08 @ 196.42, Return: 16.23
Entry: 2019-04-11 @ 200.85, Exit: 2019-04-26 @ 204.90, Return: 2.02
Entry: 2019-04-30 @ 203.06, Exit: 2019-05-16 @ 189.91, Return: -6.48
Entry: 2019-05-21 @ 185.22, Exit: 2019-06-21 @ 198.80, Return: 7.33
Entry: 2019-06-24 @ 198.54, Exit: 2019-07-10 @ 201.85, Return: 1.67
Entry: 2019-07-11 @ 203.31, Exit: 2019-07-17 @ 204.05, Return: 0.36
Entry: 2019-07-18 @ 204.00, Exit: 2019-08-30 @ 210.16, Return: 3.02
Entry: 2019-09-04 @ 208.39, Exit: 2019-09-18 @ 221.06, Return: 6.08
Entry: 2019-09-19 @ 222.01, Exit: 2019-09-26 @ 220.00, Return: -0.91
Entry: 2019-09-30 @ 220.90, Exit: 2019-12-23 @ 280.53, Return: 26.99
Entry: 2019-12-24 @ 284.69, Exit: 2020-02-18 @ 315.36, Return: 10.77
Entry: 2020-02-19 @ 320.00, Exit: 2020-02-20 @ 322.63, Return: 0.82
Entry: 2020-02-21 @ 318.62, Exit: 2020-02-24 @ 297.26, Return: -6.70
Entry: 2020-02-25 @ 300.95, Exit: 2020-03-16 @ 241.95, Return: -19.60
Entry: 2020-03-17 @ 247.51, Exit: 2020-05-20 @ 316.68, Return: 27.95
Entry: 2020-05-21 @ 318.66, Exit: 2020-06-09 @ 332.14, Return: 4.23
Entry: 2020-06-10 @ 347.90, Exit: 2020-06-23 @ 364.00, Return: 4.63
Entry: 2020-06-24 @ 365.00, Exit: 2020-07-16 @ 386.25, Return: 5.82
Entry: 2020-07-17 @ 387.95, Exit: 2020-07-20 @ 385.67, Return: -0.59
Entry: 2020-07-21 @ 396.69, Exit: 2020-07-24 @ 363.95, Return: -8.25
Entry: 2020-07-27 @ 374.84, Exit: 2020-08-17 @ 464.25, Return: 23.85
Entry: 2020-08-18 @ 457.41, Exit: 2020-08-19 @ 463.93, Return: 1.43
Entry: 2020-08-20 @ 463.00, Exit: 2020-08-24 @ 514.79, Return: 11.19
Entry: 2020-08-25 @ 498.79, Exit: 2020-08-26 @ 504.72, Return: 1.19
Entry: 2020-08-31 @ 127.58, Exit: 2020-09-14 @ 114.72, Return: -10.08
Entry: 2020-09-15 @ 118.33, Exit: 2020-09-21 @ 104.54, Return: -11.65
Entry: 2020-09-22 @ 112.68, Exit: 2020-10-02 @ 112.89, Return: 0.19
Entry: 2020-10-05 @ 113.91, Exit: 2020-10-06 @ 115.70, Return: 1.57
Entry: 2020-10-07 @ 114.62, Exit: 2020-10-08 @ 116.25, Return: 1.42
Entry: 2020-10-09 @ 115.28, Exit: 2020-10-16 @ 121.28, Return: 5.20
Entry: 2020-10-19 @ 119.96, Exit: 2020-10-20 @ 116.20, Return: -3.13
Entry: 2020-10-21 @ 116.67, Exit: 2020-10-22 @ 117.45, Return: 0.67
Entry: 2020-10-23 @ 116.39, Exit: 2020-10-28 @ 115.05, Return: -1.15
Entry: 2020-10-29 @ 112.37, Exit: 2020-10-30 @ 111.06, Return: -1.17
Entry: 2020-11-02 @ 109.11, Exit: 2020-11-06 @ 118.32, Return: 8.44
Entry: 2020-11-10 @ 115.55, Exit: 2020-11-23 @ 117.18, Return: 1.41
Entry: 2020-11-24 @ 113.91, Exit: 2021-01-04 @ 133.52, Return: 17.22
Entry: 2021-01-05 @ 128.89, Exit: 2021-01-08 @ 132.43, Return: 2.75
Entry: 2021-01-11 @ 129.19, Exit: 2021-01-12 @ 128.50, Return: -0.53
Entry: 2021-01-13 @ 128.76, Exit: 2021-01-15 @ 128.78, Return: 0.02
Entry: 2021-01-19 @ 127.78, Exit: 2021-01-21 @ 133.80, Return: 4.71
Entry: 2021-01-22 @ 136.28, Exit: 2021-01-27 @ 143.43, Return: 5.25
Entry: 2021-01-28 @ 139.52, Exit: 2021-02-04 @ 136.30, Return: -2.31
Entry: 2021-02-05 @ 137.35, Exit: 2021-02-16 @ 135.49, Return: -1.35
Entry: 2021-02-17 @ 131.25, Exit: 2021-02-22 @ 128.01, Return: -2.47
Entry: 2021-02-23 @ 123.76, Exit: 2021-03-02 @ 128.41, Return: 3.76
Entry: 2021-03-03 @ 124.81, Exit: 2021-03-04 @ 121.75, Return: -2.45
Entry: 2021-03-05 @ 120.98, Exit: 2021-03-08 @ 120.93, Return: -0.04
Entry: 2021-03-09 @ 119.03, Exit: 2021-03-10 @ 121.69, Return: 2.23
Entry: 2021-03-11 @ 122.54, Exit: 2021-03-15 @ 121.41, Return: -0.92
Entry: 2021-03-16 @ 125.70, Exit: 2021-03-18 @ 122.88, Return: -2.24
Entry: 2021-03-19 @ 119.90, Exit: 2021-03-22 @ 120.33, Return: 0.36
Entry: 2021-03-23 @ 123.33, Exit: 2021-03-24 @ 122.82, Return: -0.41
Entry: 2021-03-25 @ 119.54, Exit: 2021-03-31 @ 121.65, Return: 1.77
Entry: 2021-04-01 @ 123.66, Exit: 2021-04-05 @ 123.87, Return: 0.17
Entry: 2021-04-06 @ 126.50, Exit: 2021-04-07 @ 125.83, Return: -0.53
Entry: 2021-04-08 @ 128.95, Exit: 2021-04-09 @ 129.80, Return: 0.66
Entry: 2021-04-13 @ 132.44, Exit: 2021-04-16 @ 134.30, Return: 1.40
Entry: 2021-04-22 @ 133.04, Exit: 2021-04-26 @ 134.83, Return: 1.35
Entry: 2021-04-28 @ 134.31, Exit: 2021-04-29 @ 136.47, Return: 1.61
Entry: 2021-05-03 @ 132.04, Exit: 2021-05-04 @ 131.19, Return: -0.64
Entry: 2021-05-05 @ 129.20, Exit: 2021-05-07 @ 130.85, Return: 1.28
Entry: 2021-05-10 @ 129.41, Exit: 2021-05-11 @ 123.50, Return: -4.57
Entry: 2021-05-12 @ 123.40, Exit: 2021-05-13 @ 124.58, Return: 0.96
Entry: 2021-05-14 @ 126.25, Exit: 2021-05-17 @ 126.82, Return: 0.45
Entry: 2021-05-18 @ 126.56, Exit: 2021-05-19 @ 123.16, Return: -2.69
Entry: 2021-05-20 @ 125.23, Exit: 2021-05-21 @ 127.82, Return: 2.07
Entry: 2021-05-24 @ 126.01, Exit: 2021-05-26 @ 126.96, Return: 0.75
Entry: 2021-05-27 @ 126.44, Exit: 2021-05-28 @ 125.57, Return: -0.69
Entry: 2021-06-01 @ 125.08, Exit: 2021-06-02 @ 124.28, Return: -0.64
Entry: 2021-06-03 @ 124.68, Exit: 2021-06-14 @ 127.82, Return: 2.52
Entry: 2021-06-15 @ 129.94, Exit: 2021-06-16 @ 130.37, Return: 0.33
Entry: 2021-06-17 @ 129.80, Exit: 2021-06-28 @ 133.41, Return: 2.78
Entry: 2021-06-29 @ 134.80, Exit: 2021-07-07 @ 143.54, Return: 6.48
Entry: 2021-07-08 @ 141.58, Exit: 2021-07-12 @ 146.21, Return: 3.27
Entry: 2021-07-13 @ 144.03, Exit: 2021-07-16 @ 148.46, Return: 3.08
Entry: 2021-07-19 @ 143.75, Exit: 2021-07-23 @ 147.55, Return: 2.64
Entry: 2021-07-27 @ 149.12, Exit: 2021-07-28 @ 144.81, Return: -2.89
Entry: 2021-07-29 @ 144.69, Exit: 2021-07-30 @ 144.38, Return: -0.21
Entry: 2021-08-02 @ 146.36, Exit: 2021-08-03 @ 145.81, Return: -0.38
Entry: 2021-08-04 @ 147.27, Exit: 2021-08-09 @ 146.20, Return: -0.73
Entry: 2021-08-10 @ 146.44, Exit: 2021-08-11 @ 146.05, Return: -0.27
Entry: 2021-08-12 @ 146.19, Exit: 2021-08-16 @ 148.54, Return: 1.60
Entry: 2021-08-17 @ 150.23, Exit: 2021-08-18 @ 149.80, Return: -0.29
Entry: 2021-08-19 @ 145.03, Exit: 2021-08-20 @ 147.44, Return: 1.66
Entry: 2021-08-23 @ 148.31, Exit: 2021-08-24 @ 149.45, Return: 0.77
Entry: 2021-08-25 @ 149.81, Exit: 2021-08-30 @ 149.00, Return: -0.54
Entry: 2021-08-31 @ 152.66, Exit: 2021-09-01 @ 152.83, Return: 0.11
Entry: 2021-09-02 @ 153.87, Exit: 2021-09-07 @ 154.97, Return: 0.71
Entry: 2021-09-08 @ 156.98, Exit: 2021-09-13 @ 150.63, Return: -4.05
Entry: 2021-09-14 @ 150.35, Exit: 2021-09-15 @ 148.56, Return: -1.19
Entry: 2021-09-16 @ 148.44, Exit: 2021-09-17 @ 148.82, Return: 0.26
Entry: 2021-09-20 @ 143.80, Exit: 2021-09-24 @ 145.66, Return: 1.29
Entry: 2021-09-27 @ 145.47, Exit: 2021-10-07 @ 143.06, Return: -1.66
Entry: 2021-10-08 @ 144.03, Exit: 2021-10-11 @ 142.27, Return: -1.22
Entry: 2021-10-12 @ 143.23, Exit: 2021-10-14 @ 142.11, Return: -0.78
Entry: 2021-10-15 @ 143.77, Exit: 2021-10-20 @ 148.70, Return: 3.43
Entry: 2021-10-21 @ 148.81, Exit: 2021-10-25 @ 148.68, Return: -0.09
Entry: 2021-10-26 @ 149.33, Exit: 2021-10-27 @ 149.36, Return: 0.02
Entry: 2021-10-28 @ 149.82, Exit: 2021-10-29 @ 147.22, Return: -1.74
Entry: 2021-11-01 @ 148.99, Exit: 2021-11-02 @ 148.66, Return: -0.22
Entry: 2021-11-03 @ 150.39, Exit: 2021-11-05 @ 151.89, Return: 1.00
Entry: 2021-11-08 @ 151.41, Exit: 2021-11-09 @ 150.20, Return: -0.80
Entry: 2021-11-10 @ 150.02, Exit: 2021-11-11 @ 148.96, Return: -0.71
Entry: 2021-11-12 @ 148.43, Exit: 2021-11-15 @ 150.37, Return: 1.31
Entry: 2021-11-16 @ 149.94, Exit: 2021-11-17 @ 151.00, Return: 0.70
Entry: 2021-11-18 @ 153.71, Exit: 2021-11-19 @ 157.65, Return: 2.56
Entry: 2021-11-22 @ 161.68, Exit: 2021-11-23 @ 161.12, Return: -0.35
Entry: 2021-11-24 @ 160.75, Exit: 2021-12-02 @ 158.74, Return: -1.25
Entry: 2021-12-03 @ 164.02, Exit: 2021-12-07 @ 169.08, Return: 3.08
Entry: 2021-12-08 @ 172.13, Exit: 2021-12-14 @ 175.25, Return: 1.82
Entry: 2021-12-15 @ 175.11, Exit: 2021-12-16 @ 179.28, Return: 2.38
Entry: 2021-12-17 @ 169.93, Exit: 2021-12-23 @ 175.85, Return: 3.48
Entry: 2021-12-27 @ 177.09, Exit: 2021-12-28 @ 180.16, Return: 1.74
Entry: 2021-12-29 @ 179.33, Exit: 2022-01-12 @ 176.12, Return: -1.79
Entry: 2022-01-13 @ 175.78, Exit: 2022-01-20 @ 166.98, Return: -5.01
Entry: 2022-01-21 @ 164.42, Exit: 2022-01-24 @ 160.02, Return: -2.67
Entry: 2022-01-25 @ 158.98, Exit: 2022-02-02 @ 174.75, Return: 9.92
Entry: 2022-02-03 @ 174.48, Exit: 2022-02-07 @ 172.86, Return: -0.93
Entry: 2022-02-08 @ 171.73, Exit: 2022-02-09 @ 176.05, Return: 2.52
Entry: 2022-02-10 @ 174.14, Exit: 2022-02-17 @ 171.03, Return: -1.79
Entry: 2022-02-18 @ 169.82, Exit: 2022-02-23 @ 165.54, Return: -2.52
Entry: 2022-02-24 @ 152.58, Exit: 2022-02-28 @ 163.06, Return: 6.87
Entry: 2022-03-01 @ 164.70, Exit: 2022-03-03 @ 168.47, Return: 2.29
Entry: 2022-03-04 @ 164.49, Exit: 2022-03-10 @ 160.20, Return: -2.61
Entry: 2022-03-11 @ 158.93, Exit: 2022-03-14 @ 151.45, Return: -4.71
Entry: 2022-03-15 @ 150.90, Exit: 2022-03-16 @ 157.05, Return: 4.08
Entry: 2022-03-17 @ 158.61, Exit: 2022-03-18 @ 160.51, Return: 1.20
Entry: 2022-03-21 @ 163.51, Exit: 2022-03-23 @ 167.99, Return: 2.74
Entry: 2022-03-24 @ 171.06, Exit: 2022-03-28 @ 172.17, Return: 0.65
Entry: 2022-03-29 @ 176.69, Exit: 2022-03-31 @ 177.84, Return: 0.65
Entry: 2022-04-01 @ 174.03, Exit: 2022-04-05 @ 177.50, Return: 1.99
Entry: 2022-04-06 @ 172.36, Exit: 2022-04-07 @ 171.16, Return: -0.70
Entry: 2022-04-08 @ 171.78, Exit: 2022-04-19 @ 165.02, Return: -3.94
Entry: 2022-04-20 @ 168.76, Exit: 2022-04-25 @ 161.12, Return: -4.53
Entry: 2022-04-27 @ 155.91, Exit: 2022-04-29 @ 161.84, Return: 3.80
Entry: 2022-05-02 @ 156.71, Exit: 2022-05-03 @ 158.15, Return: 0.92
Entry: 2022-05-04 @ 159.67, Exit: 2022-05-05 @ 163.85, Return: 2.62
Entry: 2022-05-06 @ 156.01, Exit: 2022-05-10 @ 155.52, Return: -0.31
Entry: 2022-05-11 @ 153.50, Exit: 2022-05-12 @ 142.77, Return: -6.99
Entry: 2022-05-13 @ 144.59, Exit: 2022-05-16 @ 145.55, Return: 0.66
Entry: 2022-05-17 @ 148.86, Exit: 2022-05-18 @ 146.85, Return: -1.35
Entry: 2022-05-19 @ 139.88, Exit: 2022-05-20 @ 139.09, Return: -0.56
Entry: 2022-05-23 @ 137.79, Exit: 2022-05-24 @ 140.81, Return: 2.19
Entry: 2022-05-25 @ 138.43, Exit: 2022-05-26 @ 137.39, Return: -0.75
Entry: 2022-05-27 @ 145.39, Exit: 2022-05-31 @ 149.07, Return: 2.53
Entry: 2022-06-01 @ 149.90, Exit: 2022-06-02 @ 147.83, Return: -1.38
Entry: 2022-06-03 @ 146.90, Exit: 2022-06-06 @ 147.03, Return: 0.09
Entry: 2022-06-07 @ 144.35, Exit: 2022-06-08 @ 148.58, Return: 2.93
Entry: 2022-06-09 @ 147.08, Exit: 2022-06-13 @ 132.87, Return: -9.66
Entry: 2022-06-14 @ 133.13, Exit: 2022-06-16 @ 132.08, Return: -0.79
Entry: 2022-06-17 @ 130.07, Exit: 2022-06-22 @ 134.79, Return: 3.63
Entry: 2022-06-23 @ 136.82, Exit: 2022-06-28 @ 142.13, Return: 3.88
Entry: 2022-06-29 @ 137.46, Exit: 2022-07-01 @ 136.04, Return: -1.03
Entry: 2022-07-05 @ 137.77, Exit: 2022-07-07 @ 143.29, Return: 4.01
Entry: 2022-07-08 @ 145.27, Exit: 2022-07-11 @ 145.67, Return: 0.28
Entry: 2022-07-12 @ 145.76, Exit: 2022-07-13 @ 142.99, Return: -1.90
Entry: 2022-07-14 @ 144.08, Exit: 2022-07-22 @ 155.39, Return: 7.85
Entry: 2022-07-25 @ 154.01, Exit: 2022-08-03 @ 160.84, Return: 4.43
Entry: 2022-08-04 @ 166.01, Exit: 2022-08-05 @ 163.21, Return: -1.68
Entry: 2022-08-08 @ 166.37, Exit: 2022-08-10 @ 167.68, Return: 0.79
Entry: 2022-08-11 @ 170.06, Exit: 2022-08-15 @ 171.52, Return: 0.86
Entry: 2022-08-16 @ 172.78, Exit: 2022-08-17 @ 172.77, Return: -0.01
Entry: 2022-08-18 @ 173.75, Exit: 2022-08-19 @ 173.03, Return: -0.41
Entry: 2022-08-22 @ 169.69, Exit: 2022-08-23 @ 167.08, Return: -1.54
Entry: 2022-08-24 @ 167.32, Exit: 2022-08-25 @ 168.78, Return: 0.87
Entry: 2022-08-26 @ 170.57, Exit: 2022-08-29 @ 161.15, Return: -5.53
Entry: 2022-08-30 @ 162.13, Exit: 2022-08-31 @ 160.31, Return: -1.13
Entry: 2022-09-01 @ 156.64, Exit: 2022-09-06 @ 156.47, Return: -0.11
Entry: 2022-09-07 @ 154.83, Exit: 2022-09-08 @ 154.64, Return: -0.12
Entry: 2022-09-09 @ 155.47, Exit: 2022-09-12 @ 159.59, Return: 2.65
Entry: 2022-09-13 @ 159.90, Exit: 2022-09-14 @ 154.79, Return: -3.20
Entry: 2022-09-15 @ 154.65, Exit: 2022-09-21 @ 157.34, Return: 1.74
Entry: 2022-09-22 @ 152.38, Exit: 2022-09-23 @ 151.19, Return: -0.78
Entry: 2022-09-26 @ 149.66, Exit: 2022-09-27 @ 152.74, Return: 2.06
Entry: 2022-09-28 @ 147.64, Exit: 2022-09-29 @ 146.10, Return: -1.04
Entry: 2022-09-30 @ 141.28, Exit: 2022-10-04 @ 145.03, Return: 2.65
Entry: 2022-10-05 @ 144.08, Exit: 2022-10-07 @ 142.54, Return: -1.07
Entry: 2022-10-10 @ 140.42, Exit: 2022-10-12 @ 139.13, Return: -0.92
Entry: 2022-10-13 @ 134.99, Exit: 2022-10-14 @ 144.31, Return: 6.90
Entry: 2022-10-17 @ 141.07, Exit: 2022-10-18 @ 145.49, Return: 3.14
Entry: 2022-10-19 @ 141.69, Exit: 2022-10-20 @ 143.02, Return: 0.94
Entry: 2022-10-21 @ 142.87, Exit: 2022-10-25 @ 150.09, Return: 5.05
Entry: 2022-10-26 @ 150.96, Exit: 2022-10-27 @ 148.07, Return: -1.91
Entry: 2022-10-28 @ 148.20, Exit: 2022-10-31 @ 153.16, Return: 3.34
Entry: 2022-11-01 @ 155.08, Exit: 2022-11-02 @ 148.95, Return: -3.96
Entry: 2022-11-03 @ 142.06, Exit: 2022-11-04 @ 142.09, Return: 0.02
Entry: 2022-11-07 @ 137.11, Exit: 2022-11-09 @ 138.50, Return: 1.01
Entry: 2022-11-10 @ 141.24, Exit: 2022-11-16 @ 149.13, Return: 5.59
Entry: 2022-11-17 @ 146.43, Exit: 2022-11-18 @ 152.31, Return: 4.01
Entry: 2022-11-21 @ 150.16, Exit: 2022-11-22 @ 148.13, Return: -1.35
Entry: 2022-11-23 @ 149.45, Exit: 2022-11-28 @ 145.14, Return: -2.88
Entry: 2022-11-29 @ 144.29, Exit: 2022-12-01 @ 148.21, Return: 2.72
Entry: 2022-12-02 @ 145.96, Exit: 2022-12-05 @ 147.77, Return: 1.24
Entry: 2022-12-06 @ 147.08, Exit: 2022-12-08 @ 142.36, Return: -3.21
Entry: 2022-12-09 @ 142.34, Exit: 2022-12-12 @ 142.70, Return: 0.25
Entry: 2022-12-13 @ 149.50, Exit: 2022-12-16 @ 136.69, Return: -8.57
Entry: 2022-12-19 @ 135.11, Exit: 2022-12-20 @ 131.39, Return: -2.75
Entry: 2022-12-21 @ 132.98, Exit: 2022-12-22 @ 134.35, Return: 1.03
Entry: 2022-12-23 @ 130.92, Exit: 2022-12-27 @ 131.38, Return: 0.35
Entry: 2022-12-28 @ 129.67, Exit: 2022-12-29 @ 127.99, Return: -1.30
Entry: 2022-12-30 @ 128.41, Exit: 2023-01-06 @ 126.01, Return: -1.87
Entry: 2023-01-09 @ 130.47, Exit: 2023-01-12 @ 133.88, Return: 2.62
Entry: 2023-01-13 @ 132.03, Exit: 2023-01-17 @ 134.83, Return: 2.12
Entry: 2023-01-18 @ 136.82, Exit: 2023-01-23 @ 138.12, Return: 0.95
Entry: 2023-01-24 @ 140.31, Exit: 2023-01-26 @ 143.17, Return: 2.04
Entry: 2023-01-27 @ 143.16, Exit: 2023-01-31 @ 142.70, Return: -0.32
Entry: 2023-02-01 @ 143.97, Exit: 2023-02-02 @ 148.90, Return: 3.42
Entry: 2023-02-03 @ 148.03, Exit: 2023-02-07 @ 150.64, Return: 1.76
Entry: 2023-02-08 @ 153.88, Exit: 2023-02-10 @ 149.46, Return: -2.87
Entry: 2023-02-13 @ 150.95, Exit: 2023-02-16 @ 153.51, Return: 1.69
Entry: 2023-02-17 @ 152.35, Exit: 2023-02-27 @ 147.71, Return: -3.05
Entry: 2023-02-28 @ 147.05, Exit: 2023-03-02 @ 144.38, Return: -1.82
Entry: 2023-03-03 @ 148.05, Exit: 2023-03-13 @ 147.81, Return: -0.16
Entry: 2023-03-15 @ 151.19, Exit: 2023-03-17 @ 156.08, Return: 3.23
Entry: 2023-03-20 @ 155.07, Exit: 2023-03-23 @ 158.83, Return: 2.42
Entry: 2023-03-24 @ 158.86, Exit: 2023-03-28 @ 157.97, Return: -0.56
Entry: 2023-03-29 @ 159.37, Exit: 2023-03-30 @ 161.53, Return: 1.36
Entry: 2023-03-31 @ 162.44, Exit: 2023-04-05 @ 164.74, Return: 1.42
Entry: 2023-04-06 @ 162.43, Exit: 2023-04-13 @ 161.63, Return: -0.49
Entry: 2023-04-14 @ 164.59, Exit: 2023-04-17 @ 165.09, Return: 0.30
Entry: 2023-04-21 @ 165.05, Exit: 2023-04-26 @ 163.06, Return: -1.21
Entry: 2023-04-27 @ 165.19, Exit: 2023-04-28 @ 168.49, Return: 2.00
Entry: 2023-05-01 @ 169.28, Exit: 2023-05-03 @ 169.50, Return: 0.13
Entry: 2023-05-04 @ 164.89, Exit: 2023-05-08 @ 172.48, Return: 4.60
Entry: 2023-05-09 @ 173.05, Exit: 2023-05-15 @ 173.16, Return: 0.06
Entry: 2023-05-17 @ 171.71, Exit: 2023-05-18 @ 173.00, Return: 0.75
Entry: 2023-05-19 @ 176.39, Exit: 2023-05-26 @ 173.32, Return: -1.74
Entry: 2023-05-30 @ 176.96, Exit: 2023-05-31 @ 177.33, Return: 0.21
Entry: 2023-06-01 @ 177.70, Exit: 2023-06-05 @ 182.63, Return: 2.77
Entry: 2023-06-06 @ 179.97, Exit: 2023-06-14 @ 183.37, Return: 1.89
Entry: 2023-06-21 @ 184.90, Exit: 2023-06-28 @ 187.93, Return: 1.64
Entry: 2023-06-29 @ 189.08, Exit: 2023-07-06 @ 189.84, Return: 0.40
Entry: 2023-07-07 @ 191.41, Exit: 2023-07-13 @ 190.50, Return: -0.48
Entry: 2023-07-14 @ 190.23, Exit: 2023-07-19 @ 193.10, Return: 1.51
Entry: 2023-07-20 @ 195.09, Exit: 2023-07-26 @ 193.67, Return: -0.73
Entry: 2023-07-27 @ 196.02, Exit: 2023-07-28 @ 194.67, Return: -0.69
Entry: 2023-08-01 @ 196.24, Exit: 2023-08-08 @ 179.69, Return: -8.43
Entry: 2023-08-09 @ 180.87, Exit: 2023-08-14 @ 177.97, Return: -1.60
Entry: 2023-08-16 @ 177.13, Exit: 2023-08-18 @ 172.30, Return: -2.73
Entry: 2023-08-21 @ 175.07, Exit: 2023-08-22 @ 177.06, Return: 1.14
Entry: 2023-08-23 @ 178.52, Exit: 2023-08-28 @ 180.09, Return: 0.88
Entry: 2023-08-29 @ 179.70, Exit: 2023-09-08 @ 178.35, Return: -0.75
Entry: 2023-09-11 @ 180.07, Exit: 2023-09-14 @ 174.00, Return: -3.37
Entry: 2023-09-15 @ 176.48, Exit: 2023-09-26 @ 174.82, Return: -0.94
Entry: 2023-09-28 @ 169.34, Exit: 2023-09-29 @ 172.02, Return: 1.58
Entry: 2023-10-02 @ 171.22, Exit: 2023-10-04 @ 171.09, Return: -0.08
Entry: 2023-10-05 @ 173.79, Exit: 2023-10-27 @ 166.91, Return: -3.96
Entry: 2023-10-30 @ 169.02, Exit: 2023-10-31 @ 169.35, Return: 0.20
Entry: 2023-11-01 @ 171.00, Exit: 2023-11-02 @ 175.52, Return: 2.64
Entry: 2023-11-03 @ 174.24, Exit: 2023-11-06 @ 176.38, Return: 1.23
Entry: 2023-11-07 @ 179.18, Exit: 2023-11-27 @ 189.92, Return: 5.99
Entry: 2023-11-29 @ 190.90, Exit: 2023-12-05 @ 190.21, Return: -0.36
Entry: 2023-12-06 @ 194.45, Exit: 2023-12-08 @ 194.20, Return: -0.13
Entry: 2023-12-11 @ 193.11, Exit: 2023-12-14 @ 198.02, Return: 2.54
Entry: 2023-12-18 @ 196.09, Exit: 2023-12-19 @ 196.16, Return: 0.04
Entry: 2023-12-20 @ 196.90, Exit: 2023-12-21 @ 196.10, Return: -0.41
Entry: 2023-12-22 @ 195.18, Exit: 2023-12-26 @ 193.61, Return: -0.80
Entry: 2023-12-27 @ 192.49, Exit: 2023-12-28 @ 194.14, Return: 0.86
Entry: 2023-12-29 @ 193.90, Exit: 2024-01-08 @ 182.09, Return: -6.09
Entry: 2024-01-09 @ 183.92, Exit: 2024-01-17 @ 181.27, Return: -1.44
Entry: 2024-01-18 @ 186.09, Exit: 2024-01-19 @ 189.33, Return: 1.74
Entry: 2024-01-22 @ 192.30, Exit: 2024-01-26 @ 194.27, Return: 1.02
Entry: 2024-01-29 @ 192.01, Exit: 2024-02-15 @ 183.55, Return: -4.41
Entry: 2024-02-16 @ 183.42, Exit: 2024-02-20 @ 181.79, Return: -0.89
Entry: 2024-02-21 @ 181.94, Exit: 2024-03-04 @ 176.15, Return: -3.18
Entry: 2024-03-05 @ 170.76, Exit: 2024-03-19 @ 174.34, Return: 2.10
Entry: 2024-03-20 @ 175.72, Exit: 2024-03-28 @ 171.75, Return: -2.26
Entry: 2024-04-01 @ 171.19, Exit: 2024-04-02 @ 169.08, Return: -1.23
Entry: 2024-04-03 @ 168.79, Exit: 2024-04-04 @ 170.29, Return: 0.89
Entry: 2024-04-08 @ 169.03, Exit: 2024-04-09 @ 168.70, Return: -0.20
Entry: 2024-04-10 @ 168.80, Exit: 2024-04-22 @ 165.52, Return: -1.95
Entry: 2024-04-25 @ 169.53, Exit: 2024-04-26 @ 169.88, Return: 0.21
Entry: 2024-04-30 @ 173.33, Exit: 2024-05-14 @ 187.51, Return: 8.18
Entry: 2024-05-16 @ 190.47, Exit: 2024-05-24 @ 188.82, Return: -0.87
Entry: 2024-05-28 @ 191.51, Exit: 2024-05-31 @ 191.44, Return: -0.04
Entry: 2024-06-03 @ 192.90, Exit: 2024-06-13 @ 214.74, Return: 11.32
Entry: 2024-06-17 @ 213.37, Exit: 2024-06-18 @ 217.59, Return: 1.98
Entry: 2024-06-20 @ 213.93, Exit: 2024-06-24 @ 207.72, Return: -2.90
Entry: 2024-06-28 @ 215.77, Exit: 2024-07-15 @ 236.48, Return: 9.60
Entry: 2024-07-19 @ 224.82, Exit: 2024-07-23 @ 224.37, Return: -0.20
Entry: 2024-07-24 @ 224.00, Exit: 2024-07-26 @ 218.70, Return: -2.37
Entry: 2024-07-29 @ 216.96, Exit: 2024-08-06 @ 205.30, Return: -5.37
Entry: 2024-08-08 @ 213.11, Exit: 2024-08-12 @ 216.07, Return: 1.39
Entry: 2024-08-13 @ 219.01, Exit: 2024-08-14 @ 220.57, Return: 0.71
Entry: 2024-08-20 @ 225.77, Exit: 2024-08-23 @ 225.66, Return: -0.05
Entry: 2024-08-26 @ 226.76, Exit: 2024-08-27 @ 226.00, Return: -0.34
Entry: 2024-08-28 @ 227.92, Exit: 2024-08-29 @ 230.10, Return: 0.96
Entry: 2024-08-30 @ 230.19, Exit: 2024-09-06 @ 223.95, Return: -2.71
Entry: 2024-09-09 @ 220.82, Exit: 2024-09-12 @ 222.50, Return: 0.76
Entry: 2024-09-17 @ 215.75, Exit: 2024-09-26 @ 227.30, Return: 5.35
Entry: 2024-09-30 @ 230.04, Exit: 2024-10-08 @ 224.30, Return: -2.50
Entry: 2024-10-09 @ 225.23, Exit: 2024-10-14 @ 228.70, Return: 1.54
Entry: 2024-10-15 @ 233.61, Exit: 2024-10-28 @ 233.32, Return: -0.12
Entry: 2024-10-29 @ 233.10, Exit: 2024-10-31 @ 229.34, Return: -1.61
Entry: 2024-11-01 @ 220.97, Exit: 2024-11-07 @ 224.63, Return: 1.66
Entry: 2024-11-08 @ 227.17, Exit: 2024-11-13 @ 224.01, Return: -1.39
Entry: 2024-11-14 @ 225.02, Exit: 2024-11-19 @ 226.98, Return: 0.87
Entry: 2024-11-20 @ 228.06, Exit: 2024-11-22 @ 228.06, Return: 0.00
Entry: 2024-11-25 @ 231.46, Exit: 2024-11-26 @ 233.33, Return: 0.81
Entry: 2024-11-27 @ 234.47, Exit: 2024-11-29 @ 234.81, Return: 0.15
Entry: 2024-12-02 @ 237.27, Exit: 2024-12-05 @ 243.99, Return: 2.83
Entry: 2024-12-06 @ 242.91, Exit: 2024-12-09 @ 241.83, Return: -0.44
Entry: 2024-12-10 @ 246.89, Exit: 2024-12-12 @ 246.89, Return: 0.00
Entry: 2024-12-13 @ 247.82, Exit: 2024-12-23 @ 254.77, Return: 2.81
Entry: 2024-12-24 @ 255.49, Exit: 2024-12-26 @ 258.19, Return: 1.06
Entry: 2024-12-27 @ 257.83, Exit: 2024-12-30 @ 252.23, Return: -2.17
Entry: 2024-12-31 @ 252.44, Exit: 2025-01-06 @ 244.31, Return: -3.22
Entry: 2025-01-07 @ 242.98, Exit: 2025-01-23 @ 224.74, Return: -7.51
Entry: 2025-01-24 @ 224.78, Exit: 2025-01-28 @ 230.85, Return: 2.70
Entry: 2025-01-30 @ 238.67, Exit: 2025-02-03 @ 229.99, Return: -3.63
Entry: 2025-02-04 @ 227.25, Exit: 2025-02-13 @ 236.91, Return: 4.25
Entry: 2025-02-14 @ 241.25, Exit: 2025-03-05 @ 235.42, Return: -2.42
Entry: 2025-03-07 @ 235.11, Exit: 2025-03-13 @ 215.95, Return: -8.15
Entry: 2025-03-14 @ 211.25, Exit: 2025-03-27 @ 221.39, Return: 4.80
Entry: 2025-03-28 @ 221.67, Exit: 2025-03-31 @ 217.01, Return: -2.10
Entry: 2025-04-01 @ 219.81, Exit: 2025-04-02 @ 221.32, Return: 0.69
Entry: 2025-04-03 @ 205.54, Exit: 2025-04-07 @ 177.20, Return: -13.79
Entry: 2025-04-08 @ 186.70, Exit: 2025-04-16 @ 198.36, Return: 6.25
Entry: 2025-04-17 @ 197.20, Exit: 2025-04-23 @ 206.00, Return: 4.46
Entry: 2025-04-24 @ 204.89, Exit: 2025-04-28 @ 210.00, Return: 2.49
Entry: 2025-04-30 @ 209.30, Exit: 2025-05-14 @ 212.43, Return: 1.50
Entry: 2025-05-15 @ 210.95, Exit: 2025-06-18 @ 195.94, Return: -7.12
Entry: 2025-06-20 @ 198.24, Exit: 2025-07-10 @ 210.51, Return: 6.19
Entry: 2025-07-11 @ 210.57, Exit: 2025-07-14 @ 209.93, Return: -0.30
Entry: 2025-07-15 @ 209.22, Exit: 2025-07-28 @ 214.03, Return: 2.30
Entry: 2025-07-30 @ 211.90, Exit: 2025-07-31 @ 207.57, Return: -2.04
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
    # Pull the LLM
    ollama pull gemma:2b

    # Ingest news data (one-time setup)
    python ingest_data.py

    # Start the AI service
    uvicorn rag_service:app --reload
    ```
4.  **Run Backtest**: In a new terminal, run the compiled Java application.
    ```bash
    java -jar target/retrotrade-1.0.jar --symbol=AAPL --start=2019-01-01 --end=2025-08-12 --file=data/AAPL.csv
    ```

## Future Enhancements

-   Multi-asset portfolio backtesting.
-   Implement more advanced position sizing models.
-   Develop a web-based dashboard for interactive analysis.
