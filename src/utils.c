#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../include/utils.h"

/* Envia un mensaje simple en formato HTTP */
char *MensajeSimple(const char *message_str) {
	char *formatted_message = NULL;
	size_t formatted_message_size = strlen(message_str) + 20;
	formatted_message = (char *)malloc(formatted_message_size);
	if (formatted_message)
		snprintf(formatted_message, formatted_message_size, "{\"message\": \"%s\"}", message_str);
	return formatted_message;
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
