#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/financiador.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosFinanciadores(const char *url) {
	char *cache = BuscarEnCache("financiadores");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosFinanciadores";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("financiadores", result);
		return result;
	}
	return cache;
}