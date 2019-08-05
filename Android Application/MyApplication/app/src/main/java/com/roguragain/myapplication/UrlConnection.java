package com.roguragain.myapplication;

import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;

public class UrlConnection {



    public static final String LOG_TAG = "urlconnections";

    public static String getNewsJson(String urlstring) {
        URL url = createUrl(urlstring);
        String json = "";
        try {

            json = makeHttpRequest(url);
        } catch (IOException e) {
            Log.e(LOG_TAG, "ERROR MAKING URL CONNECTIONS", e);
        }
        return json;
    }

    private static URL createUrl(String urlString) {
        URL url = null;

        try {
            url = new URL(urlString);
        } catch (MalformedURLException e) {

            Log.e(LOG_TAG, "Error with creating url");
        }
        return url;

    }

    private static String makeHttpRequest(URL url) throws IOException {
        String jsonResponse = "";
        if (url == null) {

            return jsonResponse;
        }
        HttpURLConnection urlConnection = null;
        InputStream inputStream = null;


        try {
            urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.connect();

            if (urlConnection.getResponseCode() == 200) {
                inputStream = urlConnection.getInputStream();
                jsonResponse = readFromString(inputStream);

            } else {
                Log.e(LOG_TAG, "Error Resopnse Code" + urlConnection.getResponseCode());
            }

        } catch (IOException e) {
            Log.e(LOG_TAG, "PROBLEM in retrieving json results", e);
        } finally {
            if (urlConnection != null) {
                urlConnection.disconnect();
            }
            if (inputStream != null) {
                inputStream.close();
            }
        }
        return jsonResponse;
    }

    private static String readFromString(InputStream inputStream) throws IOException {
        StringBuilder output = new StringBuilder();

        if (inputStream != null) {
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream, Charset.forName("UTF-8"));
            BufferedReader reader = new BufferedReader(inputStreamReader);
            String line = reader.readLine();
            while (line != null) {
                output.append(line);
                line = reader.readLine();
            }
        }
        return output.toString();
    }


}

