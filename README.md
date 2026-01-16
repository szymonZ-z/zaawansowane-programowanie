# PeopleDetection – Asynchroniczna analiza liczby osób na zdjęciach

Projekt realizuje asynchroniczną analizę zdjęć pod kątem wykrywania osób
z wykorzystaniem API REST, RabbitMQ, workerów(consumerów), Dockera oraz
modelu YOLO (Ultralytics).

Spełnione wymagania oceniania:

1. 3 – endpoint GET z lokalnym plikiem
2. 4 – endpoint URL + async + kolejka + status
3. 5 – endpoint POST upload
4. RabbitMQ
5. Skalowanie workerów (domyślnie 8)
6. Asynchroniczne przetwarzanie
7. Detekcja osób (YOLO)
