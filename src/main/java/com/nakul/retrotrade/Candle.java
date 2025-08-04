package com.nakul.retrotrade;

import com.google.gson.annotations.SerializedName;

import java.time.LocalDate;

public class Candle {
    LocalDate date;
    double open;
    double high;
    double low;
    double close;
    @SerializedName("adjClose")
    double adjustedClose;
    double volume;

    @Override
    public String toString() {
        return "Candle [date=" + date
                + ", open=" + open
                + ", high=" + high
                + ", low=" + low
                + ", close=" + close
                + ", adjusted_close=" + adjustedClose
                + ", volume=" + volume + "]";
    }

    public LocalDate getDate() {return date;}
    public double getOpen() {return open;}
    public double getHigh() {return high;}
    public double getLow() {return low;}
    public double getClose() {return close;}
    public double getAdjustedClose() {return adjustedClose;}
    public double getVolume() {return volume;}
}
