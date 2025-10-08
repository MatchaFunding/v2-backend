#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../include/utils.h"

/*
Funciones comunes para que las respuestas cumplan con el estandar HTTP
Tambien existen funciones para facilitar la legibilidad del codigo, como
las funciones para leer los metodos o rutas de las API.
*/

/* Envia un mensaje simple en formato HTTP */
char *MensajeSimple(const char *message_str) {
	char *formatted_message = NULL;
	size_t formatted_message_size = strlen(message_str) + 20;
	formatted_message = (char *)malloc(formatted_message_size);
	if (formatted_message)
		snprintf(formatted_message, formatted_message_size, "{\"message\": \"%s\"}", message_str);
	return formatted_message;
}

/* Construye la respuesta en formato HTTP */
struct MHD_Response *CrearRespuesta(const char *message) {
	struct MHD_Response *response;
	response = MHD_create_response_from_buffer(strlen(message), (void *)message, MHD_RESPMEM_PERSISTENT);
	if (!response)
		return NULL;
	MHD_add_response_header(response, "Content-Type", "application/json");
	MHD_add_response_header(response, "Access-Control-Allow-Origin", "*");
	return response;
}

/* Construye el resultado en formato HTTP */
enum MHD_Result CrearResultado(struct MHD_Connection *conn, HTTP_response api) {
	struct MHD_Response *response;
	int ret;

	// Se formatea la respuesta en formato HTTP
	response = CrearRespuesta(api.body);
	if (!response) {
		return MHD_NO;
	}

	// Devuelve la respuesta procesada
	ret = MHD_queue_response(conn, api.status, response);
	MHD_destroy_response(response);
	return ret;
}

/* Función auxiliar para enviar una respuesta HTTP */
enum MHD_Result SendResponse(struct MHD_Connection *con, const char *msg, unsigned int status) {
	struct MHD_Response *res = MHD_create_response_from_buffer(strlen(msg), (void *)msg, MHD_RESPMEM_PERSISTENT);
	MHD_add_response_header(res, "Content-Type", "application/json");
	MHD_add_response_header(res, "Access-Control-Allow-Origin", "*");
    enum MHD_Result ret = MHD_queue_response(con, status, res);
    MHD_destroy_response(res);
    return ret;
}

/* Valida si la ruta existe y es valida */
bool EsRuta(const char *url, char *route) {
	return strstr(url, route) != NULL;
}

/* Valida si el metodo existe y es valido */
bool EsMetodo(const char *method, char *valid_method) {
	return strcmp(method, valid_method) == 0;
}

/* Valida el resultado y devuelve una respuesta HTTP */
HTTP_response ValidarResultado(char *result) {
	if (result == NULL) {
		return (HTTP_response){
			.body = MensajeSimple("Internal server error"),
			.status = INTERNAL_SERVER_ERROR
		};
	}
	return (HTTP_response){
		.body = result,
		.status = OK
	};
}
