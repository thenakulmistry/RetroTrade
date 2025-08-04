package com.nakul.retrotrade;

import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Command(name= "retrotrade", mixinStandardHelpOptions = true, version = "RetroTrade 1.0",
        description = "A CLI-based backtesting engine for stock trading strategies.")
public class CLI implements Runnable {

    @Option(names = {"-s", "--symbol"}, description = "Stock symbol", required = true)
    private String symbol;

    @Option(names = {"--start"}, description = "Start Date (YYYY-MM-DD)", required = true)
    private String startDate;

    @Option(names = {"--end"}, description = "End Date (YYYY-MM-DD)", required = true)
    private String endDate;

    @Option(names = {"-f", "--file"}, description = "CSV file path")
    private String filePath;

    private final String apiToken = System.getenv("API_TOKEN");

    public static void main(String[] args) {
        int exitCode = new CommandLine(new CLI()).execute(args);
        System.exit(exitCode);
    }

    @Override
    public void run() {
        File dataFile = new File(filePath);
        List<Candle> candles;
        if(!dataFile.exists()) {
            System.out.println("\nData file not found, fetching from API");
            DataFetcher dataFetcher = new DataFetcher();
            candles = dataFetcher.fetch(symbol, startDate, endDate, apiToken);
            dataFetcher.saveToCsv(candles, filePath);
        }
        else{
            System.out.println("\nData file found. Reading from " + filePath);
            CsvReader csvReader = new CsvReader();
            candles = csvReader.readCandles(filePath);
        }
        if(candles == null){
            System.err.println("Could not retrieve the data" );
            return;
        }

        BacktestResult bestResult = null;
        double maxReturn = 0;
        int shortWindow = 0, longWindow = 0;
        BacktestEngine engine = new BacktestEngine();
        for(int i = 5; i <= 50; i++) {
            for(int j = i+1; j <= 200; j++) {
                TradingStrategy tradingStrategy = new MovingAverageStrategy(i, j);
                BacktestResult result = engine.run(candles, tradingStrategy);
                if(result.totalReturn > maxReturn) {
                    maxReturn = result.totalReturn;
                    bestResult = result;
                    shortWindow = i;
                    longWindow = j;
                }
//                result.printReport();
            }
        }
        System.out.println("The best moving average strategy is with shortWindow of " +shortWindow+ " and longWindow of " +longWindow);
        bestResult.printReport();
    }
}
