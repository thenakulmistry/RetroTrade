package com.nakul.retrotrade;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RAGSignalStrategy implements TradingStrategy{

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_1_1)
            .connectTimeout(Duration.ofSeconds(10))
            .build();
    private final ObjectMapper objectMapper = new ObjectMapper();
    private final String symbol;
    private final String ragServiceUrl = "http://127.0.0.1:8000/generate_signal";
    private final Map<String, Signal> signalCache = new HashMap<>();

    public RAGSignalStrategy(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public Signal generateSignal(int index, List<Candle> history, boolean isInPosition){
        String dateStr = history.get(index).getDate().format(DateTimeFormatter.ISO_LOCAL_DATE);
        String cacheKey = dateStr + ": " + isInPosition;
        if(signalCache.containsKey(cacheKey)) return signalCache.get(dateStr);

        try{
            String jsonPayload = String.format("{\"symbol\": \"%s\", \"date\": \"%s\", \"is_in_position\": %b}", this.symbol, dateStr, isInPosition);
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(ragServiceUrl))
                    .header("Content-Type", "application/json")
                    .timeout(Duration.ofSeconds(30))
                    .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
                    .build();
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            if(response.statusCode() == 200){
                Map<String, String> responseMap = objectMapper.readValue(response.body(), Map.class);
                String signalStr = responseMap.getOrDefault("signal", "HOLD");
                Signal signal;
                switch(signalStr){
                    case "BUY": signal = Signal.BUY; break;
                    case "SELL": signal = Signal.SELL; break;
                    default: signal = Signal.HOLD; break;
                }
                signalCache.put(cacheKey, signal);
                return signal;
            }
            else{
                System.err.println("RAG service returned error: " + response.statusCode() + ": " + response.body());
            }
        } catch(Exception e){
            System.err.println("Error calling RAG service for date " + dateStr + ": " + e.getMessage());
        }
        signalCache.put(dateStr, Signal.HOLD);
        return Signal.HOLD;
    }
}
