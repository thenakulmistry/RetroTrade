package com.nakul.retrotrade;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class BacktestEngine {
    public BacktestResult run(List<Candle> candles, TradingStrategy strategy, double initialCapital) {
        List<Trade> tradeLog = new ArrayList<>();
        double cash = initialCapital;
        int sharesHeld = 0;
        double entryPrice = 0.0;
        LocalDate entryDate = null;
        List<Double> dailyPortfolio = new ArrayList<>();

        for(int i = 0; i < candles.size(); i++) {
            boolean isInPosition = sharesHeld > 0;
            Signal signal = strategy.generateSignal(i, candles, isInPosition);
            Candle currCandle = candles.get(i);
            double currPrice = currCandle.getOpen();

            if(sharesHeld > 0 && signal == Signal.SELL) {
                cash += sharesHeld * currPrice;
                Trade trade = new Trade(entryDate, entryPrice, currPrice, currCandle.getDate());
                tradeLog.add(trade);
                sharesHeld = 0;
            }
            else if(sharesHeld == 0 && signal == Signal.BUY) {
                int sharesToBuy = (int) ((cash * 0.95) / currPrice);
                if(sharesToBuy > 0) {
                    entryPrice = currPrice;
                    entryDate = currCandle.getDate();
                    sharesHeld = sharesToBuy;
                    cash -= sharesHeld * entryPrice;
                }
            }

            dailyPortfolio.add(cash + (sharesHeld * currCandle.getClose()));
        }

        if(sharesHeld > 0) {
            Candle lastCandle = candles.get(candles.size() - 1);
            double finalPrice = lastCandle.getClose();
            cash += sharesHeld * finalPrice;
            Trade trade = new Trade(entryDate, entryPrice, finalPrice, lastCandle.getDate());
            tradeLog.add(trade);
        }

        return calculateMetrics(dailyPortfolio, tradeLog, initialCapital, cash);
    }

    private BacktestResult calculateMetrics(List<Double> dailyPortfolio, List<Trade> tradeLog, double initialCapital, double finalCapital) {
        if(tradeLog.isEmpty()) return new BacktestResult(0, 0, 0, 0, tradeLog);

        double totalReturn = ((finalCapital - initialCapital) / initialCapital) * 100;
        long winningTrades = tradeLog.stream().filter(t -> t.returnPercentage > 0).count();
        double winRate = (double) winningTrades / tradeLog.size() * 100;

        List<Double> dailyReturns = new ArrayList<>();
        for (int i = 1; i < dailyPortfolio.size(); i++) {
            double yesterdayValue = dailyPortfolio.get(i - 1);
            double todayValue = dailyPortfolio.get(i);
            if (yesterdayValue != 0) {
                dailyReturns.add((todayValue - yesterdayValue) / yesterdayValue);
            }
        }
        double averageReturn = dailyReturns.stream().mapToDouble(val -> val).average().orElse(0.0);
        double stdDev = Math.sqrt(dailyReturns.stream().mapToDouble(r -> Math.pow(r - averageReturn, 2)).average().orElse(0.0));
        double sharpeRatio = 0;
        if (stdDev != 0) {
            // Annualize the Sharpe Ratio (assuming 252 trading days in a year)
            sharpeRatio = (averageReturn / stdDev) * Math.sqrt(252);
        }

        double maxDrawdown = 0;
        double peak = -1;
        for (double value : dailyPortfolio) {
            if (value > peak) peak = value;
            if (peak > 0) {
                double drawdown = (value - peak) / peak;
                if (drawdown < maxDrawdown) maxDrawdown = drawdown;
            }
        }
        return new BacktestResult(totalReturn, sharpeRatio, maxDrawdown, winRate, tradeLog);
    }
}
