#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/colaborador.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosColaboradores(const char *url) {
	char *cache = BuscarEnCache("sexos");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosColaboradores";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("sexo", result);
		return result;
	}
	return cache;
}
