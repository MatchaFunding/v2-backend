#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/persona.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodasLasPersonas(const char *url) {
	char *cache = BuscarEnCache("personas");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodasLasPersonas";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("personas", result);
		return result;
	}
	return cache;
}
