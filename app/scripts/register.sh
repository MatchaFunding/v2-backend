curl -H 'Content-Type: application/json' \
      -d '{
		"Persona": {
			"Nombre":"Miguel Soto Delgado",
			"Sexo":"Hombre",
			"RUT": "20.430.363-0",
			"FechaDeNacimiento": "2000-07-04"
		},
		"Usuario": {
			"NombreDeUsuario":"ElMaikina",
			"Contrasena":"asoqe123135",
			"Correo": "elmaikina@gmail.com"
		},
		"Beneficiario": {
			"Nombre":"ElMaikina",
			"FechaDeCreacion":"2000-07-04",
			"RegionDeCreacion": "Antofagasta",
			"Direccion": "Diaz Gana 1099",
			"TipoDePersona": "Natural",
			"TipoDeEmpresa": "Empresa Individual de Responsabilidad Limitada",
			"Perfil": "Empresa",
			"RUTdeEmpresa": "20.430.363-0",
			"RUTdeRepresentante": "20.430.363-0"
		}
	}' \
      -X POST \
      localhost:8080/usuario/registrar | jq '.'
