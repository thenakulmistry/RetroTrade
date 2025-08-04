package com.nakul.retrotrade;

import java.util.ArrayList;
import java.util.List;

public class BacktestEngine {
    public BacktestResult run(List<Candle> candles, TradingStrategy strategy) {
        List<Trade> tradeLog = new ArrayList<>();
        boolean inPosition = false;
        double entryPrice = 0.0;
        int entryIndex = 0;

        for(int i = 0; i < candles.size(); i++) {
            Candle currCandle = candles.get(i);

            if(!inPosition && strategy.shouldBuy(i, candles)) {
                inPosition = true;
                entryPrice = currCandle.getOpen();
                entryIndex = i;
            }
            else if(inPosition && strategy.shouldSell(i, candles)) {
                inPosition = false;
                double exitPrice = currCandle.getOpen();
                Trade trade = new Trade(candles.get(entryIndex).getDate(), entryPrice, exitPrice, currCandle.getDate());
                tradeLog.add(trade);
            }
        }

        if(inPosition) {
            Candle lastCandle = candles.get(candles.size() - 1);
            Trade trade = new Trade(candles.get(entryIndex).getDate(), entryPrice, lastCandle.getClose(), lastCandle.getDate());
            tradeLog.add(trade);
        }

        return calculateMetrics(candles, tradeLog);
    }

    private BacktestResult calculateMetrics(List<Candle> candles, List<Trade> tradeLog) {
        if(tradeLog.isEmpty()) return new BacktestResult(0, 0, 0, 0, tradeLog);
        double totalReturn = tradeLog.stream().mapToDouble(t -> t.returnPercentage).sum();
        long winningTrades = tradeLog.stream().filter(t -> t.returnPercentage > 0).count();
        double winRate = (double) winningTrades / tradeLog.size() * 100;
        double sharpeRatio = 0;
        double maxDrawdown = 0;
        return new BacktestResult(totalReturn, sharpeRatio, maxDrawdown, winRate, tradeLog);
    }
}
