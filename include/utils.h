#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <microhttpd.h>

/* Tamano maximo de los buffer para los POST requests */
#define POSTBUFFERSIZE 8192

/* Almacena los tipos de respuesta HTTP */
typedef enum {
	OK = 200,
	BAD_REQUEST = 400,
	NOT_FOUND = 404,
	INTERNAL_SERVER_ERROR = 500,
	NOT_IMPLEMENTED = 501
} HTTP_status;

/* Almacena el cuerpo de las respuestas HTTP */
typedef struct {
	char *body;
	HTTP_status status;
} HTTP_response;

/* Almacena la informacion de las llamadas entrantes */
typedef struct {
	struct MHD_PostProcessor *pp;
	char *json_data;
	size_t json_size;
} connection_info_struct;

char *MensajeSimple(const char *message_str);
struct MHD_Response *CrearRespuesta(const char *message);
enum MHD_Result CrearResultado(struct MHD_Connection *conn, HTTP_response api);
enum MHD_Result SendResponse(struct MHD_Connection *con, const char *msg, unsigned int status);
HTTP_response ValidarResultado(char *result);
bool EsMetodo(const char *method, char *valid_method);
bool EsRuta(const char *url, char *route);

#endif
