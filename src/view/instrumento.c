#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/instrumento.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosInstrumentos(const char *url) {
	char *cache = BuscarEnCache("instrumentos");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosInstrumentos";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("instrumentos", result);
		return result;
	}
	return cache;
}
