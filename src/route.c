#include "../include/utils.h"
#include <microhttpd.h>
#include <setjmp.h>
#include "../include/route.h"
#include "../include/instrumento.h"
#include "../include/sexo.h"

jmp_buf ExceptionBuffer;

/* Muestra por pantalla la request y metodo solicitados por el cliente */
void LoguearAPI(const char *url, const char *method) {
	printf("[%s] %s\n", method, url);
}

/* Construye la respuesta en formato HTTP */
struct MHD_Response *CrearRespuestaHTTP(const char *message) {
	struct MHD_Response *response;
	response = MHD_create_response_from_buffer(strlen(message), (void *)message, MHD_RESPMEM_PERSISTENT);
	if (!response)
		return NULL;
	MHD_add_response_header(response, "Content-Type", "application/json");
	MHD_add_response_header(response, "Access-Control-Allow-Origin", "*");
	return response;
}

/* Genera la respuesta al cliente a partir de la API */
enum MHD_Result GenerarRespuesta
	(struct MHD_Connection *conn, HTTP_response api) 
{
	struct MHD_Response *response;
	int ret;

	// Se formatea la respuesta en formato HTTP
	response = CrearRespuestaHTTP(api.body);
	if (!response) {
		return MHD_NO;
	}

	// Devuelve la respuesta procesada
	ret = MHD_queue_response(conn, api.status, response);
	MHD_destroy_response(response);
	return ret;
}

/* Se usa la funcion "GestorPrincipal" para redirigir las
llamadas en base al tipo de objeto que se esta invocando

(es similar a los Routers en FastAPI) */
enum MHD_Result GestorPrincipal
	(void *cls, struct MHD_Connection *conn,
	const char *url, const char *method,
	const char *ver, const char *data,
	size_t *data_size, void **con_cls)
{
	// Prepara las variables de entrada y retorno
	HTTP_response api;

	// Muestra la llamada por pantalla
	LoguearAPI(url, method);

	// Redirigimos al controlador especifico de cada objeto
	// Se genera la respuesta tras llamar una API valida
	if (setjmp(ExceptionBuffer) == 0) {
		if (strcmp(url, "/") == 0) {
			api = (HTTP_response){
				.body = MensajeSimple("BackEnd activo!"),
				.status = OK
			};
			return GenerarRespuesta(conn, api);
		}
		else if (EsRuta(url, "/instrumentos"))
		{
			api = URLInstrumento(url, method, data);
			return GenerarRespuesta(conn, api);
		}
		else if (EsRuta(url, "/sexos"))
		{
			api = URLSexo(url, method, data);
			return GenerarRespuesta(conn, api);
		}
		else {
			api = (HTTP_response){
				.body = MensajeSimple("Not found"),
				.status = NOT_FOUND
			};
			return GenerarRespuesta(conn, api);
		}
	}
	// La llamada realizada era invalida o no se pudo procesar
	else {
		api = (HTTP_response){
			.body = MensajeSimple("Internal server error"),
			.status = INTERNAL_SERVER_ERROR
		};
	}
	return GenerarRespuesta(conn, api);
}
