package com.nakul.retrotrade;

import java.util.List;

public interface TradingStrategy {
    Signal generateSignal(int index, List<Candle> history, boolean isInPosition);
}
