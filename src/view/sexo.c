#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/sexo.h"

/* Muestra absolutamente todos los sexos existentes */
HTTP_response VerSexos(const char *url) {
	char *cache = BuscarEnCache("sexos");
	if (!cache) {
		const char *query = "SELECT * FROM VerSexos";
		char *result = EjecutarQueryEnJSON(query);
		GuardarEnCache("sexos", result);
		return ValidarResultado(result);
	}
	return ValidarResultado(cache);
}
