#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/beneficiario.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosBeneficiarios(const char *url) {
	char *cache = BuscarEnCache("beneficiarios");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosBeneficiarios";
		char *result = EjecutarQueryEnJSON(query, DB);
		GuardarEnCache("instrumentos", result);
		return result;
	}
	return cache;
}

/* Muestra solo un instrumento en base a su identificador */
char* VerSoloUnBeneficiario(const char *id) {
	char cache_query[64];
	char query[64];
	snprintf(cache_query, sizeof(cache_query), "beneficiario:%s", id);
	char *cache = BuscarEnCache(cache_query);
	if (!cache) {
		snprintf(query, sizeof(query), "SELECT * FROM VerTodosLosBeneficiarios WHERE ID=%s", id);
		char *result = EjecutarQueryEnJSON(query, DB);
		GuardarEnCache(cache_query, result);
		return result;
	}
	return cache;
}
