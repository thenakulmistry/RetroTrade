package com.nakul.retrotrade;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDate;
import java.util.Collections;
import java.util.List;

public class DataFetcher {

    List<Candle> fetch(String symbol, String startDate, String endDate, String apiToken){

        String apiUrl = "https://api.tiingo.com/tiingo/daily/" +symbol+
                "/prices?startDate="+startDate+
                "&endDate="+endDate+
                "&token="+apiToken+
                "&format=json";

        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(apiUrl))
                    .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                System.err.println("Error fetching data" + response.statusCode() + " " + response.body());
                return Collections.emptyList();
            }
            Gson gson = new GsonBuilder()
                    .registerTypeAdapter(LocalDate.class, new LocalDateAdapter())
                    .create();
            return gson.fromJson(response.body(), new TypeToken<List<Candle>>(){}.getType());
        } catch (IOException | InterruptedException e) {
            System.err.println("Error fetching data" + e.getMessage());
            Thread.currentThread().interrupt();
        }
        return Collections.emptyList();
    }

    void saveToCsv(List<Candle> data, String outputPath){
        if(data.isEmpty()) {
            System.out.println("No data found");
            return;
        }
        if(outputPath != null) {
            CsvWriter csvWriter = new CsvWriter();
            csvWriter.writeToCsv(data, outputPath);
        }
        else {
            System.out.println("No output file specified");
            System.out.println("Fetched " + data.size() + " records. Printing to console");
            for(Candle candle : data) System.out.println(candle);
        }
    }
}
