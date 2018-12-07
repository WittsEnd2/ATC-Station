# ATC-Station

## About
ATC-Station uses ADS-B data (retreived from an SDR) to provide data about flgihts and airlines. It uses dump1090 to get the flight data, and then creates uses the data to perform sentiment analysis, display a map of where flights are located, weather, and get the ATC radio for the flight. 

## Technology Stack
Back-end: Python & Flask
Front-end: Angular 2 (JavaScript)

## Componenets
Flight map - Requires an SDR and dump1090 to use.
Sentiment Anlaysis Panel
ATC-Radio for the particular flight
List of flight status
Weather

## Use cases
This would be great for people who work in ATC to use (or are contractors related to the flights).
