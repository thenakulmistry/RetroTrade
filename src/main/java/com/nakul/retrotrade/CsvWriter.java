package com.nakul.retrotrade;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class CsvWriter {
    private static final String[] headers = {"date", "open", "high", "low", "close", "adjusted_close", "volume"};

    public void writeToCsv(List<Candle> candles, String filePath){

        CSVFormat csvFormat = CSVFormat.Builder.create(CSVFormat.DEFAULT)
                .setHeader(headers)
                .get();

        try(FileWriter out = new FileWriter(filePath);
            CSVPrinter printer = new CSVPrinter(out, csvFormat)){
            for(Candle candle : candles){
                printer.printRecord(
                        candle.getDate(),
                        candle.getOpen(),
                        candle.getHigh(),
                        candle.getLow(),
                        candle.getClose(),
                        candle.getAdjustedClose(),
                        candle.getVolume()
                );
            }
            System.out.println("Successfully wrote " + candles.size() + " candles to " + filePath);
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
