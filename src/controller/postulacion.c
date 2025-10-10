#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <microhttpd.h>
#include "../../include/utils.h"
#include "../../include/postulacion.h"

/* Gestiona y enruta las llamadas hacia los instrumentos */
enum MHD_Result URLPostulacion
(const char *url, const char *method, struct MHD_Connection *conn)
{
	if (strcmp(method, "GET") == 0) {
		char* result = VerTodasLasPostulaciones(url);
		return CrearRespuesta(conn, result, MHD_HTTP_OK);
	}
	char *msg = "Llamada invalida!";
	unsigned int err = MHD_HTTP_BAD_REQUEST;
	return CrearRespuesta(conn, msg, err);
}
