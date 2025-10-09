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