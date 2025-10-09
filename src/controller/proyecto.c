#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <microhttpd.h>
#include "../../include/utils.h"
#include "../../include/proyecto.h"

/* Gestiona y enruta las llamadas hacia los instrumentos */
enum MHD_Result URLProyecto
(const char *url, const char *method, struct MHD_Connection *conn)
{
	char *id = strstr(url, "/proyectos/");
	if (id != NULL) {
		id += strlen("/proyectos/");
	}
	if (EsMetodo(method, "GET")) {
		if (id == NULL) {
			char* result = VerTodosLosProyectos(url);
			return CrearRespuesta(conn, result, MHD_HTTP_OK);
		}
		else {
			char* result = VerSoloUnProyecto(id);
			return CrearRespuesta(conn, result, MHD_HTTP_OK);
		}
	}
	char *msg = "Llamada invalida!";
	unsigned int err = MHD_HTTP_BAD_REQUEST;
	return CrearRespuesta(conn, msg, err);
}
