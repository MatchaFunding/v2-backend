#ifndef ROUTE_H
#define ROUTE_H

#define POST 1
#define GET 0

#include <setjmp.h>

void LoguearAPI(const char *url, const char *method);
struct MHD_Response *CrearRespuestaHTTP(const char *message);
enum MHD_Result GestorPrincipal
	(void *cls, struct MHD_Connection *conn,
	const char *url, const char *method,
	const char *ver, const char *data,
	size_t *data_size, void **con_cls);
#endif
