#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/miembro.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosMiembros(const char *url) {
	char *cache = BuscarEnCache("sexos");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosMiembros";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("sexo", result);
		return result;
	}
	return cache;
}
