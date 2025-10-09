#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <cjson/cJSON.h>
#include "../../include/utils.h"
#include "../../include/query.h"
#include "../../include/cache.h"
#include "../../include/sexo.h"

struct Persona {
    char *Nombre;
    char *Sexo;
    char *RUT;
    char *FechaDeNacimiento;
};

// Procesa los datos JSON recibidos
static enum MHD_Result handle_json_data(const char *data) {
    printf("JSON recibido:\n%s\n\n", data);

    cJSON *json = cJSON_Parse(data);
    if (!json) {
        printf("❌ Error al parsear JSON.\n");
        return MHD_NO;
    }
    struct Persona persona;
    persona.Nombre = strdup(cJSON_GetObjectItemCaseSensitive(json, "Nombre")->valuestring);
    persona.Sexo = strdup(cJSON_GetObjectItemCaseSensitive(json, "Sexo")->valuestring);
    persona.RUT = strdup(cJSON_GetObjectItemCaseSensitive(json, "RUT")->valuestring);
    persona.FechaDeNacimiento = strdup(cJSON_GetObjectItemCaseSensitive(json, "FechaDeNacimiento")->valuestring);

    printf("✅ Persona creada:\n");
    printf("Nombre: %s\n", persona.Nombre);
    printf("Sexo: %s\n", persona.Sexo);
    printf("RUT: %s\n", persona.RUT);
    printf("Fecha de Nacimiento: %s\n", persona.FechaDeNacimiento);

    free(persona.Nombre);
    free(persona.Sexo);
    free(persona.RUT);
    free(persona.FechaDeNacimiento);
    cJSON_Delete(json);
    return MHD_YES;
}

/* Gestiona y enruta las llamadas hacia los instrumentos */
enum MHD_Result URLSexo
	(void *cls, struct MHD_Connection *conn,
	const char *url, const char *method,
	const char *ver, const char *data,
	size_t *data_size, void **con_cls)
{
	// Este metodo se invoca para leer datos desde el cliente
	if (strcmp(method, "GET") == 0) {
		const char *query = "SELECT * FROM VerSexos";
		char *result = EjecutarQueryEnJSON(query, DB);
		return CrearRespuesta(conn, result, MHD_HTTP_OK);
	}
	// Este metodo se invoca para crear datos a partir de lo que envia el cliente
	if (strcmp(method, "POST") == 0) {
		ConnectionInfo *con_info = *con_cls;
		// Primera vez que entra
		if (!con_info) {
			con_info = calloc(1, sizeof(ConnectionInfo));
			con_info->json_data = malloc(POSTBUFFERSIZE);
			con_info->json_data[0] = '\0';
			con_info->json_size = 0;
			*con_cls = (void *)con_info;
			return MHD_YES;
		}
		// Mientras llegan los datos (stream)
		if (*data_size > 0) {
			if (con_info->json_size + *data_size < POSTBUFFERSIZE - 1) {
				memcpy(con_info->json_data + con_info->json_size, data, *data_size);
				con_info->json_size += *data_size;
				con_info->json_data[con_info->json_size] = '\0';
			}
			*data_size = 0;
			return MHD_YES;
		}
		// Se recibió todo el cuerpo → procesar JSON
		else {
			enum MHD_Result res = handle_json_data(con_info->json_data);
			free(con_info->json_data);
			free(con_info);
			*con_cls = NULL;
			if (res == MHD_YES)
				return CrearRespuesta(conn, "Persona procesada\n", MHD_HTTP_OK);
		}
	}
	return CrearRespuesta(conn, "Llamada invalida!\n", MHD_HTTP_BAD_REQUEST);
}
