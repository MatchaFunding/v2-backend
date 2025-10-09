#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/proyecto.h"

/* Muestra absolutamente todos los instrumentos existentes */
char* VerTodosLosProyectos(const char *url) {
	char *cache = BuscarEnCache("proyectos");
	if (!cache) {
		const char *query = "SELECT * FROM VerTodosLosProyectos";
		char *result = EjecutarQueryEnJSON(query, DB);
		GuardarEnCache("instrumentos", result);
		return result;
	}
	return cache;
}
