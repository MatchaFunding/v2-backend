curl -H 'Content-Type: application/json' \
      -d '{
		"NombreDeUsuario":"ElMaikina",
		"Contrasena":"asoqe123135",
		"Correo": "elmaikina@gmail.com"
	}' \
      -X POST \
      localhost:8080/usuario/autenticar | jq '.'
