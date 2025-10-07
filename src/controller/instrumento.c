#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/instrumento.h"

/* Gestiona y enruta las llamadas hacia los instrumentos */
HTTP_response URLInstrumento(const char *url, const char *method, const char *body){
	char *id = strstr(url, "/instrumentos/");
	if (id != NULL) {
		id += strlen("/instrumentos/");
	}
	if (EsMetodo(method, "GET")) {
		if (id == NULL)
			return VerTodosLosInstrumentos(url);
		else
			return VerSoloUnInstrumento(id);
	}
	return (HTTP_response){
		.body = MensajeSimple("Invalid method"),
		.status = NOT_IMPLEMENTED
	};
}
