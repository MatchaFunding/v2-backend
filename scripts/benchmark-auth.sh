# Mide que tanto tiempo tarda en autenticar a un usuario
time for i in {1..1000}; do 
	curl -X POST "localhost:8080/usuario/autenticar" \
	-H 'Content-Type: application/json' \
	-d '{
		"NombreDeUsuario":"ElMaikina",
		"Contrasena":"asoqe123135",
		"Correo": "elmaikina@gmail.com"
	}' \
	--compressed \
	--insecure -s -o /dev/null -w "%{time_total}s\n"
done
