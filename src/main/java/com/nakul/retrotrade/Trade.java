package com.nakul.retrotrade;

import java.time.LocalDate;

public class Trade {
    LocalDate entryDate;
    double entryPrice;
    double exitPrice;
    LocalDate exitDate;
    double returnPercentage;

    public Trade(LocalDate entryDate, double entryPrice, double exitPrice, LocalDate exitDate) {
        this.entryDate = entryDate;
        this.entryPrice = entryPrice;
        this.exitPrice = exitPrice;
        this.exitDate = exitDate;
        this.returnPercentage = ((exitPrice - entryPrice)/entryPrice) * 100;
    }

    @Override
    public String toString() {
        return String.format("Entry: %s @ %.2f, Exit: %s @ %.2f, Return: %.2f", entryDate, entryPrice, exitDate, exitPrice, returnPercentage);
    }
}
