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

/* Función auxiliar para enviar una respuesta HTTP */
enum MHD_Result CrearRespuesta(struct MHD_Connection *con, const char *msg, unsigned int status) {
	struct MHD_Response *res = MHD_create_response_from_buffer(strlen(msg), (void *)msg, MHD_RESPMEM_PERSISTENT);
	MHD_add_response_header(res, "Content-Type", "application/json");
	MHD_add_response_header(res, "Access-Control-Allow-Origin", "*");
    enum MHD_Result ret = MHD_queue_response(con, status, res);
    MHD_destroy_response(res);
    return ret;
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
