#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/instrumento.h"

/* Muestra absolutamente todos los instrumentos existentes */
HTTP_response VerTodosLosInstrumentos(const char *url) {
	char *cache = BuscarEnCache("instrumentos");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosInstrumentos";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("instrumentos", result);
		return ValidarResultado(result);
	}
	return ValidarResultado(cache);
}

/* Muestra solo un instrumento en base a su identificador */
HTTP_response VerSoloUnInstrumento(const char *id) {
	if (id == NULL) {
		return (HTTP_response){
			.body = MensajeSimple("No id provided"),
			.status = BAD_REQUEST
		};
	}
	char cache_query[64];
	char query[64];
	snprintf(cache_query, sizeof(cache_query), "instrumento:%s", id);
	char *cache = BuscarEnCache(cache_query);
	if (!cache) {
		snprintf(query, sizeof(query), "SELECT * FROM VerTodosLosInstrumentos WHERE ID=%s", id);
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache(cache_query, result);
		return ValidarResultado(result);
	}
	return ValidarResultado(cache);
}
