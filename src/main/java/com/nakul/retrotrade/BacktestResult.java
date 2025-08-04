package com.nakul.retrotrade;

import java.util.ArrayList;
import java.util.List;

public class BacktestResult {
    double totalReturn;
    double sharpeRatio;
    double maxDrawdown;
    double winRate;
    List<Trade> tradeLog;

    public BacktestResult(double totalReturn, double sharpeRatio, double maxDrawdown, double winRate, List<Trade> tradeLog) {
        this.totalReturn = totalReturn;
        this.sharpeRatio = sharpeRatio;
        this.maxDrawdown = maxDrawdown;
        this.winRate = winRate;
        this.tradeLog = tradeLog;
    }

    public void printReport(){
        System.out.println("\n---Backtest Result---");
        System.out.printf("Total Return: %.2f%n",totalReturn);
        System.out.printf("Sharpe Ratio: %.2f%n",sharpeRatio);
        System.out.printf("Max Drawdown: %.2f%n",maxDrawdown);
        System.out.printf("Win Rate: %.2f%n",winRate);
        System.out.println("\n ---Trade log---");
        if(tradeLog.isEmpty()) System.out.println("No trades found");
        else tradeLog.forEach(System.out::println);
        System.out.println("--------------------");
    }
}
