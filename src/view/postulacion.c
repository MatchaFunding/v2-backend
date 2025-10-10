#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/postulacion.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodasLasPostulaciones(const char *url) {
	char *cache = BuscarEnCache("postulaciones");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodasLasPostulaciones";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("postulaciones", result);
		return result;
	}
	return cache;
}
