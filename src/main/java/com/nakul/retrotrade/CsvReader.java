package com.nakul.retrotrade;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CsvReader {

    public List<Candle> readCandles(String filePath) {
        List<Candle> candles = new ArrayList<>();

        CSVFormat format = CSVFormat.Builder
                .create(CSVFormat.DEFAULT)
                .setHeader()
                .setSkipHeaderRecord(true)
                .get();

        try(Reader in = new FileReader(filePath);
        CSVParser parser = format.parse(in)) {
            for (CSVRecord record : parser) {
                Candle candle = new Candle();
                candle.date = LocalDate.parse(record.get("date"));
                candle.open = Double.parseDouble(record.get("open"));
                candle.close = Double.parseDouble(record.get("close"));
                candle.high = Double.parseDouble(record.get("high"));
                candle.low = Double.parseDouble(record.get("low"));
                candle.adjustedClose = Double.parseDouble(record.get("adjusted_close"));
                candle.volume = Double.parseDouble(record.get("volume"));
                candles.add(candle);
            }
        } catch (IOException e) {
            System.err.println("Error reading from CSV");
            return Collections.emptyList();
        }
        return candles;
    }
}
