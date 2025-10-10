#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/resultado.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerResultados(const char *url) {
	char *cache = BuscarEnCache("resultados");
	if (!cache) {
		const char *query = "SELECT * FROM VerResultados";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("resultados", result);
		return result;
	}
	return cache;
}
