#ifndef HANDLER_H
#define HANDLER_H

#define POSTBUFFERSIZE 512
#define MAXANSWERSIZE 512
#define MAXNAMESIZE 20

#define POST 1
#define GET 0

#include <setjmp.h>

struct connection_info_struct {
	int connectiontype;
	char *answerstring;
	struct MHD_PostProcessor *postprocessor;
};

void LoguearAPI(const char *url, const char *method);
struct MHD_Response *CrearRespuestaHTTP(const char *message);
enum MHD_Result GestorPrincipal
	(void *cls, struct MHD_Connection *connection,
	const char *url, const char *method,
	const char *version, const char *upload_data,
	size_t *upload_data_size, void **con_cls);

#endif
