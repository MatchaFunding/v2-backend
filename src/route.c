#include "../include/utils.h"
#include <microhttpd.h>
#include <setjmp.h>
#include "../include/route.h"

#include "../include/sexo.h"

jmp_buf ExceptionBuffer;

/* Muestra por pantalla la request y metodo solicitados por el cliente */
void LoguearAPI(const char *url, const char *method) {
	printf("[%s] %s\n", method, url);
}

/* Se usa la funcion "GestorPrincipal" para redirigir las
llamadas en base al tipo de objeto que se esta invocando

(es similar a los Routers en FastAPI) */
enum MHD_Result GestorPrincipal (
	void *cls, struct MHD_Connection *conn,
	const char *url, const char *method,
	const char *ver, const char *data,
	size_t *data_size, void **con_cls
)
{
	// Muestra la llamada por pantalla
	LoguearAPI(url, method);

	// Redirigimos al controlador especifico de cada objeto
	// Se genera la respuesta tras llamar una API valida
	if (setjmp(ExceptionBuffer) == 0) {
		if (strcmp(url, "/") == 0) {
			char *msg = MensajeSimple("BackEnd activo!");
			return CrearRespuesta(conn, msg, OK);
		}
		else if (EsRuta(url, "/sexos")) {
			return URLSexo (
				cls, conn, url, method,
				ver, data, data_size, con_cls
			);
		}
		else {
			char *msg = MensajeSimple("Not found");
			return CrearRespuesta(conn, msg, NOT_FOUND);
		}
	}
	// La llamada realizada era invalida o no se pudo procesar
	char *msg = MensajeSimple("Error");
	unsigned int err = INTERNAL_SERVER_ERROR;
	return CrearRespuesta(conn, msg, err);
}
