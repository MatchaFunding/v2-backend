# Mide que tanto tiempo tarda en enviar un flujo masivo de datos por segundo
time for i in {1..1000}; do 
	curl -X GET "localhost:8080/instrumentos" --compressed --insecure -s -o /dev/null -w "%{time_total}s\n"
done
