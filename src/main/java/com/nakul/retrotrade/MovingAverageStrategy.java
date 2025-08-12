package com.nakul.retrotrade;

import java.util.List;

public class MovingAverageStrategy implements TradingStrategy {
    private final int shortWindow;
    private final int longWindow;

    public MovingAverageStrategy(int shortWindow, int longWindow) {
        this.shortWindow = shortWindow;
        this.longWindow = longWindow;
    }

    @Override
    public Signal generateSignal(int index, List<Candle> history, boolean isInPosition){
        if(index < longWindow) return Signal.HOLD;
        double shortMA = calculateMA(index, shortWindow, history);
        double longMA = calculateMA(index, longWindow, history);
        double prevShortMA = calculateMA(index-1, shortWindow, history);
        double prevLongMA = calculateMA(index-1, longWindow, history);
        if(prevShortMA <= prevLongMA && shortMA > longMA) return Signal.BUY;
        if(prevShortMA >= prevLongMA && shortMA < longMA) return Signal.SELL;
        return Signal.HOLD;
    }

    double calculateMA(int index, int window, List<Candle> history){
        double sum = 0;
        for(int i = 0; i < window; i++) sum += history.get(index-i).getAdjustedClose();
        return sum / window;
    }
}
