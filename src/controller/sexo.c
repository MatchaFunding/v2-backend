#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/sexo.h"

/* Gestiona y enruta las llamadas hacia los instrumentos */
HTTP_response URLSexo(const char *url, const char *method, const char *body){
	if (EsMetodo(method, "GET")) {
		return VerSexos(url);
	}
	return (HTTP_response){
		.body = MensajeSimple("Invalid method"),
		.status = NOT_IMPLEMENTED
	};
}
