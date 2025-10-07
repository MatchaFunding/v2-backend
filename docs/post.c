#include <microhttpd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h>

#define PORT 8080
#define POSTBUFFERSIZE 8192

struct Persona {
    char *Nombre;
    char *Sexo;
    char *RUT;
    char *FechaDeNacimiento;
};

struct connection_info_struct {
    struct MHD_PostProcessor *pp;
    char *json_data;
    size_t json_size;
};

// Función auxiliar para enviar una respuesta HTTP
static enum MHD_Result send_response(struct MHD_Connection *connection, const char *msg, unsigned int status) {
    struct MHD_Response *response = MHD_create_response_from_buffer(strlen(msg), (void *)msg, MHD_RESPMEM_PERSISTENT);
    enum MHD_Result ret = MHD_queue_response(connection, status, response);
    MHD_destroy_response(response);
    return ret;
}

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

// Maneja las solicitudes POST
static enum MHD_Result answer_to_connection(void *cls, struct MHD_Connection *connection,
                                            const char *url, const char *method,
                                            const char *version, const char *upload_data,
                                            size_t *upload_data_size, void **req_cls)
{
    (void)cls; (void)url; (void)version;

    if (strcmp(method, "POST") != 0)
        return send_response(connection, "Solo se permiten POST", MHD_HTTP_METHOD_NOT_ALLOWED);

    struct connection_info_struct *con_info = *req_cls;

    // Primera vez que entra
    if (!con_info) {
        con_info = calloc(1, sizeof(struct connection_info_struct));
        con_info->json_data = malloc(POSTBUFFERSIZE);
        con_info->json_data[0] = '\0';
        con_info->json_size = 0;
        *req_cls = (void *)con_info;
        return MHD_YES;
    }

    // Mientras llegan los datos (stream)
    if (*upload_data_size > 0) {
        if (con_info->json_size + *upload_data_size < POSTBUFFERSIZE - 1) {
            memcpy(con_info->json_data + con_info->json_size, upload_data, *upload_data_size);
            con_info->json_size += *upload_data_size;
            con_info->json_data[con_info->json_size] = '\0';
        }
        *upload_data_size = 0;
        return MHD_YES;
    } else {
        // Se recibió todo el cuerpo → procesar JSON
        enum MHD_Result res = handle_json_data(con_info->json_data);
        free(con_info->json_data);
        free(con_info);
        *req_cls = NULL;
        if (res == MHD_YES)
            return send_response(connection, "Persona procesada correctamente\n", MHD_HTTP_OK);
        else
            return send_response(connection, "Error al procesar JSON\n", MHD_HTTP_BAD_REQUEST);
    }
}

int main() {
    struct MHD_Daemon *daemon;

    printf("🚀 Servidor iniciado en http://localhost:%d/persona/\n", PORT);

    daemon = MHD_start_daemon(
        MHD_USE_AUTO | MHD_USE_INTERNAL_POLLING_THREAD,
        PORT,
        NULL,
        NULL,
        &answer_to_connection,
        NULL,
        MHD_OPTION_END);

    if (!daemon) {
        fprintf(stderr, "No se pudo iniciar el servidor\n");
        return 1;
    }

    getchar(); // Espera tecla para detener

    MHD_stop_daemon(daemon);
    return 0;
}

