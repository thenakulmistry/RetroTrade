package com.nakul.retrotrade;

import java.util.List;

public interface TradingStrategy {
    boolean shouldBuy(int index, List<Candle> history);
    boolean shouldSell(int index, List<Candle> history);
}
