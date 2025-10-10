#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <microhttpd.h>
#include "../../include/utils.h"
#include "../../include/colaborador.h"

/* Gestiona y enruta las llamadas hacia los instrumentos */
enum MHD_Result URLColaborador
(const char *url, const char *method, struct MHD_Connection *conn)
{
	if (strcmp(method, "GET") == 0) {
		char* result = VerTodosLosColaboradores(url);
		return CrearRespuesta(conn, result, MHD_HTTP_OK);
	}
	char *msg = "Llamada invalida!";
	unsigned int err = MHD_HTTP_BAD_REQUEST;
	return CrearRespuesta(conn, msg, err);
}
